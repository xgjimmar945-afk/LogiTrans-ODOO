# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Conductor(models.Model):
    _name = "logitrans.conductor"
    _description = "Conductor"
    _inherit = "logitrans.persona"

    type_licencia = fields.Selection(
        [
            ("B", "Carnet B - Turismos"),
            ("C", "Carnet C - Camiones"),
            ("D", "Carnet D - autobuses"),
        ],
        string="Tipo de Licencia",
        required=True,
    )
    points_licencia = fields.Integer(string="Puntos de Licencia", required=True)
    fecha_vencimiento_licencia = fields.Date(
        string="Fecha de Vencimiento de Licencia", required=True
    )

    # Campos computados
    days_to_expiration = fields.Integer(
        string="Días para Vencimiento",
        compute="_compute_days_to_expiration",
        store=True,
    )

    # Workflow (Activo, En Reserva, Inactivo)
    state = fields.Selection(
        [
            ("activo", "Activo"),
            ("en_reserva", "En Reserva"),
            ("inactivo", "Inactivo"),
        ],
        string="Estado",
        default="activo",
        track_visibility="onchange",
    )

    envios_ids = fields.One2many(
        "logitrans.envios",
        "conductor_id",
        string="Envios",
        help="Envios",
    )

    # Funcionamiento Workflow

    # Boton para activar desde En Reserva o Inactivo
    def action_activar(self):
        for record in self:
            if record.state in ["en_reserva", "inactivo"]:
                record.state = "activo"
            else:
                raise ValidationError("Este conductor ya está activo")

    # Botón para pasar de Activo a En Reserva
    def action_reserva(self):
        for record in self:
            if record.state == "activo":
                record.state = "en_reserva"
            else:
                raise ValidationError(
                    "Solo puedes poner en reserva un conductor activo"
                )

    # Botón para pasar de Activo a Inactivo
    def action_inactivar(self):
        for record in self:
            if record.state == "activo":
                record.state = "inactivo"
            else:
                raise ValidationError("Solo puedes inactivar un conductor activo")

    # Comportamiento No Básicos

    @api.depends("fecha_vencimiento_licencia")
    def _compute_days_to_expiration(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_vencimiento_licencia:
                diff = record.fecha_vencimiento_licencia - today
                record.days_to_expiration = diff.days
            else:
                record.days_to_expiration = 0

    # Comprobación para tener más de los 15 puntos del carnet ni tener números negativos
    @api.constrains("points_licencia")
    def _check_points_licencia(self):
        for record in self:
            if record.points_licencia < 0 or record.points_licencia > 15:
                raise ValidationError("Los puntos de licencia no pueden ser negativos")

    # Comprobación para enviar a inactivo automáticamente cuando un conductor activa tiene 0 puntos del carnet
    @api.constrains("points_licencia", "state")
    def _auto_inactivar_por_puntos(self):
        for record in self:
            if record.points_licencia == 0 and record.state == "activo":
                record.state = "inactivo"

    # Onchange para mostrar advertencia de que el conductor será puesto en inactivo si sus puntos están en 0
    @api.onchange("points_licencia")
    def _onchange_points_auto_inactivo(self):
        """Mostrar advertencia si puntos llegan a 0"""
        if self.points_licencia == 0 and self.state == "activo":
            return {
                "warning": {
                    "title": "Advertencia",
                    "message": "El conductor será puesto automáticamente en INACTIVO al guardar porque tiene 0 puntos de carnet.",
                }
            }
