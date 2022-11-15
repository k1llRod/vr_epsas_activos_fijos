# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class vr_epsas_activos_fijos(models.Model):
#     _name = 'vr_epsas_activos_fijos.vr_epsas_activos_fijos'
#     _description = 'vr_epsas_activos_fijos.vr_epsas_activos_fijos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
