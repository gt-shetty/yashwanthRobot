import json
import requests
import pymongo
import time

from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Payloads:
    def __init__(self):
        self.secure_headers = {}
        self.mongo_client = pymongo.MongoClient(
            "mongodb+srv://write:aZIMmWzMOa8VMDNl@staging.9f7yz.mongodb.net/?authSource=admin")




    @keyword
    def get_device_info_body(self):

        payload = {
            "camera_device_id": "56AI010100000015",
            "event_name": "MESSAGE/6528f82903c4b8f0d296d1ea",
            "data": "{\"event\": \"GET_DEVICE_INFO\", \"udid\": \"56AI010100000015\",\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\"}"
        }

        return payload

    @keyword
    def get_wifi_settings_body(self, camera_custom_id, camera_account_id, ssid, wifi_password):
        print("hiiiiiii")
        event_json = {
            "event": "WIFI_NETWORK_CONFIG",
            "udid": camera_custom_id,
            "timestamp" : "1682077731",
            "id": "63ce55886b9ce300f9831f6b",
            "request_id" : "87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d",
            "state" : "ENABLE",
            "ssid" : ssid,
            "password" : wifi_password,
            "security" : "WPA2"
        }


        stringified_payload = json.dumps(event_json)
        print(stringified_payload)

        payload = {
            "camera_device_id": camera_custom_id,
            "event_name": "MESSAGE/"+camera_account_id,
            "data": stringified_payload
            #"data": "{\"event\": \"WIFI_NETWORK_CONFIG\", \"udid\": {},\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\", \"state\": \"ENABLE\",\"ssid\": {},\"password\":  {},\"security\": \"WPA2\"}".format(camera_custom_id, ssid, wifi_password)
        }
        return payload


    @keyword
    def get_camera_restart_body(self, camera_custom_id, camera_account_id):
        print("hiiiiiii")
        event_json = {
            "event": "DEVICE_RESTART",
            "udid": camera_custom_id,
            "timestamp" : "1682077731",
            "id": "63ce55886b9ce300f9831f6b",
            "request_id" : "87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d"
        }


        stringified_payload = json.dumps(event_json)
        print(stringified_payload)

        payload = {
            "camera_device_id": camera_custom_id,
            "event_name": "MESSAGE/"+camera_account_id,
            "data": stringified_payload
            #"data": "{\"event\": \"WIFI_NETWORK_CONFIG\", \"udid\": {},\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\", \"state\": \"ENABLE\",\"ssid\": {},\"password\":  {},\"security\": \"WPA2\"}".format(camera_custom_id, ssid, wifi_password)
        }
        return payload




    @keyword
    def get_headers(self):

        # FETCHING AUTH TOKEN
        temp_headers = {
            "Content-Type": "application/json"
        }
        temp_payload = {
                "id": "650c2f3ca9312bd2d2264403",
                "device_id": "1234",
                "platform": "android",
                "role": "consumer",
                "app_version": "10.0.0"
            }

        url = "https://api.qa.56secure.com/rpc/v1/bifrost/create_access_token"
        response = requests.post(url, headers=temp_headers, data=json.dumps(temp_payload))
        print(type(response))
        temp_json = json.loads(response.text)
        auth_token = temp_json['access_token']
        temp_time = str(int(time.time()))

        # FORMING HEADERS
        self.secure_headers = {
                  'Authorization': auth_token,
                  'X-Device-Id': '1234',
                  'X-Platform': 'android',
                  'X-Version': '10.0.0',
                  'Content-Type': 'application/json',
                  'X-Client-Time': temp_time
                }

        return self.secure_headers


    @keyword
    def get_camera_bind_payload(self):
        temp = {
                 "is_apartment_camera": False
                }


        return temp

    @keyword
    def test_mongodb(self):
        db = self.mongo_client.vision_qa
        collection = db.camera_account
        document = collection.find_one({"camera_custom_id":"56AI010100000015", "status":"active"})
        if document:
            print(document)
        else:
            print("Document not found")

    @keyword
    def get_camera_account_id(self, camera_custom_id):
        db = self.mongo_client.vision_qa
        collection = db.camera_account
        fields_to_retrieve = {"_id": 1, "tag": 1}
        document = collection.find_one({"camera_custom_id": camera_custom_id, "status": "active"}, fields_to_retrieve)
        camera_account_id = document['_id']
        stringified_camera_account_id = str(camera_account_id)
        if document:
            print(stringified_camera_account_id)
            return stringified_camera_account_id
        else:
            print("Document not found")

            #2268902100


    @keyword
    def call_bind_api_and_fetch_reg_key(self):

        url = "https://api.qa.56secure.com/vision/v1/camera/onecam/bind"
        temp_payload = {
                "is_apartment_camera": False
            }

        response = requests.post(url, headers=self.secure_headers, data=json.dumps(temp_payload))
        temp_json = json.loads(response.text)
        print(temp_json)
        reg_key = str(temp_json['data']['registration_key'])
        binding_id = str(temp_json['data']['id'])
        return_dict = { }
        return_dict['reg_key'] = reg_key
        return_dict['binding_id'] = binding_id
        print(return_dict)
        return return_dict

    @keyword
    def init_from_camera(self, reg_key):
        print("Hiiii")
        url = "https://api.qa.56secure.com/vision/v1/onecam/camera/initialisation"
        temp_payload = {
               "registration_key": reg_key,
               "udid": "56AI010100000015",
               "tutk_udid": "2B28NITTGS6RG3W6IXQTF3RURQVJRQXTGPMSEBK3ZB2QRVNA3ZKSOUQ3QRLABWIF7GAUNV5SIUWWWER3JFDCP2RK5ATY7I6XTCHVAAAUTO",
               "camera_ip": "192.168.51.800",
               "poe_mac_address": "98:ae:71:01:9c:9e",
               "wifi_mac_address": "34:7d:e4:7e:9d:6c",
               "location": None
        }

        response = requests.post(url, headers=self.secure_headers, data=json.dumps(temp_payload))
        temp_json = json.loads(response.text)
        print(temp_json)
        cloud_id = temp_json['data']['cloud_id']
        print("Hiiiieeeee")
        return  cloud_id

    @keyword
    def fetch_ai_packs_values(self, camera_custom_id):
        print("Im at mongo db function")
        db = self.mongo_client.vision_qa
        collection = db.camera_account
        print("Im hereee")
        #fields_to_retrieve = {"ai_pack.intrusion.state": 1, "ai_pack.pms.state": 1, "ai_pack.ams.state": 1, "ai_pack.ukms.state": 1}
        fields_to_retrieve = {"ai_pack": 1}
        document = collection.find_one({"camera_custom_id": camera_custom_id, "status": "active"}, fields_to_retrieve)
        print(type(document))
        print(document)
        ai_packs = {'intrusion_pack': document['ai_pack']['intrusion']['state'], 'pms_pack': document['ai_pack']['pms']['state'],
                    'ams_pack': document['ai_pack']['ams']['state'], 'ukms_pack': document['ai_pack']['ukms']['state']}

        return  ai_packs