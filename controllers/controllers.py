# -*- coding: utf-8 -*-
# from odoo import http


# class Logitrans(http.Controller):
#     @http.route('/logitrans/logitrans/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/logitrans/logitrans/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('logitrans.listing', {
#             'root': '/logitrans/logitrans',
#             'objects': http.request.env['logitrans.logitrans'].search([]),
#         })

#     @http.route('/logitrans/logitrans/objects/<model("logitrans.logitrans"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('logitrans.object', {
#             'object': obj
#         })
