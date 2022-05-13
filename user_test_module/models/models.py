#-*- coding: utf-8 -*-

from odoo import models, fields, api


class user_test_module(models.Model):
    
    _name = 'user_test_module.user_test_module'
    _description = 'user_test_module.user_test_module'

    client_code = fields.Integer(size=10)
    client_name = fields.Char(size=25)
    address = fields.Char(size=25) 
    city = fields.Char(size=25)
    postcode = fields.Integer(size=25)
    country = fields.Text(size=25)

