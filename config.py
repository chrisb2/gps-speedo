"""Configuration file for GPS speedometer."""
from machine import Pin

# Display
frequency = 100000
scl = Pin(15)
sda = Pin(4)
rst = Pin(16, Pin.OUT)
