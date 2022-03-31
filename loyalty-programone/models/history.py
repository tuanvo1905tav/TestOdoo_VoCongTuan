from odoo import fields, models, api


class History(models.Model):
    _name = 'loyalty.history'
    _description = 'Description'

    partner_id = fields.Many2one(comodel_name='res.partner', string="Customer")
    loyalty_points = fields.Float('Total point')
    money_spent = fields.Float('Total money')
    loyalty_point = fields.Float('Loyalty point')
    date_order = fields.Datetime('Date order')
    name = fields.Char('Order code')




