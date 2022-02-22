from odoo import models, fields

class HmsDoctor(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()

    image = fields.Binary()

    patient_id = fields.One2many("hms.patient","doctor_id")

