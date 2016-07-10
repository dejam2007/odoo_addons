# -*- coding: utf-8 -*-
from openerp import http

# class Dcm(http.Controller):
#     @http.route('/dcm/dcm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dcm/dcm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dcm.listing', {
#             'root': '/dcm/dcm',
#             'objects': http.request.env['dcm.dcm'].search([]),
#         })

#     @http.route('/dcm/dcm/objects/<model("dcm.dcm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dcm.object', {
#             'object': obj
#         })