# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead"]

    @api.model
    def create(self, vals):
        partners = self.env["res.partner"].search([])
        nbr_partner = len(partners)
        name = str(vals["name"])
        if name != "":
            n = ord(name[0])
            random_consistent_partner_ind = n % nbr_partner
            vals["partner_id"] = partners[random_consistent_partner_ind].id

        return super().create(vals)
