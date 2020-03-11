# -*- coding: utf-8 -*-

import logging
import traceback
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class User(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']

    @api.multi
    def write(self, values):
        before_user_perm_set = set(self.groups_id.ids) if self.groups_id else set()

        res = super().write(values)

        after_user_perm_set = set(self.groups_id.ids) if self.groups_id else set()

        if before_user_perm_set != after_user_perm_set:
            intersection = after_user_perm_set & before_user_perm_set
            new_permission = after_user_perm_set - intersection
            removed_permission = before_user_perm_set - intersection

            _logger.info(
                "\n*SUPPORT* User permissions changed.\nModified user: %s\nUID: %s \nNew: %s \nRemoved: %s \nStacktrace:\n %s\n",
                self.name, self.env.user.name, new_permission, removed_permission, ''.join(traceback.format_stack()))

        return res

class Group(models.Model):
    _name = 'res.groups'
    _inherit = ['res.groups']

    @api.multi
    def write(self, values):
        before_users = set(self.groups_id.ids) if self.groups_id else set()

        res = super().write(values)

        after_users_set = set(self.groups_id.ids) if self.groups_id else set()
        if before_users != after_users_set:
            intersection = after_users_set & before_users
            new_permission = after_users_set - intersection
            removed_permission = before_users - intersection

            _logger.info(
                "\n*SUPPORT* Groups permissions changed.\nModified user: %s\nUID: %s \nNew: %s \nRemoved: %s \nStacktrace:\n %s\n",
                self.name, self.env.user.name, new_permission, removed_permission, ''.join(traceback.format_stack()))

        return res