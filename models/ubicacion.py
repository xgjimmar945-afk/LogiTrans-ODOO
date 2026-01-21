from odoo import models, fields, api


class Ubicacion(models.Model):
    _name = "logitrans.ubicacion"
    _description = "Ubicacion"

    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True, size=60)
    provincia = fields.Many2one(
        "res.country.state", string="Provincia", required=True, size=60
    )

    fecha_actual = fields.Datetime(
        string="Fecha Actual",
        default=fields.Datetime.now,
    )

    ciudad = fields.Char(string="Ciudad", required=True, size=60)
    direccion = fields.Char(string="Direccion", required=True, size=60)

    longitud = fields.Float(string="Longitud", required=True, size=10)
    latitud = fields.Float(string="Latitud", required=True, size=10)

    rutas_origen_ids = fields.One2many(
        "logitrans.rutas",
        "origen_ubicacion_id",
        string="Rutas de origen",
        
        
    )
    rutas_destino_ids = fields.One2many(
        "logitrans.rutas",
        "destino_ubicacion_id",
        string="Rutas de destino",
        
        
    )

    _sql_constraints = [
        ('latitud_longitud_unique', 'UNIQUE(latitud, longitud)', 'No pueden existir la misma Longitud y Latitud en dos ubicaciones'),
    ] 
