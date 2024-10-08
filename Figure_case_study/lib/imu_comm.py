# Atharv Kolhar
"""
Library to communicate with the IMU App
"""
from case_study.lib.base_test import BaseTest
import serial
import time
import socket
import pytest


class IMUComm(BaseTest):

    def setup_class(self):


    def receive_imu_app_data(self,poll_time):
        output_data = []
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to an address and port
        server_address = ('0.0.0.0', 7000)  # Listen on all interfaces, port 5000
        server_socket.bind(server_address)
        # Listen for incoming connections
        server_socket.listen()
        collection_time = 0
        start_time = time.time()
        while collection_time < poll_time:
            # Wait for a connection
            print("Waiting for a connection...")
            connection, client_address = server_socket.accept()
            try:
                print(f"Connection established with {client_address}")
                # Receive the data from the client
                while True:
                    data = connection.recv(1024)  # Buffer size of 1024 bytes
                    if data:
                        output_data.append(data.decode('utf-8'))
                        print(f"Received: {data.decode('utf-8')}")
                        collection_time = time.time() - start_time
                    else:
                        print(f"Connection closed by {client_address}")
                        break
            finally:
                # Close the connection after handling the client
                connection.close()

            return output_data

    def get_roll_angle(self, poll_time: int = 1) -> list:
        """
        Function to query list of roll angle from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        output_data=self.receive_imu_app_data(poll_time)
        return output_data['roll_angle']

    def get_pitch_angle(self, poll_time: int = 1) -> list:
        """
        Function to query list of pitch angle from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        output_data=self.receive_imu_app_data(poll_time)
        return output_data['pitch_angle']

    def get_acceleration(self, poll_time: int = 1) -> list:
        """
        Function to query list of acceleration from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        output_data=self.receive_imu_app_data(poll_time)
        return output_data['acceleration']

    def get_angular_rate(self, poll_time: int = 1) -> list:
        """
        Function to query list of angular rate from IMU App
        :param poll_time: int in millisecond
        :return: list
        """
        output_data=self.receive_imu_app_data(poll_time)
        return output_data['angular_rate']

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

    def get_app_latency(self) -> float:
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


