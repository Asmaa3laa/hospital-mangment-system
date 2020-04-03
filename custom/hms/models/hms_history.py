from odoo import models, fields, api


class LogHistory(models.Model):
    _name = "log.history"
    _rec_name = "state"
    description = fields.Char()
    patient_id = fields.Many2one(comodel_name="hms.patient")
    state = fields.Selection(
        [
            ('undetermined', 'Undetermined'),
            ('good', 'Good'),
            ('fair', 'Fair'),
            ('serious', 'Serious')
        ], default="undetermined"
    )

    def change_state(self):

        if self.state == "undetermined":
            self.state = "good"
            self.description = "state has been changed to good"
        elif self.state == "good":
            self.state = "fair"
            self.description = "state has been changed to fair"
        elif self.state == "fair":
            self.state = "serious"
            self.description = "state has been changed to serious"
        else:
            self.state = "good"
            self.description = "state has been changed to good"





