# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LogitransMantenimiento(models.Model):
    _name = 'logitrans.mantenimiento'
    _description = 'Mantenimiento de vehículo'
    _rec_name = 'fecha'

    vehiculo_id = fields.Many2one(
        'logitrans.vehiculo',
        string='Vehículo',
        required=True,
        ondelete='cascade'
    )

    fecha = fields.Date(
        string='Fecha de mantenimiento',
        required=True,
        default=fields.Date.today
    )

    tipo = fields.Selection(
    selection=[
        ('itv', 'ITV'),
        ('preventivo', 'Preventivo'),
        ('reparacion', 'Reparación'),
        ('estetico', 'Estético'),
    ],
    string='Tipo de mantenimiento',
    required=True,
    default='preventivo'
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

    @api.constrains('coste')
    def _check_coste(self):
        for record in self:
            if record.coste is not None and record.coste < 0:
                raise ValidationError("El coste del mantenimiento no puede ser negativo.")