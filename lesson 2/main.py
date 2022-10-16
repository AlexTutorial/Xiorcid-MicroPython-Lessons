# from machine import Pin
# led = Pin(4, Pin.OUT)
# button = Pin(12, Pin.IN, Pin.PULL_UP)
# while True:
#     if button.value():
#         led.value(0)
#     else:
#         led.value(1)
#
from machine import Pin, PWM
from time import sleep
led = PWM(Pin(4), freq=500, duty=512)
button = Pin(12, Pin.IN, Pin.PULL_UP)
flag = False
while True:
    val = button.value()
    if not val:
        sleep(0.05)
        if val != button.value():
            flag = not flag
    if flag:
        led.duty(512)
    else:
        led.duty(10232)
