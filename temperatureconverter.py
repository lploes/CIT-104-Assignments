"""
File: temperatureconverter.py
A GUI program that converts temperatures between degrees
Fahrenheit and degrees Celsius.
"""

from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """The  window for the temperature converter."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Temperature Converter")

        # Row 0: the labels
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel (text="Celsius", row=0, column=1)

        # Row 1: the entry fields (they start out at 32.0 and 0.0)
        self.fahrenheitField = self.addFloatField(value=32.0, row=1, column=0,
                                                  precision=2)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=1,
                                               precision=2)

        # Row 2: the command buttons
        self.addButton(text=">>>>", row=2, column=0,
                       command=self.computeCelsius)
        self.addButton(text="<<<<", row=2, column=1,
                       command=self.computeFahrenheit)

    def computeCelsius(self):
        """Gets Fahrenheit from its field, converts it, and
        puts the answer in the Celsius field."""
        fahrenheit = self.fahrenheitField.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)

    def computeFahrenheit(self):
        """Gets Celsius from its field, converts it, and
        puts the answer in the Fahrenheit field."""
        celsius = self.celsiusField.getNumber()
        fahrenheit = celsius * 9 / 5 + 32
        self.fahrenheitField.setNumber(fahrenheit)


def main():
    """Creates the window and starts the program."""
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()