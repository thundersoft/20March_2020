*** Settings ***

Resource     ${EXEC_DIR}/Keywords/Generic_Keywords.robot
Variables    ${EXEC_DIR}/Variables/Config.yaml

*** Test Cases ***
test_launchapp_iterations: It verifies the App launch and close launch based on number of iterations provided
    create UIAutomatorObject
    VERIFY LANCH AND CLOSE APPLICATION USING TIME    ${LAUNCH_CLOSE_ITERATIONS_TIME_MIN}
    
    