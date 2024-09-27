# Atharv Kolhar
"""
Library to communicate with the IMU App
"""


class IMUComm:
    def __init__(self):
        pass

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
