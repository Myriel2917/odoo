from odoo import http


class CloudManagement(http.Controller):
    @http.route('/cloud_management', auth='public')
    def index(self, **kw):
        return "Cloud Management Module Working!"
