from odoo import fields, models, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Extend res config setting'

    loyalty_for_sale_id = fields.Boolean('Loyalty for sale id', default=False)
