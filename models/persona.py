# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'logitrans.persona'
    _description = 'Persona'

    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Teléfono")
    birthdate = fields.Date(string="Fecha de Nacimiento")

    

    # Campo Computado para calcular la edad automaticamente
    age = fields.Integer(String="Edad", compute="_compute_age", store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365
            else:
                record.age = 0