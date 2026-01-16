# -*- coding: utf-8 -*-
from odoo import models, fields

class LogitransTipoCarga(models.Model):
    _name = 'logitrans.tipo_carga'
    _description = 'Tipo de carga'

    
    name = fields.Char(
        string='Tipo de carga',
        required=True)
    descripcion = fields.Text(
        string='Descripción del tipo'
    )

    nota_admin = fields.Text(
        string='Notas internas'
    )

    activo = fields.Boolean(
        string='Activo',
        default=True
    )
    vehiculo_ids = fields.Many2many(
        'logitrans.vehiculo',
        string='Vehículos autorizados'
    )