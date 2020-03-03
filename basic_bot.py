import telepot
import sys
import time
import random
import datetime

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/lightTurnOn':
        GPIO.output(18,GPIO.HIGH)
    elif command == '/lightTurnOff':
         GPIO.output(18,GPIO.LOW)

if __name__ == '__main__':

    bot = telepot.Bot('YOUR TOKEN HERE')
    bot.message_loop(handle)
    print 'I am listening'

    while 1:
        time.sleep(10)
