import pyfirmata
import time

board = pyfirmata.Arduino('/dev/usbmodem1201')
# usbmodem1201 it's my Mac port
it = pyfirmata.util.Iterator(board)
it.start()

analog_input_value = board.get_pin('a:0:i')
# board.get_pin('a:0:i') a-> analog pin, 0-> analog A0 pin, i->INPUT
# analog_input_value -> it's variable
led1 = board.get_pin('d:13:o')
# board.get_pin('d:13:o') d-> digital pin, 13-> digital 13 pin, o->OUTPUT
# led1 -> it's variable

while True:
    analog_pin_value = analog_input_value.read()
    if analog_pin_value is not None:
        delay = analog_pin_value + 0.01
        led1.write(1)
        time.sleep(delay)
        led1.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)