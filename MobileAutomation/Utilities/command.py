import subprocess

def executeCommandOnDevice(command):
    try:
        output = None
        commandToExecute = __getPrefixCommand()
        commandToExecute += command
        output = subprocess.check_output(commandToExecute, shell=True)
        if output is not None:
            outputStr = output.decode('utf-8')
            return outputStr
        return None
    except Exception as e:
        print("Error: {}".format(e.__str__()))
        return None


def __getPrefixCommand():
    return "adb "

def executeCommandInBackground(command):
    try:
        output = None
        commandToExecute = __getPrefixCommand()
        commandToExecute += command
        pid = subprocess.Popen(commandToExecute, shell=True)
        if pid is not None:
            return pid
        return None
    except Exception as e:
        print("Error: {}".format(e.__str__()))
        return None

def executeCommand(cmd):
    try:
        output = subprocess.check_output(cmd)
        if output is not None:
            outputStr = output.decode('utf-8')
            return outputStr
        return None
    except Exception as e:
        print("Error: {}".format(e.__str__()))
        return None
