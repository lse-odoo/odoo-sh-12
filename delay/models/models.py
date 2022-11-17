# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from time import sleep


class delay(models.Model):
    _name = 'delay'
    _description = 'Just add delay to init the model' 

    _auto = False
