# Atharv Kolhar
"""
Testsuite to validate the requirements for the IMU App
"""
import pytest
from pytest import approx

from case_study.lib.imu_comm import IMUComm


class TestIMUApp(IMUComm):

    def setup_class(self):
        # Setting the Motion Table to Zero degree roll and pitch
        self.table_ctrl.roll_table(0)
        self.table_ctrl.pitch_table(0)
        # Getting the roll error and pitch error for the imu when table is flat
        self.roll_err = self.get_roll_angle()[-1]
        self.pitch_err = self.get_pitch_angle()[-1]

    # Testcase : 001.1
    @pytest.mark.parametrize("req_roll_angle", [-40, -30, -20, -10, 10, 20, 30, 40])
    def test_imu_roll_angle(self, req_roll_angle):
        threshold = 0.1

        roll_angle_set = self.tabel_ctrl.roll_table(req_roll_angle)

        resp_roll_angle = self.get_roll_angle(100)[-1]

        assert resp_roll_angle-self.roll_err == approx(roll_angle_set, abs=threshold), f"When Roll angle set to {roll_angle_set}, IMU reported {resp_roll_angle} which is not within the 0.1 degree threshold"

    # Testcase : 001.2
    @pytest.mark.parametrize("req_pitch_angle", [-40, -30, -20, -10, 10, 20, 30, 40])
    def test_imu_pitch_angle(self, req_pitch_angle):
        threshold = 0.1

        pitch_angle_set = self.tabel_ctrl.roll_table(req_pitch_angle)

        resp_pitch_angle = self.get_pitch_angle(100)[-1]

        assert resp_pitch_angle-self.pitch_err == approx(pitch_angle_set, abs=threshold), f"When Roll angle set to {pitch_angle_set}, IMU reported {resp_pitch_angle} which is not within the 0.1 degree threshold"

    # Testcase : 002.1
    def test_error_code_rate(self):
        error_message_count = self.get_serial_message(40)
        total_message_count = self.get_total_message()
        error_rate = error_message_count/total_message_count
        assert error_rate <= 0.00001, f"Error rate {error_rate} is greater than 1e-5"

    # Testcase 003.1
    def test_imu_app_latency(self):
        # Check the message latency by sending a motion table control request and check the response
        latency = self.get_latency()
        assert latency < 2, f"Latency of imu and imu_app is great than 2 ms, Actual Latency {latency}"



