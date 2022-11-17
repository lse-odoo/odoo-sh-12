# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, tools
from time import sleep

_logger = logging.getLogger(__name__)

class delay(models.Model):
    _name = 'delay'
    _description = 'Just add delay to init the model' 

    _auto = False

    def init(self):
        _logger.info("Start sleep")
        sleep(65)
        _logger.info("End sleep")
        tools.drop_view_if_exists(self.env.cr, 'delay')
        self.env.cr.execute("""create or replace view delay as (SELECT 42)""")