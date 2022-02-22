from odoo import models, fields, api
from datetime import datetime

class LogHistory(models.Model):

    _name = "log.history"

    date = fields.Datetime(
        string=' Date', default= lambda *a: datetime.now() )
    description = fields.Char()
    patient_id = fields.Many2one("hms.patient")
    created_by = fields.Many2one(related="patient_id.doctor_id")
    new_state = fields.Selection(related="patient_id.state")


    @api.model
    def create(self, vals):
        changed = super().create(vals)
        changed.description = changed.new_state

        return changed




