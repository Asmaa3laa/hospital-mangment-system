from odoo import models, fields, api
import re
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError


class HmsPatient(models.Model):
    _name = 'hms.patient'
    _rec_name = "firstName"

    firstName = fields.Char(required="True")
    lastName = fields.Char(required="True")
    birthDate = fields.Date()
    history = fields.Html()
    crRatio = fields.Float()
    bloodType = fields.Selection(
        [
            ('A+', 'A+'),
            ('B+', 'B+'),
            ('O+', 'O+'),
            ('AB+', 'AB+'),
            ('A-', 'A-'),
            ('B-', 'B-'),
            ('O-', 'O-'),
            ('AB-', 'AB-')
        ]
    )
    pcr = fields.Boolean(default=False)
    Address = fields.Text()
    Age = fields.Char(compute="compute_age", store=True)
    image = fields.Binary(string='Image')
    department_id = fields.Many2one(comodel_name='hms.department')
    capacity = fields.Integer(related="department_id.capacity")
    patient_histories = fields.One2many(comodel_name="log.history", inverse_name="patient_id")
    state = fields.Selection(related="patient_histories.state")

    email = fields.Char()

    _sql_constraints = [
        ("unique mail", "UNIQUE(email)", "your email is already exist")
    ]

    @api.constrains("email")
    def check_email(self):
        for record in self:
            pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            match = re.match(pattern, record.email)
            if match is None:
                raise UserError("Email isn't correct")

    @api.onchange("Age")
    def onchange_pcr(self):
        if int(self.Age) < 30:
            self.pcr = True
            return {
                # "domain": {'track_id': new_domain},
                "warning": {
                    "title": "pcr is checked",
                    "message": "pcr is mandatory"
                }
             }
        else:
            self.pcr = False

    @api.depends("birthDate")
    @api.multi
    def compute_age(self):
        if self.birthDate:
            d1 = datetime.strptime(str(self.birthDate), "%Y-%m-%d").date()

            d2 = date.today()

            self.Age = relativedelta(d2, d1).years
