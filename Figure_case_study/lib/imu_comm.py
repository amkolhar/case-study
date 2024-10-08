# Atharv Kolhar
"""
Library to communicate with the IMU App
"""
from case_study.lib.base_test import BaseTest
import serial
import time


class IMUComm(BaseTest):

    def get_roll_angle(self, poll_time: int = 1) -> list:
        """
        Function to query list of roll angle from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        pass

    def get_pitch_angle(self, poll_time: int = 1) -> list:
        """
        Function to query list of pitch angle from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        pass

    def get_acceleration(self, poll_time: int = 1) -> list:
        """
        Function to query list of acceleration from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        pass

    def get_angular_rate(self, poll_time: int = 1) -> list:
        """
        Function to query list of angular rate from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        pass

    def get_serial_message(self, time_out: int = 40):
        """
        Function to capture RS-422 serial message
        :param time_out:
        :return:
        """

        ser = serial.Serial(
            port='COM1',  # or '/dev/ttyS1' on Linux
            baudrate=9600,  # RS422 typically uses various baud rates
            bytesize=serial.EIGHTBITS,  # or serial.SEVENBITS
            parity=serial.PARITY_NONE,  # or serial.PARITY_ODD, serial.PARITY_EVEN
            stopbits=serial.STOPBITS_ONE,  # or serial.STOPBITS_TWO
            timeout=1  # in seconds, can be adjusted or set to None for blocking mode
        )
        start_time = time.time()
        time_elapse = 0
        try:
            while time_elapse < time_out:
                if ser.in_waiting > 0:  # Check if data is available
                    data = ser.read(ser.in_waiting)  # Read the available data
                    with open("data_file.bin", "a") as data_file:
                        data_file.write(data)
                time_elapse = time.time() - start_time
        finally:
            ser.close()

    def get_app_latency(self) -> int:
        """
        Function to get the imu app latency in milliseconds
        :return:
        """
        latency = 0 # implement a function to capture latency
        return latency

    def evaluate_error_message(self) -> int:
        self.get_serial_message(time_out=40)

        # evaluate the message and return error message count

        return self.error_message_count

    def get_total_message(self) -> int:
        # evaluate total message count in recorded data
        return self.total_message_count


