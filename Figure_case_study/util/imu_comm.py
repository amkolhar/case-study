# Atharv Kolhar
"""
Library to communicate with the IMU App
"""

import socket
import time


class IMUComm:
    def receive_imu_app_data(poll_time):
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
