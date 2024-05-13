from hal import hal_input_switch as switch
from hal import hal_led as led
import time
from time import sleep

def main():
    n = 0 
    i = 1
    switch.init()
    led.init()
    switchlevel = switch.read_slide_switch()
    led.set_output (0,0)
    while True:
        if switchlevel==1:
            led.set_output(0,1)
            time.sleep(2)
            led.set_output(0,0)
            time.sleep(2)

        else:
            led.set_output(0,1)
            time.sleep(1)
            led.set_output(0,0)
            time.sleep(1)

        switchlevel = switch.read_slide_switch()

    

    




if __name__ == "__main__":
    main()
