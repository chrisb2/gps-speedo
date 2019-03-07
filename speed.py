"""GPS speedometer program."""
import machine
from micropyGPS import MicropyGPS
from machine import UART
import screen
import utime
import config


def run():
    """Run the program."""
    uart = UART(1)
    uart.init(config.baudrate, bits=8, parity=None, stop=1,
              rx=config.rx, tx=config.tx)
    gps = MicropyGPS()
    s = screen.Screen()

    kph = None
    start = utime.ticks_ms()
    while kph is None and utime.ticks_diff(utime.ticks_ms(), start) < 1000:
        if uart.any():
            try:
                stat = gps.update(chr(uart.read(1)[0]))
            except:
                pass
            if stat == 'GNRMC':
                print(stat)
                kph = gps.speed[2]

    if kph is not None:
        s.update(kph)

    machine.deepsleep(5000)
