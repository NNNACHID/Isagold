# -*- coding: utf-8 -*-

from odoo import api,fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection([('Accepted', 'accepted'), ('Refused', 'refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7, inverse="_inverse_date")
    date_deadline = fields.Date(compute="_compute_date", inverse="_inverse_date")
    
    @api.depends('record.create_date')
    def _compute_date(self):
            for record in self:
                if record.create_date and record.date_deadline != record.create_date + relativedelta(days=+record.validity):
                    record.date_deadline = record.create_date + relativedelta(days=+record.validity)

    def _inverse_date(self):
            for record in self:
                if record.create_date and record.date_deadline != record.create_date + relativedelta(days=+record.validity):
                    record.validity = record.create_date + relativedelta(days=+record.validity)