from datetime import datetime
path = '/home/pi/desktop/plantes/'
initWaitTime = 5
waitTime = 2

def mainLoop():
    sleep(waitTime)
    now = datetime.now()
    camera.capture(path + now.strftime('%m-%d%Y %H-%M-%S') + '.jpg')


def startIt():
    camera.start_preview()
    sleep(initWaitTime)
    mainLoop()
    camera.stop_preview()
