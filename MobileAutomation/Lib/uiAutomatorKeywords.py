import re
from uiautomator import Device
from time import sleep
import subprocess

class uiAutomatorKeywords:
    def __init__(self):
        self.device = None

    def getDeviceInstance(self):
        deviceId = self.getDeviceID()
        if deviceId is not None:
            self.device = Device(deviceId)

    def addItemToCart(self):
        self.getDeviceInstance()
        self.openAppList()
        self.clickUsingText("Amazon Shopping")
        self.clickUsingText("Search")
        self.clearTheText("Search")
        self.setText("Search", "one plus 7 mobile")
        self.pressDown()
        self.pressEnter()
        self.clickUsingText("OnePlus 7 (Mirror Grey, 6GB RAM, 128GB Storage)")
        self.scrollAndClickAnElement("Add to Cart", "android.widget.Button")
        self.pressEnter()
        self.checkAndClickUsingText("DONE")

    def executeCommandOnDevice(self, command):
        try:
            output = None
            commandToExecute = self.__getPrefixCommand()
            commandToExecute += command
            output = subprocess.check_output(commandToExecute, shell=True)
            if output is not None:
                outputStr = output.decode('utf-8')
                return outputStr
        except Exception as e:
            print("Error: {}".format(e.__str__()))
            return None

    def __getPrefixCommand(self):
        return "adb "

    def getDeviceID(self):
        deviceId = None
        cmd = "devices"
        output = self.executeCommandOnDevice(cmd)
        if output is not None:
            for line in output.splitlines():
                reObj = re.search(r'(\w+).*device\b', line)
                if reObj:
                    deviceId = reObj.group(1).strip()
        return deviceId

    def openAppList(self):
        self.device.press.home()
        self.swipeUp()

    def getCoOrdinates(self, xPercentage, yPercentage):
        x = (self.device.info['displayWidth']*xPercentage)/100
        y = (self.device.info['displayHeight']*yPercentage)/100
        return x,y

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
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1,y1,x2,y2,speed)
        self.executeCommandOnDevice(cmd)

    def scrollDown(self,speed=60):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1,y1,x2,y2,speed)
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
        if className is None:
            self.device(text=textObj,instance=instance).click.wait()
            sleep(1)
        else:
            self.device(text=textObj, className= className, instance=instance).click.wait()

    def clearTheText(self, textObj, instance=0):
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

    def scrollAndClickAnElement(self, textObj, className=None, instance=0):
        self.getDeviceInstance()
        count = 0
        while count <= 10:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj, className, instance)
                print(count)
                # break
            else:
                self.scrollUp(500)
            count += 1

    def isElementwithTextExists(self,textObj):
        if self.device(text=textObj).exists:
            return True
        return False

    def checkAndClickUsingText(self, textObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj,instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def recordScreen(self, filePath):
        cmd = "adb shell screenrecord {}".format(filePath)
        pid = subprocess.Popen(cmd, shell=True)
        if pid is not None:
            return pid

    def stopRecording(self, pid):
        pid.kill()