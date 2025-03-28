from odoo import models, fields


class Solution(models.Model):
    _name = 'solution'
    _description = 'Solución'

    name = fields.Char(string='Nombre', required=True)
    capacity = fields.Float(string='Capacidad')
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
