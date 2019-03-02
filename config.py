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
rx = Pin(12)
tx = Pin(13)
