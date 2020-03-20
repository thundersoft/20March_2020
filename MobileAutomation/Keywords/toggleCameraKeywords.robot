*** Settings ***
Library     ${EXEC_DIR}/Lib/CameraToggle.py
Library      uiautomatorlibrary

*** Keywords ***
VERIFY LAUNCH CAMERA APP
    Log to Console    Launching the Camera Application...!!
    ${res}          launchApplication    org.codeaurora.snapcam    com.android.camera.CameraLauncher
    ${app_launch}    wait for exists    5000    resourceId=org.codeaurora.snapcam:id/scene_mode_switcher
    Log to Console    ${app_launch}
    Run Keyword If   ${app_launch}==True    Log to Console    Camera App is Launched Sucessfully...!!
    ...  ELSE  Fail  Camera is not able to launch..!!

CAPTURE IMAGE
    Log to Console    Capturing Image...!!
    Builtin.sleep     3
    Capturescreen

SWITCH TO ANOTHER CAMERA
    switchCamera

Start LOGCAT
    ${log_cat}    startCollectLogcat    ${EXEC_DIR}/logs/Camera_log.txt
    
GETLOG
    ${get_log}    parseLog    ${EXEC_DIR}/logs/Camera_log.txt
    Log to Console    ${get_log}
    [Return]   ${get_log}

CAMERATOGGLE
    [Arguments]    ${iterations}
    Log to Console  Performing the toggle operation...!!
    :For  ${i}  IN RANGE  ${iterations}
    \    Log to Console    Taking the Image in loop : ${i+1}
    \    CAPTURE IMAGE
    \    Log to Console    Switching to Another Camera in loop : ${i+1}...!!
    \    SWITCH TO ANOTHER CAMERA
    \    Log to Console    Taking the Image again after switching 
    \    CAPTURE IMAGE
    

VERIFY FRONT IMAGE CAPTURE
    Log to Console  Verifying the image is captured sucessfully or not in front camera...!!
    [Arguments]    ${iter}   ${result}
    ${front_image_validations}    Front Image Validations   ${iter}    ${result}
    Log to Console   ${front_image_validations}
    Run Keyword If   '${front_image_validations}'=='True'    Log to Console    Front camera was launched and captured screenshot given no of iterations
    ...  ELSE  Fail  Front camera was not launched and captured screenshot given no of iterations

VERIFY BACK IMAGE CAPTURE
    [Arguments]    ${iter}   ${result}
    Log to Console  Verifying the image is captured sucessfully or not in back camera...!!
    ${back_image_validations}    Back Image Validations    ${iter}    ${result}
    Log to Console   ${back_image_validations}
    Run Keyword If   '${back_image_validations}'=='True'    Log to Console    Back camera was launched and captured screenshot given no of iterations
    ...  ELSE  Fail  Back camera was not launched and captured screenshot given no of iterations



    