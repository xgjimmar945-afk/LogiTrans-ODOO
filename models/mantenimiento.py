# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LogitransMantenimiento(models.Model):
    _name = 'logitrans.mantenimiento'
    _description = 'Mantenimiento de vehículo'
    _rec_name = 'fecha'

    vehiculo_id = fields.Many2one(
        'logitrans.vehiculo',
        string='Vehículo',
        required=True,
        ondelete='cascade'
    )

    fecha = fields.Date(
        string='Fecha de mantenimiento',
        required=True,
        default=fields.Date.today
    )

    tipo = fields.Selection(
    selection=[
        ('itv', 'ITV'),
        ('preventivo', 'Preventivo'),
        ('reparacion', 'Reparación'),
        ('estetico', 'Estético'),
    ],
    string='Tipo de mantenimiento',
    required=True,
    default='preventivo'
    )

    coste = fields.Float(
        string='Coste (€)',
        default=0.0
    )

    descripcion = fields.Text(
        string='Descripción'
    )

    #Workflow:
    state = fields.Selection(
        selection=[
            ('solicitud', 'Solicitud'),
            ('programado', 'Programado'),
            ('en_proceso', 'En proceso'),
            ('realizado', 'Realizado'),
            ('cancelado', 'Cancelado'),
        ],
        string='Estado',
        default='solicitud',
        required=True
    )

    observaciones = fields.Text(string='Motivo Cancelación:')

    #el coste no puede ser negativo:
    @api.constrains('coste')
    def _check_coste(self):
        for record in self:
            if record.coste is not None and record.coste < 0:
                raise ValidationError("El coste del mantenimiento no puede ser negativo.")
            
    #onChange para los botones:
    @api.onchange('state')
    def _onchange_state(self):
        for record in self:
            if record.state == 'cancelado' and not record.observaciones:
                return {
                    'warning': {
                        'title': "Falta motivo",
                        'message': "Mantenimiento cancelado, escriba el motivo: "
                    }
                }
            
    #restriccion del state- si cancela tiene que llenar observaciones.
    @api.constrains('state', 'observaciones')
    def _check_motivo_cancelacion(self):
        for record in self:
            if record.state == 'cancelado' and not (record.observaciones or '').strip():
                raise ValidationError("Para cancelar un mantenimiento debes indicar el motivo de la cancelación.")
            
    #botones/transiciones: 
    def action_programar(self):
        for record in self:
            # Regla: debe existir fecha y tipo para programar
            if not record.fecha or not record.tipo:
                raise ValidationError("Para programar, debes indicar Fecha y Tipo de mantenimiento.")
            record.write({'state': 'programado'})

    def action_iniciar(self):
        for record in self:
            if record.state != 'programado':
                raise ValidationError("Solo se puede iniciar un mantenimiento que esté en estado Programado.")
            record.write({'state': 'en_proceso'})

    def action_finalizar(self):
        for record in self:
            if record.state != 'en_proceso':
                raise ValidationError("Solo se puede finalizar un mantenimiento que esté En proceso.")
            record.write({'state': 'realizado', 'realizado': True})

    def action_cancelar(self):
        for record in self:
            if record.state == 'realizado':
                raise ValidationError("No se puede cancelar un mantenimiento que ya está Realizado.")
            # La obligación del motivo controla el constrains, aquí solo cambiamos state
            record.write({'state': 'cancelado'})       
