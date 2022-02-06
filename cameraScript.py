from datetime import datetime
from time import sleep
from picamera import PiCamera
from gpiozero import LED

debug = True

picLed = LED(27)

camera = PiCamera()
path = '/home/pi/Desktop/plantes/' # The path of the folder you want your jpegs to be saved in.
initWaitTime = 5
waitTime = 900 # This is the time between every frame, I made it 15min for my 10 weeks timelapse.
maxPics = 6720 # The max number of picture you want to take in total, check how much space you have left.

def debugPrint(prtStr):
    if debug:
        print(prtStr)

def mainLoop(time):
    i=0
    while i < time:
        now = datetime.now()
        picLed.on()
        # I used a datetime format for the files name so it's easier to do the editing later.
        camera.capture(path + now.strftime('%m-%d%Y %H-%M-%S') + '.jpg') 
        picLed.off()
        debugPrint('Picute #' + str(i+1) + ' taken.')
        sleep(waitTime)
        i+=1


def startIt():
    
    # I have commented out the camera previews because it takes all your screen if it happens hold crt+al+t and blindly type "pkill python3"
    #camera.start_preview()
    sleep(initWaitTime)
    mainLoop(maxPics)
    #camera.stop_preview()
    debugPrint('done')
    

startIt()
