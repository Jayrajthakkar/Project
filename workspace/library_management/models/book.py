from odoo import models, fields, api
from random import randint
class Book(models.Model):
	_name = 'library.book'
	_description = 'This model stores the data about the Book information'
	_inherit=['mail.thread','mail.activity.mixin']
	_rec_name = 'book_name'


	def _default_random(self):
		return randint(10**(8-1),(10**8)-1)


	book_name = fields.Char(string='Name')
	author = fields.Char(string='Author')
	photo = fields.Image(string='Cover Photo')
	state = fields.Selection([("good condition","Good Condition"),("scrapped","Scrapped")],default='good condition',string='State',tracking=True)
	sale_history_ids = fields.One2many(string='Sales',comodel_name='sale.history.book',inverse_name='book_id')
	total = fields.Integer(string='total',compute='_compute_total')
	isbn = fields.Integer(string='ISBN',default=_default_random)
	rate = fields.Selection([("star","star"),("low","Low"),("med","Med"),("high","High")],string='Rate')
	status = fields.Selection([("Available","Available"),("Unavailable","Unavailable")])

	# @api.model
	# def create(self,vals):
	# 	vals['isbn'] = randint(10**(8-1),(10**8)-1)
	# 	res = super(Book,self).create(vals)
	# 	return res 


	def _compute_total(self):
		for rec in self:
			sum_1 = 0

			for result in rec.sale_history_ids:
				sum_1 = result.subtotal + sum_1
		self.total = sum_1

	

	
	def change_state(self):
		for rec in self:
			if rec.state == 'good condition':
				rec.state = 'scrapped'
	



	def action_view_salescount(self):
		print('click --------------')

class SalseHistory(models.Model):
	_name='sale.history.book'
	_description = "his model stores the data about the sales information"
	

	book_id = fields.Many2one(comodel_name='library.book',string='Book')
	visitor_id = fields.Many2one(comodel_name='visitor.visitor',string='Visitor')
	quantity = fields.Integer(string='Quantity')
	price = fields.Float(string='Price')
	subtotal=fields.Integer(compute='_compute_total',string='total')


	@api.depends('quantity','price')
	def _compute_total(self):
		for rec in self:
			rec.subtotal=rec.quantity*rec.price


