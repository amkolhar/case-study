# Atharv Kolhar
import sysv_ipc
import socket
import argparse


class IMUDataSender:
    
    def __init__(self, reciver_ip):
        # Shared memory key where data is stored
        self.shared_mem_key = 2468
        self.receiver_ip = reciver_ip

        # Create a socket object
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attach to shared memory
        self.imu_shared_memory = sysv_ipc.SharedMemory(self.shared_mem_key)

    def stream_imu_data(self):
        """
        Stream IMU data over socket
        """
        # Connect to the receiver
        server_address = (self.receiver_ip, 7000) 
        self.sock.connect(server_address)
        
        while True:
            # Read the data from shared memory
            data = self.imu_shared_memory.read()
            
            if not data:
                # breeak the while loop if no data available in shared memory
                break
                
            # Send the shared memory data over the socket
            self.sock.sendall(data)
        
        # Close the socket connection
        self.sock.close()

        # Detach from the shared memory segment
        self.imu_shared_memory.detach()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Arguement to start the IMU data streaming on Socket 7000")

    # Add arguments
    parser.add_argument('--reciever_ip', type=str, required=True, help="Receiver ip address")

    # Parse the arguments
    args = parser.parse_args()
    
    imu_data_sender = IMUDataSender(args.receiver_ip)
    
    imu_data_sender.stream_imu_data()
