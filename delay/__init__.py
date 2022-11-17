# -*- coding: utf-8 -*-

from . import models

import logging
from time import sleep

_logger = logging.getLogger(__name__)


def sleep_patch():
    _logger.info("Start sleep")
    sleep(65)
    _logger.info("End sleep")