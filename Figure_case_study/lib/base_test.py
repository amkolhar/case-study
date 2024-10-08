# Atharv Kolhar
"""
Base library for test cases
"""
import sys

import logging
from new.table_control import TableController


class BaseTest:
    logger = logging.getLogger("test_logger")
    format = "%(asctime)s|%(name)s|%(levelname)s|%(message)s"
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=format)
    table_ip = "192.168.1.1"
    roll_err = 0
    pitch_err = 0

    def __init__(self):
        self.table_ctrl: TableController
        self.error_message_count = 0
        self.total_message_count = 0

    def setup_class(self):
        self.table_ctrl = TableController(self.table_ip)

    def teardown_class(self):
        self.table_ctrl.disconnect()
