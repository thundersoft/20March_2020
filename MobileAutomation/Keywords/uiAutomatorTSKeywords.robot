*** Settings ***
Library  ../Lib/uiAutomatorLib.py


*** Keywords ***
create UIAutomatorObject
    [Documentation]  It will create the instance of the connected device
    getdeviceinstance

get Device ID
    [Documentation]  Get the connected device id
    getDeviceID

launch App Menu
    [Documentation]  It will open the app menu
    openAppList

Launch Application
    [Arguments]    ${packageName}    ${activityName}
    [Documentation]  It will open the particular application
    launchApplication    ${packageName}    ${activityName}
    
Close Application
    [Arguments]    ${packageName}
    [Documentation]  It will close the particular application
    closeApplication    ${packageName}    ${activityName}
    
VERIFY LAUNCH APPLICATION
    [Arguments]    ${packageName}    ${activityName}
    Launch Application    ${packageName}    ${activityName}
    ${launch_res}  waituntillgettingresourceId    org.codeaurora.snapcam:id/scene_mode_switcher    5000
    [Return]    ${launch_res} 
   
VERIFY CLOSE APPLICATION
    [Arguments]    ${packageName}    ${activityName}
    Launch Application    ${packageName}    ${activityName}
    ${close_res}  waituntillgettingresourceId    org.codeaurora.snapcam:id
    [Return]    ${close_res}
get screen resolution
    [Documentation]  It will give the resolution of the device
    ${height}  ${width} = getCoOrdinates
    [Return]  ${height} ${width}

do scroll up
    [Documentation]  It will scroll the screen towards top
    scrollUp

do scroll down
    [Documentation]  It will scroll the screen towards down
    scrollDown

do scroll right
    [Documentation]  It will scroll the screen towards right
    scrollRight

do scroll left
    [Documentation]  It will scroll the screen towards left
    scrollLeft

do drag up
    [Documentation]  It will drag the screen to up
    dragUp

do drag down
    [Documentation]  It will drag the screen to down
    dragDown

click using Text Element
    [Documentation]  It will click on the text element
    [Arguments]     ${textelementlocator}  ${classname}=None  ${instance}=0
    clickUsingText  ${textelementlocator}  ${classname}  ${instance}

click Using Description Element
    [Documentation]  It will click on the description elements
    [Arguments]            ${descriptionelementlocator}  ${classname}=None  ${instance}=0
    clickUsingDescription  ${descriptionelementlocator}  ${classname}  ${instance}

clear text Element
    [Documentation]  It will clear the text of textbox
    [Arguments]  ${texteleloc}  ${instance}=0
    clearText    ${texteleloc}  ${instance}

press Down button
    [Documentation]  It will execute down input keyevent
    pressDown

press Back Button
    [Documentation]  It will navigage to previous page
    pressBack

press Enter Button
    [Documentation]  It will press the center button
    pressEnter

scroll And Click
    [Arguments]  ${textElementLocator}
    scrollAndClickAnElement  ${textelementlocator}

is Element exists with text
    [Arguments]              ${textelementlocator}
    isElementwithTextExists  ${textelementlocator}

check and click using text
    [Arguments]             ${textelementlocator}  ${classname}=None  ${instance}=0
    checkAndClickUsingText  ${textelementlocator}  ${classname}  ${instance}

capture Video
    [Arguments]   ${filepath}
    recordScreen  ${filepath}

pull Files From Device
    [Arguments]  ${srcpath}  ${destinationpath}
    pullFiles    ${srcpath}  ${destinationpath}

set Text
    [Arguments]  ${text}
    enterText    ${text}

input Keyevent
    [Arguments]    ${keycode}
    pressKeycode   ${keycode}

is Element exists with Description
    [Arguments]                     ${desclocator}
    isElementExistsWithDescription  ${desclocator}

check and click using Description
    [Arguments]                    ${desclocator}  ${instance}=0
    checkAndClickUsingDescription  ${desclocator}  ${instance}

is Element exists with ResourceID
    [Arguments]  ${resourceidloc}
    isElementExistsWithResourceId  ${resourceidloc}

click using ResourceID
    [Arguments]           ${resourceidloc}  ${classname}=None  ${instance}=None
    clickUsingResourceId  ${resourceidloc}  ${classname}  ${instance}

check and click using ResourceID
    [Arguments]  ${resourceidloc}  ${instance}=0
    checkAndClickUsingResourceId   ${resourceidloc}  ${instance}

get Device Brand
    ${devicebrand} =  getDeviceBrand
    [Return]  ${devicebrand}

get Device Model
    ${devicemodel} =  getDeviceModel
    [Return]  ${devicemodel}

get installed Apps list
    @{apps} =  getInstalledApps
    [Return]  @{apps}

check application is installed
    ${result} =  isApplicationInstalled
    [Return]  ${result}

set Screen Timeout
    [Arguments]       ${timeinmilliseconds}
    setScreenTimeOut  ${timeinmilliseconds}

check Display ON
    [Documentation]  It will check whether the display is on or not
    ${result} =  isDisplayON
    [Return]  ${result}

disable Display
    [Documentation]  It will turn on the dispaly of the connected device
    turnDisplayON

get Text
    [Documentation]  Get the text from textbox
    [Arguments]  ${resourceeleloc}  ${classname}
    ${text} =  getText  ${resourceeleloc}  ${classname}
    [Return]  ${text}

collect logcat
    [Documentation]  Collects the logs of the connected devices
    [Arguments]     ${filepath}
    collectLogcat   ${filepath}

open Application
    [Documentation]  It will launch an application
    [Arguments]          ${packagename}   ${activityname}
    launchApplication    ${packagename}   ${activityname}

close recent applications
    [Documentation]  It will close all the recent applications
    closeRecentApplication

root device
    [Documentation]  Make the device has root permissions
    root

remount device
    [Documentation]  Give the remount permissions to the device
    remount

reboot device
    [Documentation]  Reboot the device
    reboot

get Application launch time
    [Documentation]  It will return the time which application is taking to launch
    [Arguments]   ${packagename}  ${activityname}
    ${launchtime} =  launchApplication  ${packagename}  ${activityname}
    [Return]  ${launchtime}











