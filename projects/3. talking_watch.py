from microbit import *
import speech
from time import ticks_ms, ticks_diff

hours = 0
minutes = 0
mode = False
time = "0:0"
scheduled_time = 4000
last_time = 0

def check_button_press();
    global mode
    if button_a.is_pressed() and button_b.is_pressed():
        mode = not mode

def set_time():
    global hours
    global minutes
    global time
    global mode
    if button_a.is_pressed() and button_b.is_pressed():
        mode = not mode
    elif button_a.is_pressed():
        hours = hours + 1
        display.show(hours, clear = True)
    elif button_b.is_pressed():
        minutes = minutes + 1
        display.show(minutes, clear = True)
    time = str(hours)+":"+str(minutes)
    
def keept_time():
    global mode
    global hours
    global minutes
    global last_time
    if ticks_diff(ticks_ms(), last_time) > 60000:
        minutes = minutes + 1
        last_time = ticks_ms()
        speech.say("Time now is "+str(hours)+" hours and "+str(minutes)+" minutes")
    if minutes >59:
        hours = hours + 1
        minutes = 0
    if hours > 23:
        hours = 0
    return str(hours)+":"+str(minutes)
    
while True:
    if mode == True:
        set_time()
        scheduled_time = ticks_ms() + 4000
    else:
        check_button_press()
        if ticks_diff(scheduled_time, ticks_ms()) > 3500:
            display.scroll(keep_time()), wait=False, loop= False)
        if ticks_diff(scheduled_time, ticks_ms()) < 0:
            scheduled_time = ticks_ms() + 4000