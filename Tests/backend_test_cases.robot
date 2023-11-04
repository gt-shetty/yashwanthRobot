*** Settings ***

Library     RequestsLibrary
Library     DatabaseLibrary
Library     ../Resource/Payloads.py




*** Variables ***

*** Test Cases ***

Get device info

    ${get_device_info_body}         get device info body
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_device_info_body}    expected_status=200   headers=${onecam_headers}


Change_wifi_settings

    test mongodb
    ${get_wifi_settings_body}         get wifi settings body
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_wifi_settings_body}    expected_status=200   headers=${onecam_headers}


