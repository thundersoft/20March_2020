import os, sys,re,time,subprocess
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.normpath(TEST_DIR + os.sep + os.pardir )
sys.path.append(ROOT_DIR)
from Utilities import command
from time import sleep
from Lib.uiAutomatorLib import uiAutomatorLib


class CameraToggle(uiAutomatorLib):

    def __init__(self):
        super().__init__()

    def captureScreen(self):
        if self.isElementExistsWithResourceId("org.codeaurora.snapcam:id/shutter_button"):
            self.clickUsingResourceId("org.codeaurora.snapcam:id/shutter_button")
            sleep(1)

    def switchCamera(self):
        if self.isElementExistsWithResourceId("org.codeaurora.snapcam:id/front_back_switcher"):
            self.clickUsingResourceId("org.codeaurora.snapcam:id/front_back_switcher")

    def startCollectLogcat(self,filePath):
        cmd = "logcat -c"
        command.executeCommandOnDevice(cmd)
        logcatPid = self.collectLogcat(filePath)
        if logcatPid is not None:
            return logcatPid

    def toggleCamera(self,filePath):
        self.captureScreen()# back camera
        sleep(1)
        self.switchCamera()
        self.captureScreen()# front camera
        self.switchCamera()

    def parseLog(self,logFile):
        cameraActions = list()
        try:
            with open(logFile, 'r') as file:
                for line in file:
                    # take_picture: 930: [KPI Perf]: E PROFILE_TAKE_PICTURE camera id 1
                    regex = re.search(r'.*take_picture:\s+\d+:\s+\[KPI Perf\]:\s+E\s+PROFILE_TAKE_PICTURE camera id\s+(\d)$',line)
                    if regex:
                        cameraType = int(regex.group(1).strip())
                        cameraActions.append(cameraType)
            return cameraActions

        except Exception as e:
            print("Exception occured while parsing log file")
            print(e.__str__())

    def front_image_validations(self,iterations,resultData):
        oneCount = sum(resultData)
        print (type(oneCount),resultData,type(iterations))
        if str(oneCount) == str(iterations):
            print("Front camera was launched and captured screenshot given no of iterations")
            return True
        else:
            print("Front camera was not launched and captured screenshot given no of iterations")
            return False

    def back_image_validations(self,iterations,resultData):
        oneCount = sum(resultData)
        zeroCount = len(resultData) - sum(resultData)
        if str(zeroCount) == str(iterations):
            print("Back camera was launched and captured screenshot given no of iterations")
            return True
        else:
            print("Back camera was not launched and captured screenshot given no of iterations")
            return False
    def verify_close_app(self):
        #subprocess.call('adb shell am force-stop org.codeaurora.snapcam',shell=True)
        
        subprocess.Popen( 'adb shell am force-stop org.codeaurora.snapcam',shell=True,stdin=subprocess.DEVNULL)
        if self.isElementExistsWithResourceId("org.codeaurora.snapcam:id/scene_mode_switcher"):
            return True
        '''except:
            return False
        return False'''
if __name__ == "__main__":
    iterations = 2
    filePath = os.path.join(os.path.join(ROOT_DIR,"Logs"), "camera_log.txt")
    obj = CameraToggle()
    obj.getDeviceInstance()
    if obj.device is not None:
        logcatPid = obj.startCollectLogcat(filePath)
        obj.launchApplication("org.codeaurora.snapcam","com.android.camera.CameraLauncher")
        for i in range(0,iterations):
            obj.toggleCamera(filePath)
        logcatPid.kill()
        obj.closeRecentApplication()
        resultData = obj.parseLog(filePath)
        obj.testValidation(iterations,resultData)
    else:
        print("unable to get the device instance")
