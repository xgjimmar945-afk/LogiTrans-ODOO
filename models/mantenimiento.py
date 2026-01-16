# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LogitransMantenimiento(models.Model):
    _name = 'logitrans.mantenimiento'
    _description = 'Mantenimiento de vehículo'

    vehiculo_id = fields.Many2one(
        'logitrans.vehiculo',
        string='Vehículo',
        required=True,
        ondelete='cascade'
    )

    fecha = fields.Date(
        string='Fecha de mantenimiento',
        required=True
    )

    tipo = fields.Char(
        string='Tipo de mantenimiento',
        required=True
    )

    coste = fields.Float(
        string='Coste (€)',
        default=0.0
    )

    descripcion = fields.Text(
        string='Descripción'
    )

    realizado = fields.Boolean(
        string='Realizado',
        default=False
    )