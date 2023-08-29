from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Bodies:

    @keyword
    def get_device_info_body(self):
        temp = {
                    "camera_device_id": "56AI010100000017",
                    "event_name": "MESSAGE/64b9297fc35b1d648623bd3a",
                    "data": "{\"event\": \"GET_DEVICE_INFO\", \"udid\": \"56AI010100000017\",\"timestamp\": \"1682077731\", \"id\": \"63ce55886b9ce300f9831f6b\", \"request_id\":\"87e5d0e7-6e10-4f27-877a-1b9d1a19dd2d\" }"
                }


        return temp

    @keyword
    def get_onecam_headers(self):



        return temp