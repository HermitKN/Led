from machine import Pin
import time

led = Pin(15, Pin.OUT)
led_25 = Pin(25, Pin.OUT)

arreglo = "101000101"

for i in arreglo:
    if(i == "1"):
        led.on()
        time.sleep_ms(1000)
        led.off()
        time.sleep_ms(500)
    else:
        led_25.on()
        time.sleep_ms(1000)
        led_25.off()
        time.sleep_ms(500)
