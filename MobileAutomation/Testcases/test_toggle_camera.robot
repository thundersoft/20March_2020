*** Settings ***
Resource     ../Keywords/toggleCameraKeywords.robot
Library    ../Lib/uiAutomatorLib.py

*** Variables ***
${iter}    100

*** Test Cases ***
toggle: It verifies the Toggling of Camera
    [Tags]    Toggle
    VERIFY LAUNCH CAMERA APP
    getDeviceInstance    ${TEST_DEVICE_ID}
    Start LOGCAT
    CAMERATOGGLE    ${iter}
    ${res}    GETLOG
    VERIFY FRONT IMAGE CAPTURE     ${iter}    ${res}
    VERIFY BACK IMAGE CAPTURE    ${iter}    ${res}
    
