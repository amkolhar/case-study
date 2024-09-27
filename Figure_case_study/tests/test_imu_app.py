# Atharv Kolhar
"""
Testsuite to validate the requirements for the IMU App
"""
import pytest
from pytest import approx

from lib.base_test import BaseTest


class TestIMUApp(BaseTest):

    # Testcase : 001.1
    @pytest.mark.parametrize("req_roll_angle", [-40,-30,-20,-10,10, 20, 30, 40])
    def test_imu_roll_angle(self, req_roll_angle):
        threshold = 0.1

        roll_angle_set = self.tabel_ctrl.roll_table(req_roll_angle)

        resp_roll_angle = self.imu_comm.get_roll_angle(100)[-1]

        assert resp_roll_angle-self.roll_err == approx(roll_angle_set, abs=threshold), f"When Roll angle set to {roll_angle_set}, IMU reported {resp_roll_angle} which is not within the 0.1 degree threshold"

    # Testcase : 001.2
    @pytest.mark.parametrize("req_pitch_angle", [-40,-30,-20,-10,10, 20, 30, 40])
    def test_imu_roll_angle(self, req_pitch_angle):
        threshold = 0.1

        pitch_angle_set = self.tabel_ctrl.roll_table(req_pitch_angle)

        resp_pitch_angle = self.imu_comm.get_pitch_angle(100)[-1]

        assert resp_pitch_angle-self.pitch_err == approx(pitch_angle_set, abs=threshold), f"When Roll angle set to {pitch_angle_set}, IMU reported {resp_pitch_angle} which is not within the 0.1 degree threshold"
