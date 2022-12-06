from machine import Pin
import time

led = Pin(15, Pin.OUT)
led_25 = Pin(25, Pin.OUT)

while 1:
    led_25.off()
    led.on()
    time.sleep_ms(1000)
    led_25.on()
    led.off()
    time.sleep_ms(1000)