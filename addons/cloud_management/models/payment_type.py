from odoo import models, fields


class PaymentType(models.Model):
    _name = 'payment.type'
    _description = 'Tipo de Pago'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    price = fields.Float(string='Precio')
