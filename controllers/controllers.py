# -*- coding: utf-8 -*-
from odoo import http

# class OdooMusica(http.Controller):
#     @http.route('/odoo_musica/odoo_musica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_musica/odoo_musica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_musica.listing', {
#             'root': '/odoo_musica/odoo_musica',
#             'objects': http.request.env['odoo_musica.odoo_musica'].search([]),
#         })

#     @http.route('/odoo_musica/odoo_musica/objects/<model("odoo_musica.odoo_musica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_musica.object', {
#             'object': obj
#         })