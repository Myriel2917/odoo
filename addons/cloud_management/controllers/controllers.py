from odoo import http
from odoo.http import request


class CloudManagement(http.Controller):
    @http.route('/cloud_management/hello', auth='public', website=True)
    def hello(self, **kw):
        return "¡Hola, este es el módulo Cloud Management funcionando correctamente! 🎉"

    @http.route('/cloud_management/data_centers', auth='public', methods=['GET'], type='json')
    def list_data_centers(self, **kw):
        data_centers = request.env['data.center'].sudo().search([])
        data_list = []
        for data in data_centers:
            data_list.append({
                'name': data.name,
                'description': data.description,
                'price': data.price,
            })
        return {'data_centers': data_list}
