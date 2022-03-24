from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Loyalty History'

    fk_promotion = fields.Many2one('manage.promotions', string='Promotions name')
    total_loyalty_points = fields.Float('Total loyalty point')
    money_spent = fields.Float('Total amount per order')
    #Hello mấy cưn:vv
    #đa tạ a hehe