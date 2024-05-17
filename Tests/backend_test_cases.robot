*** Settings ***
Library     RequestsLibrary
Library     DatabaseLibrary
Library     ../Resource/Payloads.py
Library     ../Resource/Custom_functions.py
Resource     ../Resource/backend_resource_functions.resource
Library    ExcelLibrary
Library    JSONLibrary
Library    Collections
#Library    DataDriver       file=/Users/yashwanthgt/Downloads/practice_csv.csv       encoding=utf_8      dialect=unix
#Test Template    Change_wifi_settings


*** Variables ***
${onecam_headers}
${bind_payload}


*** Test Cases ***

Camera_bind
    &{wifi_details}      Create Dictionary      ssid=YashwanthGT        password=sunflower00$       security=WPA2
    ${return_results}     bind from app
    ${reg_key}    Set Variable           ${return_results['data']['registration_key']}
    ${binding_id}    Set Variable        ${return_results['data']['id']}
    pass bind info to camera        ${return_results}      ${wifi_details}
    #bind from camera     ${reg_key}
    start polling       ${binding_id}
    verify ai packs

Simple_test
    Change Wifi Connection
    #pass bind info to camera



Change wifii settings ${camera_custom_id} ${ssid} ${wifi_password}

Restart camera ${camera_custom_id}
       [Template]       Restart_camera


Get device info
    ${get_device_info_body}         get device info body

    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_device_info_body}    expected_status=200   headers=${onecam_headers}








