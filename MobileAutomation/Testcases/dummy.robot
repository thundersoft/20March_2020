*** Settings ***
variables   ${EXEC_DIR}/Variables/config.yaml
*** Variables ***
${var}    10
#@{var}    Create List    10    20     30    
*** Test Cases ***
Sample: Testing
    Log to Console    Variable is ${LAUNCH_RESOURCE_ID}
    Run Keyword If  ${var}==15   Log to Console   tc is true..!!
    ...  ELSE   Fail  Tc is not frue..