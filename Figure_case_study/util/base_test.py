# Atharv Kolhar
"""
Base library for test cases
"""
import sys

import pytest
import logging
from util.imu_comm import IMUComm
from util.table_control import TableController

import yaml


class BaseTest:

    logger = logging.getLogger("test_logger")
    format = "%(asctime)s|%(name)s|%(levelname)s|%(message)s"
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=format)
    
    # Test Config data
    with open("/Users/atharvkolhar/figure/Figure_case_study/test_config.yaml", 'r') as config:
        config_data = yaml.safe_load(config)
        
    table_ip = config_data['table_ip']
    imu_app_ip = config_data['imu_app_ip']
    roll_err = 0
    pitch_err = 0

    def __init__(self):
        # Initializing the tabel control and imu communicaation
        self.tabel_ctrl = TableController(self.table_ip)
        self.imu_comm = IMUComm(self.imu_app_ip)

    def setup_class(self):
        # Setting the Motion Table to Zero degree roll and pitch
        self.tabel_ctrl.roll_table(0)
        self.tabel_ctrl.pitch_table(0)

        # Getting the roll error and pitch error for the imu when table is flat
        self.roll_err = self.imu_comm.get_roll_angle()[-1]
        self.pitch_err = self.imu_comm.get_pitch_angle()[-1]

    def teardown_class(self):
        self.table_ctrl.disconnect()
