from datetime import datetime
from time import sleep
from picamera import PiCamera
from gpiozero import LED

debug = True

picLed = LED(27)

camera = PiCamera()
path = '/home/pi/Desktop/plantes/'
initWaitTime = 5
waitTime = 5 #900 # 15 minutes
maxPics = 6720

def debugPrint(prtStr):
    if debug:
        print(prtStr)

def mainLoop(time):
    i=0
    while i < time:
        now = datetime.now()
        picLed.on()
        camera.capture(path + now.strftime('%m-%d%Y %H-%M-%S') + '.jpg')
        picLed.off()
        debugPrint('Picute #' + str(i+1) + ' taken.')
        sleep(waitTime)
        i+=1


def startIt():
    #camera.start_preview()
    sleep(initWaitTime)
    mainLoop(maxPics)
    #camera.stop_preview()
    debugPrint('done')
    

startIt()