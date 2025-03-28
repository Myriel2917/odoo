from odoo import models, fields


class DataCenter(models.Model):
    _name = 'data.center'
    _description = 'Data Center'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
