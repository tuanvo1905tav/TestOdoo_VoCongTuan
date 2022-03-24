from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer extend res.partner'

    loyalty_point = fields.Float('Loyalty points')
    fk_loyalty_level = fields.Many2one('partner.levels', string='Loyalty level')

    @api.onchange('fk_loyalty_level')
    def _onchange_level(self):
        self.loyalty_point = self.fk_loyalty_level.loyalty_points
