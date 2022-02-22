from odoo import models, fields, api

class HmsDepartment(models.Model):
  _name = "hms.department"
  name = fields.Char()
  capacity = fields.Integer(string="capacity", default= 0)
  is_opened = fields.Boolean()
  patient_id = fields.One2many("hms.patient","department_id")







