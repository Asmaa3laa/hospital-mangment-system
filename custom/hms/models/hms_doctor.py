from odoo import models,fields


class HmsDoctor(models.Model):
    _name = "hms.doctor"

    firstName = fields.Char()
    lastName = fields.Char()
    image = fields.Binary(string='Image')
    departments_ids = fields.Many2many(comodel_name="hms.department")
