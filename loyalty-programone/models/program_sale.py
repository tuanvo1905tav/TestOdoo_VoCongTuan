from odoo import fields, models, api


class ProgramSale(models.Model):
    _name = 'program.sale'
    _description = 'Program'

    name = fields.Char('Name', required=True)
    points = fields.Float('% Point', required=True)
    active = fields.Boolean('Active', required=True)
