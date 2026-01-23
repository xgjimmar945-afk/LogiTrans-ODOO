# -*- coding: utf-8 -*-
import re  # esto es una libreria de python para expresiones regulares para las validaciones...
from odoo import models, fields, api
from odoo.exceptions import ValidationError

MATRICULA_RE = re.compile(
    r"^\d{4}[A-Z]{3}$"
)  # sera global asi no la llama cada vez en el bucle


class LogitransVehiculo(models.Model):
    _name = "logitrans.vehiculo"
    _description = "Vehículo"
    _rec_name = "matricula"

    foto = fields.Image(string="Foto", max_width=1200, max_height=1200)

    anio_fabricacion = fields.Selection(
        [(str(y), str(y)) for y in range(fields.Date.today().year, 1950, -1)],
        string="Año de fabricación",
        help="Año del modelo del vehículo. Dato técnico para identificación de piezas.",
    )

    fecha_matriculacion = fields.Date(
        string="Fecha de matriculación",
        help="Fecha de primera matriculación. Base legal para ITV y revisiones.",
    )

    antiguedad = fields.Integer(
        string="Antigüedad (años)", compute="_compute_antiguedad", store=False
    )

    matricula = fields.Char(
        string="Matrícula", required=True, index=True, help="Formato 1234ABC o 1234 ABC"
    )
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    capacidad_kg = fields.Float(string="Capacidad (kg)", default=0.0)
    activo = fields.Boolean(string="Activo", default=True)

    mantenimiento_ids = fields.One2many(
        "logitrans.mantenimiento", "vehiculo_id", string="Mantenimientos"
    )

    tipo_carga_ids = fields.Many2many(
        "logitrans.tipo_carga", string="Tipos de carga autorizados"
    )

    envios_ids = fields.One2many("logitrans.envios", "vehiculo_id", string="Envíos")

    _sql_constraints = [
        ("matricula_unique", "unique(matricula)", "La matrícula ya existe.")
    ]

    # esto es para que si el usuario ingresa 1234ABC o 1234 abc lo reescribe y lo unifica todo en el mismo formato
    # asi puede comparar realmente que es la misma matrícula. Recrea el valor y en write lo reescribe.
    def _normalize_matricula(self, m):
        # deja "1234 ABC" como "1234ABC" y lo pone en mayúsculas
        return re.sub(r"\s+", "", (m or "").strip()).upper()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "matricula" in vals:
                vals["matricula"] = self._normalize_matricula(vals["matricula"])
        return super().create(vals_list)

    def write(self, vals):
        if "matricula" in vals:
            vals["matricula"] = self._normalize_matricula(vals["matricula"])
        return super().write(vals)

    # aqui se hace la validacion del formato:
    @api.constrains("matricula")
    def _check_matricula_es(self):
        for record in self:
            if not record.matricula:
                continue

            value = self._normalize_matricula(record.matricula)

            if not MATRICULA_RE.match(value):
                raise ValidationError("Matrícula inválida: usa 1234ABC o 1234 ABC")

    # aqui calcula la antiguedad del coche para las revisiones tecnicas(ITV)
    @api.depends(
        "fecha_matriculacion"
    )  # esto es para que recalcule el campo, en caso de cambiarlo manualmente, pero por lo general lo recalcula al recargar la vista.
    def _compute_antiguedad(self):
        hoy = fields.Date.today()
        for record in self:
            if record.fecha_matriculacion:
                record.antiguedad = hoy.year - record.fecha_matriculacion.year
            else:
                record.antiguedad = 0

    @api.constrains("capacidad_kg")
    def _check_capacidad(self):
        for record in self:
            if record.capacidad_kg is not None and record.capacidad_kg < 0:
                raise ValidationError("La capacidad (kg) no puede ser negativa.")

    # esto es para saber las piezas de recambios a que modelo y año corresponden
    @api.constrains("anio_fabricacion", "fecha_matriculacion")
    def _check_fechas_vehiculo(self):
        for record in self:
            if record.anio_fabricacion and record.fecha_matriculacion:
                anio = int(
                    record.anio_fabricacion
                )  # <-- como entra de un select como string hay que pasarlo a int para validar

                if anio > record.fecha_matriculacion.year:
                    raise ValidationError(
                        "El año de fabricación no puede ser posterior a la fecha de matriculación."
                    )
