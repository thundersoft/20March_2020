from Lib.uiAutomatorLib import uiAutomatorLib

obj = uiAutomatorLib()
obj.getDeviceInstance()
obj.clickUsingText("Email")
obj.closeRecentApplication()