# 9v battery connect

import pygame
import sys
import os
from pygame.locals import *
import RPi.GPIO as GPIO

GPIO_pin_White = 7
GPIO_pin_Grey = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_pin_White,GPIO.OUT)
GPIO.setup(GPIO_pin_Grey,GPIO.OUT)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Left Right')

key_state_map = {K_LEFT: False, K_RIGHT: False}

def all_pins_off():
    GPIO.output(PIO_pin_White, False)
    GPIO.output(PIO_pin_Grey, False)
    
def detect_key(keys, key_to_detect, key_state_map, GPIOPin, not_with_keys):
    if keys[key_to_detect]:
        
        #This key is pressed, make sure not with keys are not also pressed
        for not_with_key in not_with_keys:
            if key_state_map[not_with_key]:
                os.system("aplay /home/pi/python_games/badswap.wav")
                print("You can't press these keys together")
                return
            
        if key_state_map[key_to_detect] == False:
            key_state_map[key_to_detect] = True
            #print("ON")
            GPIO.output(GPIOPin, True)
            #os.system("aplay /home/pi/python_games/badswap.wav")
    else:
        if key_state_map[key_to_detect] == True:           
            key_state_map[key_to_detect] = False
            #print("OFF")
            GPIO.output(GPIOPin, False)
            #os.system("aplay /home/pi/python_games/match2.wav")


all_pins_off

running = True
while running:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    
    detect_key(keys, K_LEFT, key_state_map, GPIO_pin_White, [K_RIGHT])
    detect_key(keys, K_RIGHT, key_state_map, GPIO_pin_Grey, [K_LEFT])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


all_pins_off
GPIO.cleanup()

pygame.quit();
sys.exit;

# 9v battery disconnect