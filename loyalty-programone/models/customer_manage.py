from odoo import fields, models, api


class CustomerManage(models.Model):
    _inherit = 'res.partner'
    _description = 'Decription'

    loyalty_point = fields.Float('Loyalty point')
    loyalty_level = fields.Many2one(comodel_name='partner.level')
    loyalty_levels = fields.Char('Loyalty level', compute='_get_level_loyalty')
    point_level = fields.Float(related='loyalty_level.loyalty_points')

    @api.model
    def _get_level_loyalty(self):
        if self.loyalty_point <= 1000:
            self.loyalty_levels = 'Đồng'
        elif (self.loyalty_point > 1000) and (self.loyalty_point <= 2000):
            self.loyalty_levels = 'Bạc'
        elif (self.loyalty_point > 2000) and (self.loyalty_point <= 3000):
            self.loyalty_levels = 'Vàng'
        if self.loyalty_point > 3000:
            self.loyalty_levels = 'Kim cương'
