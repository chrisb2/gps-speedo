"""Main program of GPS speedometer."""
import screen
import machine
import utime

s = screen.Screen()
s.update(6.5)

utime.sleep_ms(20000)
machine.deepsleep(20000)
