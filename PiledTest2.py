from hal import hal_led as LED
from hal import hal_input_switch as SWITCH
import time

def main():
    LED.init()
    SWITCH.init()
    level = 1  # LED blinking starts with turn-on
    while (True):
        switch_pos = SWITCH.read_slide_switch()
        if (switch_pos==1): # Slide switch at left position
            LED.set_output(24, level)
            level = not level  # Toggle level for next loop
            time.sleep(0.1)  # 5mHz = 0.1s low + 0.1s high
        else:
            LED.set_output(24,0)  # Off the LED
            time.sleep(0.1)  # Add a delay to reduce the frequency of checking the slide switch.

if __name__=="__main__":
    main()