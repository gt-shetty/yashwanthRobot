import json
import requests
import pymongo

from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Bodies:

    @keyword
    def get_device_info_body(self):
        payload = {
            "camera_device_id": "56AI010100000017",
            "event_name": "MESSAGE/64b9297fc35b1d648623bd3a",
            "data": "{\"event\": \"GET_DEVICE_INFO\", \"udid\": \"56AI010100000017\",\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\" }"
        }

    @keyword
    def get_wifi_settings_body(self):
        payload = {
            "camera_device_id": "56AI010100000017",
            "event_name": "MESSAGE/64b9297fc35b1d648623bd3a",
            "data": "{\"event\": \"WIFI_NETWORK_CONFIG\", \"udid\": \"56AI010100000018\",\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\", \"state\": \"ENABLE\",\"ssid\": \"56Secure J\",\"password\":  \"56Secure@123$\",\"security\": \"WPA2\"}"
        }
        return payload

    @keyword
    def get_onecam_headers(self):
        temp = {
                  'X-Device-Id': 'postman',
                  'X-Platform': 'android',
                  'X-Version': '10.0.0',
                  'Content-Type': 'application/json'
                }


        return temp

    @keyword
    def test_mongodb(self):
        mongo_client = pymongo.MongoClient("mongodb+srv://write:aZIMmWzMOa8VMDNl@staging.9f7yz.mongodb.net/?authSource=admin")
        db = mongo_client.vision_qa
        collection = db.camera_account
        document = collection.find_one({"camera_custom_id":"56AI010100000015", "status":"active"})
        if document:
            print(document)
        else:
            print("Document not found")
