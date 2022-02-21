# -*- coding: utf-8 -*-

from email.policy import default
from odoo import fields, models
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
