"""Main program of GPS speedometer."""
import screen
import machine

s = screen.Screen()
s.update(6.5)

machine.deepsleep(5000)
