# -*- coding: utf-8 -*-
from odoo import http

# class TestApp(http.Controller):
#     @http.route('/test_app/test_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_app/test_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_app.listing', {
#             'root': '/test_app/test_app',
#             'objects': http.request.env['test_app.test_app'].search([]),
#         })

#     @http.route('/test_app/test_app/objects/<model("test_app.test_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_app.object', {
#             'object': obj
#         })