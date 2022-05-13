# -*- coding: utf-8 -*-
# from odoo import http


# class UserTestModule(http.Controller):
#     @http.route('/user_test_module/user_test_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_test_module/user_test_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_test_module.listing', {
#             'root': '/user_test_module/user_test_module',
#             'objects': http.request.env['user_test_module.user_test_module'].search([]),
#         })

#     @http.route('/user_test_module/user_test_module/objects/<model("user_test_module.user_test_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_test_module.object', {
#             'object': obj
#         })
