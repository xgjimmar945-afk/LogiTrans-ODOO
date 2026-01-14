from odoo import models, fields, api


class Rutas(models.Model):
    _name = "logitrans.rutas"
    _description = "Rutas"

    tipo_ruta = fields.Selection(
        [
            ("ruta", "Ruta"),
            ("ruta", "Ruta"),
        ],
        string="Tipo de ruta",
        required=True,
        help="Tipo de ruta",
    )
    distancia_estimada = fields.Float(
        string="Distancia estimada", required=True, help="Distancia estimada"
    )
    
