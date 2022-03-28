from odoo import fields, models, api


class CustomerManage(models.Model):
    _inherit = 'res.partner'
    _description = 'Decription'

    loyalty_point = fields.Float('Loyalty point')
    loyalty_level = fields.Many2one('partner.levels')
