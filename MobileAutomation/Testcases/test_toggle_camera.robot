*** Settings ***
Resource     ${EXEC_DIR}/Keywords/toggleCameraKeywords.robot

*** Variables ***
${iter}    100

*** Test Cases ***
toggle: It verifies the Toggling of Camera
    [Tags]    Toggle
    VERIFY LAUNCH CAMERA APP
    getDeviceInstance
    Start LOGCAT
    CAMERATOGGLE    ${iter}
    ${res}    GETLOG
    VERIFY FRONT IMAGE CAPTURE     ${iter}    ${res}
    VERIFY BACK IMAGE CAPTURE    ${iter}    ${res}
    
