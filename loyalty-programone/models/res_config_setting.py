from odoo import fields, models, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Extend res config setting'

    fk_program = fields.Many2one('program.sale', string="Chương trình khuyến mãi")
