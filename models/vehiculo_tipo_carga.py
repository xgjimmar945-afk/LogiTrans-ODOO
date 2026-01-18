# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class LogitransVehiculoTipoCarga(models.Model):
    _name = 'logitrans.vehiculo_tipo_carga'
    _description = 'Autorizacion Vehículo - Tipo de Carga'

    name= fields.Char(string="Referencia", compute="_compute_name", store=True)

    vehiculo_id = fields.Many2one(
        'logitrans.vehiculo',
        string='Vehiculo',
        required=True,
        ondelete='cascade'
    )

    tipo_carga_id = fields.Many2one(
        'logitrans.tipo_carga',
        string='Tipo de carga',
        required=True,
        ondelete='cascade'
    )

    vigente = fields.Boolean(string='Vigente', default=True)
    
    #se agregan los campos adicionales para poder mostrar vistas del modelo propio de la relacion many2many
    #suponemos un permiso que tiene el vehiculo con una fecha de autorización
    fecha_autorizacion = fields.Date(
        string='Fecha de autorización',
        default=fields.Date.today,
        required=True
    )

    proxima_renovacion = fields.Date(
        string='Próxima renovación',
        help='Fecha prevista para revisar/renovar la autorización.'
    )

    limite_kg = fields.Float(string='Límite autorizado (kg)', default=0.0)

    observaciones = fields.Text(string='Observaciones')


    @api.depends('vehiculo_id', 'tipo_carga_id')
    def _compute_name(self):
        for rec in self:
            v = rec.vehiculo_id.display_name if rec.vehiculo_id else ''
            t = rec.tipo_carga_id.display_name if rec.tipo_carga_id else ''
            rec.name = f"{v} - {t}" if (v or t) else "Autorización"

    @api.constrains('limite_kg')
    def _check_limite_kg(self):
        for rec in self:
            if rec.limite_kg is not None and rec.limite_kg < 0:
                raise ValidationError(_("El límite (kg) no puede ser negativo."))

    @api.constrains('fecha_autorizacion', 'proxima_renovacion')
    def _check_fechas(self):
        for rec in self:
            if rec.fecha_autorizacion and rec.proxima_renovacion:
                if rec.proxima_renovacion < rec.fecha_autorizacion:
                    raise ValidationError(_("La próxima renovación no puede ser anterior a la fecha de autorización."))

    _sql_constraints = [
        (
            'vehiculo_tipo_unique',
            'unique(vehiculo_id, tipo_carga_id)',
            'Ya existe una autorización para este vehículo y este tipo de carga.'
        ),
    ]