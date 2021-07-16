# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class h4o_banariego(models.Model):
#     _name = 'h4o_banariego.h4o_banariego'
#     _description = 'h4o_banariego.h4o_banariego'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
