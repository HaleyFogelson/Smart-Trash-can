#!/usr/bin/env python
#pin numbers colors: red 10 blue 11 green 12
#Infared sensor 17
#servo pin 3
# import required libs and functions
import time
import pigpio
import calendar
import datetime
import os
import RPi.GPIO as GPIO
from picamera import PiCamera
from classify_image import run_inference_on_image
from class_list import class_dictionary
#Servo motor stuff I added
import RPi.GPIO as GPIO
from time import sleep
GPIO.setup(3,GPIO.OUT)
pwm = GPIO(03,50)
pwm.start(0)
#the color pins
red = 10
blue =11
green= 12
## SET UP VARIABLES
pi=pigpio.pi()
# Time variables
motor_delay = 0.001 # Sets the amount of time between each step on the motor (in seconds)

# Half-step sequence for smooth motion
sequence = [ [1,0,0,0],
             [1,1,0,0],
             [0,1,0,0],
             [0,1,1,0],
             [0,0,1,0],
             [0,0,1,1],
             [0,0,0,1],
             [1,0,0,1]
           ]

# Sets up the GPIO pin locations on the raspberry pi
step_pins = [27,18,21,22] # be sure you are setting pins accordingly (for this setup: GPIO27,GPIO18,GPIO21,GPI22)
pir_pin = 17 # this is the starting pin we used for the PIR sensor

# Set trash type hash
waste_type = {"r":"Recycling", "c":"Compost"}

# set path of saved images directory
photo_depot = '/home/pi/Pictures/'
os.chdir(photo_depot)
camera = PiCamera()
class_dictionary = class_dictionary();
def SetAngle(angle)
  duty = angle /18+2
  GPIO.output(3,True)
  pwm.ChangeDutyCycle(duty)
  sleep(1)
  GPIO.output(3,False)
  pwm.ChangeDutyCycle(0)
  
def setcolor(pin,brightness):
  pi.set_PWM_dutycycle(pin,brightness)
  
def predict_top_5(image_url):
    print("Tensorflow is processing the image...")
    return run_inference_on_image(image_url)


def top_prediction_name(prediction):
    return prediction[4]


def what_is_it(image_name):
    image_path = photo_depot + image_name  # Setting variable for image filepath.
    top_5 = predict_top_5(image_path)  # Pulling-out the top 5 matched results
    print top_5

    top = top_5[4]  # Pulling-out the top class
    top_name = top[0]  # Pulling-out the top class name

    print "THE OBJECT WAS: " + top_name

    if class_dictionary[top_name] == 'c':
<<<<<<< HEAD

=======
>>>>>>> abb619bc169ab5fe281bc988c2bdb0b6c04768ca
        return 'c'
    else:
        return 'r'


def ClickPicture():
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    camera.resolution = (1024,768)
    camera.start_preview()

    time.sleep(1)

    image_name = date + '_img.jpg'

    camera.capture(image_name)
    camera.stop_preview()

    GPIO.cleanup()

    return image_name


def RunMotor():
<<<<<<< HEAD
  for i in range(256): # running motor (256) steps in one revolution
=======
  for i in range(256): # running motor (512) steps in one revolution
>>>>>>> abb619bc169ab5fe281bc988c2bdb0b6c04768ca
        for halfstep in range(8): # 8 steps in each cycle
            for pin in range(4): # 4 plates
                GPIO.output(step_pins[pin], sequence[halfstep][pin]) # activate the pins
            time.sleep(motor_delay) # delay between each step


def SetPins():
    # Set all pins as output
    for pin in step_pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)


def CounterClockwise():
    GPIO.cleanup(); # cleaning up in case GPIOS have been preactivated
    GPIO.setmode(GPIO.BCM); # use BCM GPIO references instead of physical pin numbers
    SetPins(); # set all pins as output
    RunMotor(); # turns the motor 90 degrees
    GPIO.cleanup(); # cleaning up GPIOs


def ClockWise():
    sequence.reverse() # reverse the sequence direction
    CounterClockwise() # calls the same function, just in reverse
    sequence.reverse() # sets sequence variable back to original state


def MasterFunction():
    print "HELLO - WELCOME TO CERBERUS"

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_pin, GPIO.IN)

    i = GPIO.input(pir_pin)

    # No movement detected
    if i == 0:
        print 'No Intruders'
        time.sleep(2)

    # Movement detected
    elif i == 1:
        print 'Intruder Detected'
        image_name = ClickPicture();
        trash_type = what_is_it(image_name)
        print "WASTE TYPE: " + waste_type[trash_type]

        if trash_type == "r":
            ClockWise();
            setcolor(green,255)
            time.sleep(1)
            CounterClockwise();
        else:
            CounterClockwise();
            setcolor(red,255)
            time.sleep(1)
            ClockWise();

        del image_name
    #button for pushing
    recycling_button=(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    recycling_button = GPIO.input(18)
    trash_button=(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    trash_button = GPIO.input(19)
    if recycling_button = false
      SetAngle(0)
      SetAngle(90)
    if trash_button = false
      SetAngle(180)
      SetAngle(90)
      
    
    


while True:
    MasterFunction()



