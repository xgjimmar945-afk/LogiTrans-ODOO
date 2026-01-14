from odoo import models, fields, api


class Envios(models.Model):
    _name = "logitrans.envios"
    _description = "Envios"

    nombre = fields.Char(
        string="Nombre", required=True, help="Nombre"
    )
    fecha_creacion = fields.Date(
        string="Fecha de creación", required=True, help="Fecha de creación"
    )

    peso_kg = fields.Integer("Peso en kg")
    """ tipos_cargas_id = fields.Many2many(
        "logi_trans.tipos_cargas", string="Tipos de carga"
    )

    vehiculo_id = fields.Many2one("logi_trans.vehiculos", string="Vehiculo")
    conductor_id = fields.Many2one("logi_trans.conductores", string="Conductor") """
