from odoo import models, fields, api
from datetime import date
class Librarian(models.Model):
	_name = 'librarian.librarian'
	_description = 'This is master Table to store the Librarians'

	name = fields.Char(string='Name')
	gender = fields.Selection([("male","Male"),("female","Female")],string='Gender')
	dob = fields.Date(string='DOB')
	age = fields.Integer(compute='_compute_age',string='AGE')
	date_of_joining = fields.Date(string='Date of Joining') 
	current_experience = fields.Float(string="Current Experience", compute='_compute_experience')


	@api.depends('dob')
	def _compute_age(self):
		for rec in self:
			rec.age = 0
			if rec.dob:
				birthDate = rec.dob
				today = date.today()
				age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
				rec.age = age
	
	@api.depends('date_of_joining')
	def _compute_experience(self):
		for rec in self:
			rec.current_experience = 0
			if rec.date_of_joining:
				join_date = rec.date_of_joining
				today = date.today()
				experience = today.year - join_date.year -((today.month, today.day) < (join_date.month, join_date.day))
				
				rec.current_experience = experience