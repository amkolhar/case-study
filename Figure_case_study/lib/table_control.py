# Atharv Kolhar
"""
Library to control the motion table
"""


class TableController:
    def __init__(self, ip):
        self.ip = ip
        self.table_connected = self.connect(self.ip)

    def connect(self, ip: str) -> bool:
        """
        Function to build the connection with the motion table
        :param ip: str
        :return: bool
        """
        # Actions to connect the table using IP address
        connected = True
        return connected

    def disconnect(self):
        """
        Function to disconnect the motion table
        :return:
        """
        pass

    def roll_table(self, roll_angle: float) -> float:
        """
        Function to roll the table at certain angle
        :param roll_angle: float
        :return: float
        """
        pass

    def pitch_table(self, pitch_angle: float) -> float:
        """

        :param pitch_angle: float
        :return: float
        """
        pass
