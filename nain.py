#working

import RPi.GPIO as IO    # calling for header file which helps in using GPIOs of PI

import time              # we are calling for time to provide delays in program

IO.setwarnings(False)    # do not show any warnings

IO.setmode (IO.BCM)      #programming the GPIO by BCM pin numbers (like PIN29 as GPIO5)

while 1:
    if (IO.input(27) == 0):  #If GPIO 27 goes low toggle LED on 21pin and print RIGHT
        time.sleep(0.01)
        print ("RIGHT")
    if (IO.input(4) == 1):   #If GPIO 4 goes high toggle LED on 20pin and print LEFT
        time.sleep(0.01)
        print ("LEFT")
    if (IO.input(22) == 0):  #If GPIO 22 goes low toggle LED on 16pin and print UP
        time.sleep(0.01)
        print ("UP")
    if (IO.input(17) == 1):  #If GPIO 17 goes high toggle LED on 12pin and print DOWN
        time.sleep(0.01)
        print ("DOWN") 
