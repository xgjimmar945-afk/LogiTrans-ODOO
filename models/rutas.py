from odoo import models, fields, api


class Rutas(models.Model):
    _name = "logitrans.rutas"
    _description = "Rutas"

    _rec_name = "tipo_ruta"

    tipo_ruta = fields.Selection(
        [
            ("Urbana", "Urbana / Local"),
            ("Provincial", "Provincial"),
            ("Nacional", "Nacional"),
            ("Internacional", "Internacional"),
        ],
        string="Tipo de ruta",
        required=True,
        help="Tipo de ruta",
    )
    distancia_estimada = fields.Float(
        string="Distancia estimada", required=True, help="Distancia estimada"
    )

    destino_ubicacion_id = fields.Many2one(
        "logitrans.ubicacion", string="Destino", help="Destino"
    )
    origen_ubicacion_id = fields.Many2one(
        "logitrans.ubicacion", string="Origen", help="Origen"
    )

    envios_ids = fields.Many2many(
        "logitrans.envios", string="Envios", required=True, help="Envios"
    )

    @api.onchange("origen_ubicacion_id", "destino_ubicacion_id")
    def _onchange_ubicaciones(self):
        if self.origen_ubicacion_id and self.destino_ubicacion_id:
            if self.origen_ubicacion_id == self.destino_ubicacion_id:
                return {
                    "warning": {
                        "title": "Error",
                        "message": "Origen y Destino no pueden ser iguales.",
                    }
                }

            if (
                self.origen_ubicacion_id.provincia
                == self.destino_ubicacion_id.provincia
            ):
                self.tipo_ruta = "Provincial"
            else:
                self.tipo_ruta = "Nacional"

    def btn_borrarUbicacionOrigen(self):
        for record in self:
            record.origen_ubicacion_id = False

    def btn_borrarUbicacionDestino(self):
        for record in self:
            record.destino_ubicacion_id = False
