from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Extend sale order'

    partner_idx = fields.Many2one(comodel_name='res.partner', string='Customer')
    loyalty_name = fields.Many2one(comodel_name='program.sale', string='Program name')
    point_accumulated = fields.Float(related='partner_idx.loyalty_point', string='Points accumulated')
    point_accumulating = fields.Float('Points accumulating')
    point_won = fields.Float('Points won')
    point_used = fields.Float('Points used')
    percent = fields.Float(related='loyalty_name.points')

    fk_loyalty_program = fields.Many2one('program.sale')
    fk_point = fields.Float(related='fk_loyalty_program.points')
    points = fields.Float('Point', compute='_compute_point')


    @api.depends('fk_point')
    def _compute_point(self):
        for rec in self:
            rec.points = rec.fk_point * (rec.amount_untaxed / 100)
            rec.point_won = self.point_accumulated + self.points
    @api.model
    def create(self, values):

        self.env['res.partner'].browse(values.get('partner_id')).write({
            'loyalty_point': values.get('point_won')
        })

        val = {
            'name': values.get('name'),
            'partner_id': values.get('partner_id'),
            'date_order': values.get('date_order'),
            'loyalty_point': values.get('points')
        }
        self.env['loyalty.history'].sudo().create(val)
        result = super(SaleOrder, self).create(values)
        return result
