# -*- coding: utf-8 -*-

import re  #esto es una libreria de python para expresiones regulares para las validaciones...
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LogitransVehiculo(models.Model):
    _name = 'logitrans.vehiculo'
    _description = 'Vehículo'

    name = fields.Char(string='Nombre', required=False)

    matricula = fields.Char(
        string = 'Matricula',
        required=True,
        index=True,
        help="Formato 1234ABC o 1234 ABC"
    )
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')

    capacidad_kg = fields.Float(string='Capacidad (kg)', default=0.0)
    activo = fields.Boolean(string='Activo', default=True)

    mantenimiento_ids = fields.One2many(
        'logitrans.mantenimiento',
        'vehiculo_id',
        string='Mantenimientos'
    )
    _sql_constraints = [
        ('matricula_unique','unique(matricula)','La matrícula ya existe.')

    ]

    @api.constrains('matricula')
    def _check_matricula_es(self):
        """
        Validación sencilla de matrícula española
        -4digitos
        -3 letras
        -permite espacio opcional: 1234 ABC o 1234ABC
        """
        patron= re.compile(r'^\d{4}\s?[A-Z]{3}$')

        for rec in self:
            if not rec.matricula:
                continue
            value = rec.matricula.strip().upper()
            #para guardar la matricula toda en upper case.
            rec.matricula = value

            if not patron.match(value):
                raise ValidationError(
                    "Matricula inválida usa el formato: 1234ABC o 1234 ABC"
                )
    
    @api.constrains('capacidad_kg')
    def _check_capacidad(self):
        for rec in self:
            if rec.capacidad_kg is not None and rec.capacidad_kg < 0:
                raise ValidationError("La capacidad en (kg) no puede ser negativa.")   