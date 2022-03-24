from odoo import fields, models, api


class PartnerLevels(models.Model):
    _name = 'partner.levels'
    _description = 'Partner Levels'

    name = fields.Char('Name', required=True)
    loyalty_points = fields.Float('Loyalty Points', required=True)
    description = fields.Text('Description')
