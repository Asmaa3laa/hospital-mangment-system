from odoo import models, fields


class HmsDepartment(models.Model):
    _name = 'hms.department'

    name = fields.Char()
    capacity = fields.Integer()
    is_open = fields.Boolean()
    # patient_id = fields.One2many(comodel_name="hms.patient", inverse_name="department_id")
    # patient_id is carrying an object from patient model
    doctors_ids = fields.Many2many(comodel_name="hms.doctor")
