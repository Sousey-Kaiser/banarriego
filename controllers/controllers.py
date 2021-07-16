# -*- coding: utf-8 -*-
# from odoo import http


# class H4oBanariego(http.Controller):
#     @http.route('/h4o_banariego/h4o_banariego/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/h4o_banariego/h4o_banariego/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('h4o_banariego.listing', {
#             'root': '/h4o_banariego/h4o_banariego',
#             'objects': http.request.env['h4o_banariego.h4o_banariego'].search([]),
#         })

#     @http.route('/h4o_banariego/h4o_banariego/objects/<model("h4o_banariego.h4o_banariego"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('h4o_banariego.object', {
#             'object': obj
#         })
