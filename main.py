#!/usr/bin/env python

# Google SHEET: https://docs.google.com/spreadsheets/d/1BrL5Otvrh-FoOBY85auZIQjPN3vux14J4V3oUd4Tpfk/


import RPi.GPIO as GPIO
import time
import signal
import sys
from mfrc522 import SimpleMFRC522

from sheet import push_data


BUTTON_PIN = 40
PWR_PIN = 38
BUTTON_STATE = False
MACHINE_STATE = False

last_user = {}

def signal_handler(sig, frame):
    print("[*] Performing Cleanup!")
    GPIO.cleanup()
    sys.exit()

def button_pressed_callback(channel):
    print("[+] Button Pressed!")
    global BUTTON_STATE
    global MACHINE_STATE
    BUTTON_STATE = not BUTTON_STATE
    if MACHINE_STATE == False:
        print("[+] Machine already powered down! Ignoring...")
    else:
        MACHINE_STATE = False
        global last_user
        update = push_data('3d_printer', last_user['UID'], status=MACHINE_STATE)
        print("[*] Updated Entry: ", update)
        last_user = update
        GPIO.output(PWR_PIN, GPIO.LOW)
        print("[*] Powered Down Machine")


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PWR_PIN, GPIO.OUT)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed_callback, bouncetime=200)

    signal.signal(signal.SIGINT, signal_handler)
    reader = SimpleMFRC522()
    print("[*] Initialization Complete...")
    while True:
        id, text = reader.read()
        print("[+] ID: ", id)
        print("[+] Text: ", text)
        if id is not None and id != '' and MACHINE_STATE == False:
            MACHINE_STATE = not MACHINE_STATE
            update = push_data('3d_printer', id, status=MACHINE_STATE)
            last_user = update
            GPIO.output(PWR_PIN, GPIO.HIGH)
            print("[*] Updated Entry: ", last_user)
    