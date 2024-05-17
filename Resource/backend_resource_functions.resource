*** Settings ***
Library     ../Resource/Payloads.py
Library     ../Resource/Custom_functions.py
Library     RequestsLibrary
Library     DatabaseLibrary
Library    ExcelLibrary
Library    JSONLibrary
Library    Collections
Library    BuiltIn

*** Keywords ***

Change_wifi_settings
    [Arguments]     ${camera_custom_id}        ${ssid}      ${wifi_password}

#    ${variable_type}    Evaluate    type($camera_custom_id).__name__
#    Log    ${variable_type}
    Log        ${camera_custom_id}
    Sleep    5
    ${camera_account_id}    get camera account id        ${camera_custom_id}
    ${get_wifi_settings_body}         get wifi settings body        ${camera_custom_id}     ${camera_account_id}    ${ssid}     ${wifi_password}
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_wifi_settings_body}    expected_status=200   headers=${onecam_headers}


Get onecam headers

    Log To Console          ${onecam_headers}

Restart_camera
    [Arguments]     ${camera_custom_id}

    ${camera_account_id}    get camera account id        ${camera_custom_id}
    ${get_camera_restart_body}         get camera restart body        ${camera_custom_id}     ${camera_account_id}
    ${onecam_headers}         get onecam headers
    POST        https://api.qa.56secure.com/rpc/v1/raven/send_message    json=${get_camera_restart_body}    expected_status=200   headers=${onecam_headers}


bind from app
    Log To Console    app calling bind api...
    ${onecam_headers}        get headers
    ${bind_payload}         get camera bind payload
    ${return_values}=     call bind api and fetch reg key
    Log     printing values received from cloud
    Log    ${return_values}
    Return From Keyword     ${return_values}

bind from camera
    [Arguments]    ${reg_key}
    Log To Console    binding from camera...
    ${cloud_id}      init from camera    ${reg_key}
    Sleep      3
    bind complete from camera       ${reg_key}      ${cloud_id}

start polling
    [Arguments]    ${binding_id}
    Log To Console  started polling...
    ${onecam_headers}        get headers


    FOR    ${i}    IN RANGE     1       8

        ${response}=     GET        https://api.qa.56secure.com/vision/v1/camera/onecam/bind/${binding_id}      expected_status=200   headers=${onecam_headers}
        ${polling_result}       Set Variable        ${response.json()}[data][status]

        IF    '${polling_result}'=='success'
            Exit For Loop
        END

        IF    '${polling_result}'=='failure'
            Exit For Loop
        END

        Sleep    15

    END

    Log To Console      ${polling_result}

bind complete from camera
    [Arguments]    ${reg_key}       ${cloud_id}
    Log To Console    making bind completion from camera...
    ${headers}    Get Headers
    &{payload}      Create Dictionary           registration_key=${reg_key}     tutk_cred=abcd
    Set To Dictionary       ${headers}      Authorization       ${cloud_id}
    Set To Dictionary       ${headers}      X-Device-Id       56AI010100000001

    ${response}=     POST          https://api.qa.56secure.com/vision/v1/onecam/camera/completion     expected_status=200   headers=${headers}   json=${payload}


verify ai packs
    Log To Console  verifying ai packs...
    ${ai_packs_values}     fetch ai packs values       56AI010100000015
    Should Be Equal As Strings    ${ai_packs_values}[intrusion_pack]        enabled
    Should Be Equal As Strings    ${ai_packs_values}[pms_pack]        inactive
    Should Be Equal As Strings    ${ai_packs_values}[ams_pack]        inactive
    Should Be Equal As Strings    ${ai_packs_values}[ukms_pack]        inactive

pass bind info to camera
    [Arguments]     ${data_to_pass_in_sock_connection}         ${wifi_details}
    establish socket connection     ${data_to_pass_in_sock_connection}    ${wifi_details}