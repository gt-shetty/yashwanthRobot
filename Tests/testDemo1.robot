*** Settings ***
Library     RequestsLibrary
Library      ../Resources/Bodies.py
Library ../Resources/Bodies.py

*** Variables ***


*** Test Cases ***

Get device info
    reverse a string
    ${get_device_info_body}         get device info body
    ${onecam_headers}         get_onecam_headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json= ${get_device_info_body}      expected_status=200   headers=${onecam_headers}
    sleep   5

# comment by smw
