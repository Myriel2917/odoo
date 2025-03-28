from odoo import models, fields

# Modelo para Data Center
class DataCenter(models.Model):
    _name = 'data.center'
    _description = 'Data Center'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    price = fields.Float('Precio')

# Modelo para SLA
class SLA(models.Model):
    _name = 'sla'
    _description = 'Service Level Agreement'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    price = fields.Float('Precio')

# Modelo para Tipo de Pagos
class PaymentType(models.Model):
    _name = 'payment.type'
    _description = 'Tipo de Pago'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    price = fields.Float('Precio')

# Modelo para Cloud Powerback
class CloudPowerback(models.Model):
    _name = 'cloud.powerback'
    _description = 'Cloud Powerback'
    name = fields.Char('Nombre', required=True)
    capacity = fields.Integer('Capacidad (GB)')
    description = fields.Text('Descripción')
    price = fields.Float('Precio')

# Modelo para Solución
class Solution(models.Model):
    _name = 'solution'
    _description = 'Solución'
    name = fields.Char('Nombre', required=True)
    capacity = fields.Integer('Capacidad (GB)')
    description = fields.Text('Descripción')
    price = fields.Float('Precio')
