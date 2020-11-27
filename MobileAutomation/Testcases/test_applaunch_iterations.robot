*** Settings ***

Resource     ../Keywords/Generic_Keywords.robot
Variables    ../Variables/Config.yaml
Variables    ../Variables/Device_config.yaml


*** Test Cases ***
test_launchapp_iterations: It verifies the App launch and close launch based on number of iterations provided
    create UIAutomatorObject    ${TEST_DEVICE_ID}
    VERIFY LANCH AND CLOSE APPLICATION IN ITERATIONS    ${LAUNCH_CLOSE_ITERATIONS}    ${TEST_DEVICE_ID}
    

Sample_Test: to understand list
    @{MyList}=    Create List    
    Log to Console    ${MyList}