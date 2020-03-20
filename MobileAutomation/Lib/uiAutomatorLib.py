import re,sys
import subprocess
from uiautomator import Device
from time import sleep

class uiAutomatorLib:

    def __init__(self):
        self.device = None

    def getDeviceInstance(self,deviceId):
        #deviceId = self.getDeviceID()
        #if deviceId is not None:
            #self.device = Device(deviceId)
        self.device = Device(deviceId)

    def getDeviceID(self):
        deviceId = None
        cmd = "devices"
        output = self.executeCommandOnDevice(cmd)
        if output is not None:
                reObj = re.search(r'(\w+-?\w+?).*device\b', output,re.MULTILINE)
                if reObj:
                    deviceId = reObj.group(1).strip()
                    return deviceId
                else:
                    return "No Device"


    def openAppList(self):
        self.device.press.home()
        self.swipeUp()

    def getCoOrdinates(self, xPercentage, yPercentage):
        x = (self.device.info['displayWidth'] * xPercentage) / 100
        y = (self.device.info['displayHeight'] * yPercentage) / 100
        return x, y

    def swipeUp(self):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        self.device.swipe(x1, y1, x2, y2)

    def swipeDown(self):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        self.device.swipe(x1, y1, x2, y2)

    def scrollUp(self, speed=60):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1, y1, x2, y2, speed)
        self.executeCommandOnDevice(cmd)

    def scrollDown(self, speed=60):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1, y1, x2, y2, speed)
        self.executeCommandOnDevice(cmd)

    def scrollRight(self, speed=60):
        x1, y1 = self.getCoOrdinates(25, 50)
        x2, y2 = self.getCoOrdinates(75, 50)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1, y1, x2, y2, speed)
        self.executeCommandOnDevice(cmd)

    def scrollLeft(self, speed=60):
        x1, y1 = self.getCoOrdinates(75, 50)
        x2, y2 = self.getCoOrdinates(25, 50)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1, y1, x2, y2, speed)
        self.executeCommandOnDevice(cmd)

    def dragUp(self):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        self.device.drag(x1, y1, x2, y2)

    def dragDown(self):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        self.device.drag(x1, y1, x2, y2)

    def clickUsingText(self, textObj, className=None, instance=0):

        if className is not None:
            self.device(text=textObj, className=className, instance=instance).click.wait()
        else:
            self.device(text=textObj, instance=instance).click.wait()
            sleep(1)

    def clickUsingDescription(self, textObj, className=None, instance=0):
        if className is None:
            self.device(description=textObj, instance=instance).click.wait()
            sleep(1)
        else:
            self.device(description=textObj, className=className, instance=instance).click.wait()

    def clearText(self, textObj, instance=0):
        self.device(text=textObj, instance=instance).clear_text()

    def setText(self, textObj, text, instance=0):
        self.device(text=textObj, instance=instance).set_text(text)
        sleep(1)

    def pressDown(self):
        self.device.press.down()
        sleep(1)

    def pressEnter(self):
        self.device.press.enter()
        sleep(1)

    def pressBack(self):
        self.device.press.back()

    def scrollAndClickAnElement(self, textObj, className=None, instance=0):
        count = 0
        while count <= 20:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj, className, instance)
                break
            else:
                self.scrollUp(500)

    def isElementwithTextExists(self, textObj):
        if self.device(text=textObj).exists:
            return True
        return False

    def checkAndClickUsingText(self, textObj, className=None, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj, className, instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def pullFiles(self, source, destination):
        cmd = "pull {} {}".format(source, destination)
        self.executeCommandOnDevice(cmd)

    def enterText(self, text):
        cmd = "shell input text {}".format(text)
        self.executeCommandOnDevice(cmd)

    def pressKeycode(self, keycode):
        cmd = "shell input keyevent {}".format(keycode)
        self.executeCommandOnDevice(cmd)

    def isElementExistsWithDescription(self, descriptionObj):
        if self.device(description=descriptionObj).exists:
            return True
        return False

    def clickUsingDescription(self, descriptionObj, className=None, instance=0):
        if className is None:
            self.device(text=descriptionObj, instance=instance).click.wait()
            sleep(1)
        else:
            self.device(text=descriptionObj, className=className, instance=instance).click.wait()

    def checkAndClickUsingDescription(self, descriptionObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementExistsWithDescription(descriptionObj):
                self.clickUsingDescription(descriptionObj, instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def isElementExistsWithResourceId(self, resourceIdObj):
        if self.device(resourceId=resourceIdObj).exists:
            return True
        return False
    
    def waituntillgettingresourceId(self,resourceIdObj,time):
        if self.device(resourceId=resourceIdObj).wait.exists(timeout=int(time)):
            return True
        return False
        
    def clickUsingResourceId(self, resourceIdObj, className=None, instance=0):
        if className is None:
            self.device(resourceId=resourceIdObj, instance=instance).click.wait()
            sleep(1)
        else:
            self.device(resourceId=resourceIdObj, className=className, instance=instance).click.wait()

    def checkAndClickUsingResourceId(self, resourceIdObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementExistsWithResourceId(resourceIdObj):
                self.clickUsingResourceId(resourceIdObj, instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def getDeviceProperty(self, property):
        '''
        It will give the property of the device
        :param property:
        :return:
        '''
        try:
            cmd = "shell getprop"
            output = self.executeCommandOnDevice(cmd)
            if output is not None:
                lines = output.splitlines()
                for line in lines:
                    if property in line:
                        (key, value) = line.split(':')
                        patternObj = re.search(r'\[(.*)\]', value)
                        if patternObj:
                            return patternObj.group(1)
            else:
                print("property is not found in getprop list")
                return None
        except Exception as e:
            print("Error:Unable to get the device property")
            print(e.__str__())

    def getDeviceBrand(self):
        '''
        It will return the brand of the device(Ex: Samsung,onePlus..etc)
        :return:
        '''
        brand = self.getDeviceProperty('ro.product.brand')
        return brand

    def getDeviceModel(self):
        '''
        It will return the model of the device
        :return:
        '''
        model = self.getDeviceProperty('ro.product.model')
        return model

    def getInstalledApps(self):
        '''
        It will return the list of applications installed on the device
        :return:
        '''
        cmd = "shell pm list packages"
        packageList = self.executeCommandOnDevice(cmd)
        if packageList is not None:
            return packageList

    def isApplicationInstalled(self, packageName):
        '''
        It checks whether the given application is installed on the device or not
        :param packageName:
        :return: Boolean
        '''
        try:
            packageList = self.getInstalledApps()
            if packageList is not None:
                packageLines = packageList.splitlines()
                for line in packageLines:
                    if packageName in line:
                        patternObj = re.search(r'package:(.*)', line)
                        if patternObj:
                            pkgName = patternObj.group(1)
                            if pkgName == packageName:
                                return True

            return False
        except Exception as e:
            print("Error: while checking the application status")
            print(e.__str__())

    def recordScreen(self, filePath):
        '''
        It will record the screen whatever actions we performed on the device
        :param filePath:
        :return:
        '''
        cmd = "shell screenrecord {}".format(filePath)
        return self.executeCommandInBackground(cmd)

    def setScreenTimeOut(self, time=600000):
        '''
        It will set the device display timeout
        :param time:
        :return:
        '''
        cmd = "shell settings put system screen_off_timeout {}".format(time)
        self.executeCommandOnDevice(cmd)

    def isDisplayON(self):
        try:
            cmd = "shell dumpsys display"
            output = self.executeCommandOnDevice(cmd)
            if output is not None:
                lines = output.splitlines()
                for line in lines:
                    if 'mScreenState' in line:
                        (key, value) = line.split('=')
                        if value == "ON":
                            return True
                        else:
                            return False
        except Exception as e:
            print("Error while checking the display status")
            print(e.__str__())

    def turnDisplayON(self):
        '''
        It will turn on the display
        :return:
        '''
        cmd = "shell input keyevent 26"
        self.executeCommandOnDevice(cmd)

    def getText(self, resourceObj, className):
        '''
        It will extract the value of the textbox and returns the text
        :return: string
        '''
        info = self.device(resourceId=resourceObj, className=className).info
        return info['text']

    def executeCommandOnDevice(self,command):
        try:
            output = None
            commandToExecute = self.__getPrefixCommand()
            commandToExecute += command
            output = subprocess.check_output(commandToExecute, shell=True)
            if output is not None:
                outputStr = output.decode('utf-8')
                return outputStr
            return None
        except Exception as e:
            print("Error: {}".format(e.__str__()))
            return None

    def __getPrefixCommand(self):
        return "adb "

    def executeCommandInBackground(self,command, fileHandle=None):
        try:
            output = None
            commandToExecute = self.__getPrefixCommand()
            commandToExecute += command
            pid = subprocess.Popen(commandToExecute,stdin=fileHandle,stdout=fileHandle,shell=False)
            if pid is not None:
                return pid
            return None
        except Exception as e:
            print("Error: {}".format(e.__str__()))
            return None

    def executeCommand(self,cmd):
        try:
            output = subprocess.check_output(cmd)
            if output is not None:
                outputStr = output.decode('utf-8')
                return outputStr
            return None
        except Exception as e:
            print("Error: {}".format(e.__str__()))
            return None

    def turn_on_off_wifi(self,deviceID,wifi_mode):
        command = 'adb -s '+str(deviceID)+' shell svc wifi enable'
        if wifi_mode=='off':
            command = 'adb -s '+str(deviceID)+' shell svc wifi disable'
        self.executeCommand(command)
       
    def executeCommandAndWriteToFile(self, cmd, filePath):
        pid = None
        try:
            with open(filePath, 'w') as f:
                pid = self.executeCommandInBackground(cmd, f)
        except Exception as e:
            print("Exception occured while collecting logcat")
            print(e.__str__)
        finally:
            return pid

    def collectLogcat(self, filePath):
        cmd = "logcat"
        pid = self.executeCommandAndWriteToFile(cmd, filePath)
        return pid

    def launch_Application_using_adb(self, packageName, activityName,deviceID):
        try:
            cmd = "-s "+str(deviceID) +" shell am start -n {}/{}".format(packageName, activityName)
            self.executeCommandOnDevice(cmd)
        except Exception as e:
            print("Exception occured while launching an application:{}".format(packageName))
            print(e.__str__())

    def close_application_using_adb(self, packageName,deviceID):
        try:
            cmd = "-s "+str(deviceID) +" shell am force-stop {}".format(packageName)
            self.executeCommandOnDevice(cmd)
        except Exception as e:
            print("Exception occured while Closing an application:{}".format(packageName))
            print(e.__str__())
    def make_call_using_adb(self,number,deviceID):
        try:
            cmd = "-s "+str(deviceID) +' shell am start -a android.intent.action.CALL -d tel:"'+str(number)+'"'
            self.executeCommandOnDevice(cmd)
            
        except Exception as e:
            print("Exception occured while  calling a number:{}".format(number))
            print(e.__str__())
    
    def verify_call_connection(self,deviceID):
        try:
            cmd = "-s "+str(deviceID) +' shell dumpsys telephony.registry | grep mCallState'
            status = self.executeCommandOnDevice(cmd)
            status =int(status.split('mCallState=')[2])
            if status!=0:
                return True
            else:
                return False
        except Exception as e:
            print("Exception occured while  verifying a call connection")
            print(e.__str__())
    def end_call_using_adb(self,deviceID):
        try:
            cmd = "-s "+str(deviceID) +' shell input keyevent 6'
            self.executeCommandOnDevice(cmd)
        except Exception as e:
            print("Exception occured while  ending a call connection")
            print(e.__str__())
    
    def verify_call_disconnection(self,deviceID):
        try:
            cmd = "-s "+str(deviceID) +' shell dumpsys telephony.registry | grep mCallState'
            status = self.executeCommandOnDevice(cmd)
            status =int(status.split('mCallState=')[2])
            if status==0:
                return True
            else:
                return False
        except Exception as e:
            print("Exception occured while  verifying a call disconnection")
            print(e.__str__())

    def closeRecentApplication(self):
        self.pressKeycode("KEYCODE_APP_SWITCH")
        count = 0
        while (count <= 5):
            if self.isElementwithTextExists('CLEAR ALL'):
                self.clickUsingText("CLEAR ALL")
                break
            else:
                self.scrollDown()
                count = count - 1

    def reboot(self):
        self.executeCommandOnDevice('reboot')

    def root(self):
        self.executeCommandOnDevice('root')

    def remount(self):
        self.executeCommandOnDevice('remount')

    def launchApplication(self,packageName, activityName):
        cmd = "shell am start -W -n {}/{}".format(packageName,activityName)
        output = self.executeCommandOnDevice(cmd)
        return self.getAppLaunchTime(output)

    def getAppLaunchTime(self, outputStr):
        reg = re.search(r'.*TotalTime:\s+(\d+).*', outputStr, re.MULTILINE)
        launchTime = 0
        if reg:
            launchTime = reg.group(1)
        return launchTime

    def deleteDeviceInstance(self):
        self.executeCommandOnDevice("kill-server")
        self.device = None
        del self
    def reboot_to_normal(self):
        self.reboot()
        total_time=0
        while(total_time<100):
            print (total_time)
            device_id =self.getDeviceID()
            if device_id != "No Device":
                break
            total_time=total_time+5
            print (device_id,total_time)
            sleep(5)
        if self.waituntillgettingresourceId('com.android.launcher3:id/workspace',65000):
            return True
        return False
    def sam(self):
        try:
            subprocess.call('dfsdf')
        except Exception as e:
            print("Exception occured while Closing an application:{}")
            print(e)
        
obj=uiAutomatorLib()
obj.sam()
#obj.getDeviceInstance('32007da2fa3456d1')
#obj.make_call_using_adb('9440644587','32007da2fa3456d1')
#sleep(2)
#print (obj.verify_call_connection('32007da2fa3456d1'))
#obj.end_call_using_adb('32007da2fa3456d1')
#sleep(2)
#print (obj.verify_call_disconnection('32007da2fa3456d1'))
#obj.getDeviceInstance('f957ac9d')
#obj.turn_on_off_wifi('f957ac9d','off')
#obj.turn_on_off_wifi('f957ac9d','off')
# k=obj.reboot_to_normal()
#print (k)