"""GPS speedometer screen."""
from machine import I2C
import utime
import ssd1306
from writer import Writer
# Font
import fullheight_bold
import config


class Screen:
    """GPS speedometer screen.

    Data sheet: https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf
    """

    def __init__(self):
        """Create with the configuration."""
        self._enable_display(config.rst)

        i2c = I2C(-1, config.scl, config.sda, freq=config.frequency)
        self._oled = ssd1306.SSD1306_I2C(config.width, config.height, i2c)
        self._writer = Writer(self._oled, fullheight_bold, verbose=False)

    def update(self, speed):
        """Update the displayed speed."""
        if speed >= 10:
            value = "{:.0f}".format(speed)
        else:
            value = "{:.1f}".format(speed)

        self._oled.fill(0)
        # Right justify
        len = self._writer.stringlen(value)
        self._writer.set_textpos(self._oled, 0, config.width - len)
        self._writer.printstring(value)
        self._oled.show()

    def _enable_display(self, resetPin):
        resetPin.off()
        # Minimum 3us, datasheet p27, Power ON and OFF sequence
        utime.sleep_us(5)
        resetPin.on()
