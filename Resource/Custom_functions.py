import json
from datetime import datetime

import requests
import time
import socket
import subprocess

from robot.api.deco import library, keyword

@library
class Custom_functions:
    @keyword
    def establish_socket_connection(self, data_to_pass_in_sock_connection, wifi_details):

        #CONNECTING TO CAMERA MAC ADDRESS
        wifi_ssid_string = "\"56Secure34:7d:e4:7e:9c:3c\""
        modified_string = '\\"' + wifi_ssid_string + '\\"'
        command = f"networksetup -setairportnetwork en0 {modified_string}"
        try:
            subprocess.run(command, shell=True, check=True)
            time.sleep(15)
            print("WiFi connection changed successfully!")
            print("confirming wifi successssss")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")




        data_to_pass_in_sock_connection = data_to_pass_in_sock_connection['data']
        data_to_pass_in_sock_connection.pop('id')
        data_to_pass_in_sock_connection['wifi']= wifi_details

        # Define the mapping of old keys to new keys
        key_mapping = {
            "username": "user_name",
            "password": "user_password"
        }

        epoch_time = data_to_pass_in_sock_connection['configs']['timezone_timestamp'] / 1000  # Divide by 1000 to convert milliseconds to seconds
        exponential_format = "{:e}".format(epoch_time)
        data_to_pass_in_sock_connection['configs']['timezone_timestamp'] = exponential_format
        data_to_pass_in_sock_connection['configs']['camera_heartbeat_interval_in_mins'] = 1.0




        # Create a new dictionary with modified key names
        modified_dict = {key_mapping.get(k, k): v for k, v in data_to_pass_in_sock_connection.items()}

        my_string = "\"secure_56\":"

        result = my_string + str(modified_dict)

        print(result)


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.2.1'
        port = 6789
        s.connect((host, port))


        try:
            s.sendall(result.encode())

            # Receive response from the server
            response = s.recv(1024).decode()
            print("Server response:", response)

        finally:
            # Close the socket connection
            s.close()


        #CONNECTING TO INTERNET
        command = f"networksetup -setairportnetwork en0 YashwanthGT"

        try:
            subprocess.run(command, shell=True, check=True)
            time.sleep(25)
            print("WiFi connection changed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")


    @keyword
    def change_wifi_connection(self):
        command = f"networksetup -setairportnetwork en0 56Secure34:7d:e4:7e:9c:3c"

        try:
            subprocess.run(command, shell=True, check=True)
            print("WiFi connection changed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")