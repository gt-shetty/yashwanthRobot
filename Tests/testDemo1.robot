*** Settings ***
Library     RequestsLibrary
Library      ../Resources/Bodies.py
Library    DatabaseLibrary



*** Variables ***
${count}   0


*** Test Cases ***

Get device info

    ${get_device_info_body}         get device info body
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_device_info_body}    expected_status=200   headers=${onecam_headers}
    sleep   5
    ${count}  Evaluate     ${count} + 1
    Log To Console     call...${count}



Change_wifi_settings

#    Connect To Database Using Custom Connection String    dbapiModuleName=pymongo    db_connect_string=mongodb+srv://write:aZIMmWzMOa8VMDNl@staging.9f7yz.mongodb.net/?authSource=admin
#
#    ${query} =    Evaluate    {camera_custom_id:"56AI010100000015", status:"active"}    json
#    ${result} =    Run Keyword    Find All Documents    vision_qa.camera_account     ${query}
#    Log    Value from MongoDB: ${result[0]['tag']}

    test mongodb
    ${get_wifi_settings_body}         get wifi settings body
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_wifi_settings_body}    expected_status=200   headers=${onecam_headers}
    sleep   5
    Log To Console     call...${count}
