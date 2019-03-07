"""Configuration file for GPS speedometer."""
from machine import Pin

# Display
frequency = 800000
scl = Pin(15)
sda = Pin(4)
rst = Pin(16, Pin.OUT)
width = 128
height = 64

# GPS
rx = 12
tx = 13
pps = Pin(14)
baudrate = 115200
