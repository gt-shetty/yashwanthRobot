*** Settings ***
Library     RequestsLibrary
Library     DatabaseLibrary
Library     ../Resource/Payloads.py
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
    ${return_results}     bind from app
    ${reg_key}=    Set Variable           ${return_results}[0]
    ${binding_id}=    Set Variable        ${return_results}[1]

    bind from camera     ${reg_key}
    start polling       ${binding_id}
    verify ai packs




Change wifii settings ${camera_custom_id} ${ssid} ${wifi_password}

Restart camera ${camera_custom_id}
       [Template]       Restart_camera


Get device info
    ${get_device_info_body}         get device info body

    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_device_info_body}    expected_status=200   headers=${onecam_headers}








