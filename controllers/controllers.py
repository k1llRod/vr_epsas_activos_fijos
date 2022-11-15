# -*- coding: utf-8 -*-
# from odoo import http


# class VrEpsasActivosFijos(http.Controller):
#     @http.route('/vr_epsas_activos_fijos/vr_epsas_activos_fijos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vr_epsas_activos_fijos/vr_epsas_activos_fijos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vr_epsas_activos_fijos.listing', {
#             'root': '/vr_epsas_activos_fijos/vr_epsas_activos_fijos',
#             'objects': http.request.env['vr_epsas_activos_fijos.vr_epsas_activos_fijos'].search([]),
#         })

#     @http.route('/vr_epsas_activos_fijos/vr_epsas_activos_fijos/objects/<model("vr_epsas_activos_fijos.vr_epsas_activos_fijos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vr_epsas_activos_fijos.object', {
#             'object': obj
#         })
