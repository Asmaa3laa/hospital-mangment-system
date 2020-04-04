from odoo import models, fields, api
from odoo.exceptions import UserError


class InheritCustomer(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one(comodel="hms.patient")
    vat = fields.Char(required=True)

    # related_patient_id = fields.Char()
    @api.model
    def create(self, vals):
        email = vals["email"]
        result = self.env["hms.patient"].search([("email", "=", email)])
        print("*************")
        print(result.email)
        if result.email==False:
            new_record =super().create(vals)
        else:
            raise UserError("this email is already exist")
        return new_record

    @api.multi
    def unlink(self):

        if not self.related_patient_id:
            raise UserError("you can't delete that customer")
        else:
            super().unlink(self)

