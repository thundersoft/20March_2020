*** Settings ***
Resource     ../Keywords/Generic_Keywords.robot
Variables    ../Variables/Config.yaml
Variables    ../Variables/Device_config.yaml
*** Test Cases ***
test_restart_iterations: Restart verification
    [Tags]    Camera
    create UIAutomatorObject    ${TEST_DEVICE_ID}
    VERIFY RESTART ON GIVEN ITERATIONS    ${RESTART_ITERATIONS}
