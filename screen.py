"""GPS speedometer screen."""
from machine import I2C
import utime
import ssd1306
from writer import Writer
# Font
import fullheight_bold
import config


class Screen:
    """GPS speedometer screen."""

    def __init__(self):
        """Create with the configuration."""
        self._enable_display(config.rst)

        i2c = I2C(-1, config.scl, config.sda, freq=config.frequency)
        self._oled = ssd1306.SSD1306_I2C(config.width, config.height, i2c)
        self._writer = Writer(self._oled, fullheight_bold, verbose=False)

    def update(self, speed):
        """Update the displayed speed."""
        value = str(speed)  # TODO format 1dp if < 10
        len = self._writer.stringlen(value)
        Writer.set_textpos(self._oled, 0, config.width - len)

        self._oled.fill(0)
        self._writer.printstring(value)
        self._oled.show()

    def _enable_display(self, resetPin):
        resetPin.off()
        utime.sleep_ms(50)
        resetPin.on()
