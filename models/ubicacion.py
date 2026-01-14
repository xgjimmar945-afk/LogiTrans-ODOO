from odoo import models, fields, api

class Ubicacion(models.Model):
    _name = "logitrans.ubicacion"
    _description = "Ubicacion"

    provincia = fields.Many2one(
        "res.country.state", string="Provincia", required=True, help="Provincia"
    )

    ciudad = fields.Char(
        string="Ciudad", required=True, help="Ciudad"
    )
    direccion = fields.Char(
        string="Direccion", required=True, help="Direccion"
    )
    nombre = fields.Char(
        string="Nombre", required=True, help="Nombre"
    )   
    longitud = fields.Float(
        string="Longitud", required=True, help="Longitud"
    )
    latitud = fields.Float(
        string="Latitud", required=True, help="Latitud"
    )