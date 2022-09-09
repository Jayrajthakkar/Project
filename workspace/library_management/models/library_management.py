from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryManagement(models.Model):
	_name = 'library.management'
	_description = 'This is master table to store the Libraries'

	name = fields.Char(string='Name')
	property_type = fields.Selection([("public","Public"),("private","Private")],string='Type')
	librarians_ids = fields.Many2many(comodel_name = 'librarian.librarian',string='Librarians')




	@api.constrains('librarians_ids.current_experience')
	def _check_experience(self):
		for librarians_rec in self:
			if librarians_rec.librarians_ids.current_experience < 2:
				raise ValidationError('Your Exprience Should Be Gratter Than Two')