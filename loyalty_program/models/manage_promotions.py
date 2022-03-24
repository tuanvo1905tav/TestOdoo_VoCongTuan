# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManagePromotions(models.Model):
    _name = 'manage.promotions'
    _description = 'Manage promotions'

    name = fields.Char('Loyalty Program Name', required=True)
    points = fields.Float('Points (%)', required=True)
    active = fields.Boolean('Active', required=True, default=True)
