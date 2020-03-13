# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Lead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead"]

    @api.multi
    def write(self, vals):
        res = super(Lead, self).write(vals)

        today = fields.Date.context_today(self)
        datetime_today = fields.Datetime.from_string(today)
        self.date_open = fields.Datetime.to_string(datetime_today + relativedelta(days=+1))

        return res