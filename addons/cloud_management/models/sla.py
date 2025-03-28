from odoo import models, fields


class SLA(models.Model):
    _name = 'sla'
    _description = 'Service Level Agreement'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
