from odoo import models, fields, api

class HmsPatient(models.Model):
     _name = "hms.patient"
     _rec_name = "first_name"
     first_name = fields.Char()
     last_name = fields.Char()
     birth_date = fields.Date()
     history = fields.Html()
     cr_ratio = fields.Float()
     blood_type = fields.Selection(
          [("O","O"),("O-","O-"),("A","A"),("A+","A+")]

     )
     pcr = fields.Boolean()
     image = fields.Binary()
     age = fields.Integer()
     department_id = fields.Many2one("hms.department")
     capacity_id = fields.Integer(related="department_id.capacity")
     doctor_id = fields.Many2one("hms.doctor")
     log_history_id = fields.One2many("log.history","patient_id")

     state = fields.Selection([
          ("undetermined","Undetermined"),
          ("good","Good"),
          ("fair","Fair"),
          ("serious","Serious")
          ],default="undetermined")

     def state_function(self):

          if self.state == "undetermined":
               self.state = "good"
          elif self.state == "good":
               self.state = "fair"
          elif self.state == "fair":
               self.state = "serious"


     @api.onchange('age')
     def _onchange_did(self):

      if self.age == 30:
          self.pcr = True

      return {

          'warning':{'title':"age changed",
                     'message':"that can change pce value"}

     }






