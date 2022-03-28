# -*- coding: utf-8 -*-
# from odoo import http


# class Loyalty-programone(http.Controller):
#     @http.route('/loyalty-programone/loyalty-programone', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyalty-programone/loyalty-programone/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyalty-programone.listing', {
#             'root': '/loyalty-programone/loyalty-programone',
#             'objects': http.request.env['loyalty-programone.loyalty-programone'].search([]),
#         })

#     @http.route('/loyalty-programone/loyalty-programone/objects/<model("loyalty-programone.loyalty-programone"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyalty-programone.object', {
#             'object': obj
#         })
