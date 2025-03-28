from odoo import models, fields


class CloudPowerback(models.Model):
    _name = 'cloud.powerback'
    _description = 'Cloud PowerBack'

    name = fields.Char(string='Nombre', required=True)
    capacity = fields.Float(string='Capacidad')
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
