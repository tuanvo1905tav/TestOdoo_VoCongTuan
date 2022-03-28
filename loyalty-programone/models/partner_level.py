from odoo import fields, models, api


class PartnerLevel(models.Model):
    _name = 'partner.level'
    _description = 'Description'

    name = fields.Char('Name', required=True)
    loyalty_points = fields.Float('Loyalty point', required=True)
    description = fields.Text('Description')
