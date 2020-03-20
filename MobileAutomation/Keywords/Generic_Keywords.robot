*** Settings ***
Library    ../Lib/uiAutomatorLib.py
Library    DateTime

*** Keywords ***
create UIAutomatorObject
    [Arguments]   ${Device_Id}
    [Documentation]  It will create the instance of the connected device
    getdeviceinstance    ${Device_Id}
    [Return]    

Launch Application
    [Arguments]    ${packageName}    ${activityName}    ${TEST_DEVICE_ID}
    [Documentation]  It will open the particular application
    launch_Application_using_adb    ${packageName}    ${activityName}    ${TEST_DEVICE_ID}
    
Close Application
    [Documentation]  It will close the particular application
    closeRecentApplication  
    
VERIFY LAUNCH APPLICATION
    [Arguments]    ${launch_resource_id}
    ${launch_res}  waituntillgettingresourceId     ${launch_resource_id}    5000
    [Return]    ${launch_res} 
   
VERIFY CLOSE APPLICATION
    [Arguments]    ${close_resource_id}
    ${close_res}  waituntillgettingresourceId    ${close_resource_id}      5000
    [Return]    ${close_res}


VERIFY LANCH AND CLOSE APPLICATION IN ITERATIONS
    [Arguments]    ${iterations}    ${TEST_DEVICE_ID}
    :For   ${index}   IN RANGE   ${iterations}  
    \    Log to Console   Launching the application in loop:${index+1}
    \    LAUNCH APPLICATION      ${APP_PACKAGE_NAME}     ${APP_ACTIVITY_NAME}    ${TEST_DEVICE_ID}
    \    Log to Console   Verifying whether the application is launched or not in loop:${index+1}
    \    ${launch_res}    VERIFY LAUNCH APPLICATION    ${LAUNCH_RESOURCE_ID}
    \    Run Keyword If   ${launch_res}==True    Log to Console   Application is launched sucessfully in loop:${index+1}
         ...  ELSE  Log to Console  Application is not launched sucessfully in loop:${index+1}
    \    Log to Console   Closing the application in loop:${index+1}
    \    Builtin.sleep    1
    \    close_application_using_adb     ${APP_PACKAGE_NAME}    ${TEST_DEVICE_ID}
    \    Log to Console   Verifying whether the application is closed or not in loop:${index+1}
    \    ${close_res}    VERIFY CLOSE APPLICATION    ${CLOSE_RESOURCE_ID}
    \    Run Keyword If   ${close_res}==True    Log to Console   Application is closed sucessfully in loop:${index+1}
         ...  ELSE  Log to Console  Application is not closed sucessfully in loop:${index+1}
    \    Log to Console  ${close_res},${launch_res}
    \    ${final_test_res}=   Set Variable If   ${close_res}==True and ${launch_res}==True  
         ...  ${index+1}
    Log to Console   ......${final_test_res}
    Run Keyword If   ${final_test_res}==${iterations}    Log to Console   Launch and close operations is verified sucessfully...!!
    ...  ELSE  Fail   Launch and close operations is not able to verified in above loops...!!

VERIFY LANCH AND CLOSE APPLICATION USING TIME
    [Arguments]    ${time}
    ${get_current_time}    Get Current Date
    Log to Console     ${get_current_time}
    :For   ${index}   IN RANGE   9999999
    \    Log to Console   Launching the application in loop:${index+1}
    \    LAUNCH APPLICATION      ${APP_ACTIVITY_NAME}     ${APP_PACKAGE_NAME}
    \    Log to Console   Verifying whether the application is launched or not in loop:${index+1}
    \    ${launch_res}    VERIFY LAUNCH APPLICATION    ${LAUNCH_RESOURCE_ID}
    \    Run Keyword If   ${launch_res}==True    Log to Console   Application is launched sucessfully in loop:${index+1}
         ...  ELSE  Fail  Application is not launched sucessfully in loop:${index+1}
    \    Log to Console   Closing the application in loop:${index+1}
    \    Close Application
    \    Log to Console   Verifying whether the application is closed or not in loop:${index+1}
    \    ${close_res}    VERIFY CLOSE APPLICATION    ${CLOSE_RESOURCE_ID}
    \    Run Keyword If   ${close_res}==True    Log to Console   Application is closed sucessfully in loop:${index+1}
         ...  ELSE  Fail  Application is not closed sucessfully in loop:${index+1}
    \    ${get_time_after_one_iter}    Get Current Date
    \    ${res}    Subtract Date From Date   ${get_time_after_one_iter}    ${get_current_time}
    \    Log to Console    Completed time After this iteration is :${res/60} mins
    \    ${time_ver}    Evaluate   ${res}>=${time}*60
    \    Exit for loop If   ${time_ver}==True
    
    
VERIFY RESTART ON GIVEN ITERATIONS
    [Arguments]    ${restart_iterations}
    :For   ${index}  IN RANGE   ${restart_iterations}
    \    Log to Console    Verifying the restart operation in loop:${index+1}
    \    ${restart_res}    reboot_to_normal    
    \     Run Keyword If   ${restart_res}==True    Log to Console   Restart Operation is verified sucessfully in loop:${index+1}
         ...  ELSE  Fail  Restart Operation is not able to verified in loop:${index+1}
    
    