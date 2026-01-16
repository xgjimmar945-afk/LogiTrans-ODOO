# -*- coding: utf-8 -*-
from odoo import models, fields

class LogitransTipoCarga(models.Model):
    _name = 'logitrans.tipo_carga'
    _description = 'Tipo de carga'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')