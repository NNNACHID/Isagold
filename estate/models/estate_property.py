# -*- coding: utf-8 -*-

from email.policy import default
import string
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate property'
    
    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    postcode = fields.Char()
    state = fields.Selection(
        [('new', 'New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        default='new',
        copy=False,
        required=True
    )
    active = fields.Boolean('Active', default=True)
    date_availability = fields.Date('Available from',default=(fields.Date.today() + relativedelta(months=+3)),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson = fields.Many2one('res.users', string='Salesman', index=True, tracking=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', copy=False, index=True, tracking=True)
    tag_ids = fields.Many2many("estate.property.tag", string="Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total")
    best_price = fields.Char(compute="_compute_best_price")

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids.price > 0:
                record.best_price = max(record.offer_ids.mapped('price'))
            else: 
                record.best_price = 0.00
