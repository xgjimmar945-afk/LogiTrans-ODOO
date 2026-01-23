from odoo import models, fields, api


class Envios(models.Model):
    _name = "logitrans.envios"
    _description = "Envios"

    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True, help="Nombre")
    fecha_creacion = fields.Date(
        string="Fecha de creación", required=True, help="Fecha de creación"
    )

    fecha_actual = fields.Datetime(
        string="Fecha Actual",
        default=fields.Datetime.now,
    )

    state = fields.Selection(
        [
            ("entregado", "Entregado"),
            ("camino", "En Camino"),
            ("fabrica", "En Fabrica"),
        ],
        "Estado",
        default="fabrica",
    )

    peso_kg = fields.Integer("Peso en kg")

    total_distancia = fields.Float(
        string="Distancia Total", compute="_compute_total_distancia"
    )

    @api.depends("rutas_ids")
    def _compute_total_distancia(self):
        for record in self:
            record.total_distancia = sum(
                ruta.distancia_estimada for ruta in record.rutas_ids
            )

    rutas_ids = fields.Many2many(
        "logitrans.rutas", string="Rutas", required=True, help="Rutas"
    )

    _sql_constraints = [
        ("envios_nombre_unique", "UNIQUE (nombre)", "El nombre debe ser único")
    ]

    vehiculo_id = fields.Many2one("logitrans.vehiculo", string="Vehiculo que se encarga del envío")

    """ 
    conductor_id = fields.Many2one("logi_trans.conductores", string="Conductor") """

    @api.constrains("peso_kg")
    def _check_peso_kg(self):
        for record in self:
            if record.peso_kg < 0 or record.peso_kg > 10000:
                raise models.ValidationError(
                    "El peso debe ser mayor o igual a 0 y menor o igual a 10000."
                )

    def btn_borrarRutas(self):
        self.write({"rutas_ids": [(5, 0, 0)]})

    def btn_submit_to_fabrica(self):
        self.write({"state": "fabrica"})

    def btn_submit_to_camino(self):
        self.write({"state": "camino"})

    def btn_submit_to_entregado(self):
        self.write({"state": "entregado"})

    def btn_generar_informe(self):
        return self.env.ref("logitrans.logitrans_report_envios_action").report_action(
            self
        )
