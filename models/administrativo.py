# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Administrativo(models.Model):
    _name = 'logitrans.administrativo'
    _description = 'Administrativo'
    _inherit = 'logitrans.persona'

    departamento = fields.Selection([
        ('administracion', 'Administración'),
        ('finanzas', 'Finanzas'),
        ('recursos_humanos', 'Recursos Humanos'),
        ('marketing', 'Marketing'),
    ], string="Departamento", required=True)

    extension_telefonica = fields.Char(string="Extensión Telefónica", required=True)

    nivel_acceso = fields.Selection([
        ('1', 'Nivel Lector'),
        ('2', 'Nivel Escritor'),
        ('3', 'Supervisor'),
        ('4', 'Gestor'),
        ('5', 'Administrador')
    ], string="Nivel de Acceso", required=True)