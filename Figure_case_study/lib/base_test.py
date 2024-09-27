# Atharv Kolhar
"""
Base library for test cases
"""
import sys

import pytest
import logging
from lib.imu_comm import IMUComm
from lib.table_control import TableController


class BaseTest:

    logger = logging.getLogger("test_logger")
    format = "%(asctime)s|%(name)s|%(levelname)s|%(message)s"
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=format)
    table_ip = "192.168.1.1"
    roll_err = 0
    pitch_err = 0

    def __init__(self):
        self.tabel_ctrl = TableController(self.table_ip)
        self.imu_comm = IMUComm()

    def setup_class(self):
        # Setting the Motion Table to Zero degree roll and pitch
        self.tabel_ctrl.roll_table(0)
        self.tabel_ctrl.pitch_table(0)

        # Getting the roll error and pitch error for the imu when table is flat
        self.roll_err = self.imu_comm.get_roll_angle()[-1]
        self.pitch_err = self.imu_comm.get_pitch_angle()[-1]

    def teardown_class(self):
        self.table_ctrl.disconnect()
