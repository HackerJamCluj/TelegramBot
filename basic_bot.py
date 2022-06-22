import telepot
import sys
import time
import random
import datetime

import RPi.GPIO as GPIO

LED_PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/turnLightOn':
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif command == '/turnLightOff':
         GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == '__main__':

    bot = telepot.Bot('YOUR TOKEN HERE')
    bot.message_loop(handle)
    print('I am listening')

    while 1:
        time.sleep(10)
