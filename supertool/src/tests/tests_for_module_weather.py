"""
This is a unittest test suite for the module weather.py.
"""

import sys
import unittest

from supertool.io_redirect import StdOutRedirector
from supertool.weather import print_weather, print_forecast


class PositiveTests(unittest.TestCase):
    def test_current_weather(self):
        with StdOutRedirector():
            print_weather('http://samples.openweathermap.org/data/2.5/weather', ['London'],
                          'fae8fb5c89bba98d73b24e12cb1c2eae')
            response = sys.stdout.getvalue()
            correct_response = 'Current weather in London :\nSky: clear sky\nTemperature: 12 °C\nPressure: 760 mm Hg\n' \
                               'Humidity: 100%\nWind speed: 5.52 m/s\n'
            self.assertEqual(response, correct_response)

    def test_five_day_forecast(self):
        with StdOutRedirector():
            print_forecast('http://samples.openweathermap.org/data/2.5/forecast', ['London'],
                           'fae8fb5c89bba98d73b24e12cb1c2eae')
            response = sys.stdout.getvalue()
            correct_response = '5-day forecast for London :\n' \
                               '   Date and time        Sky               Temperature  Pressure   Humidity   Wind speed 15\n' \
                               '2017-01-30 18:00:00  clear sky               10°C      763 mm Hg    100%      7.27 m/s\n' \
                               '2017-01-30 21:00:00  clear sky               9°C       765 mm Hg    100%      6.21 m/s\n' \
                               '2017-01-31 00:00:00  clear sky               8°C       767 mm Hg    100%      6.71 m/s\n' \
                               '2017-01-31 03:00:00  clear sky               8°C       768 mm Hg    100%      5.46 m/s\n' \
                               '2017-01-31 06:00:00  clear sky               9°C       768 mm Hg    100%      4.11 m/s\n' \
                               '2017-01-31 09:00:00  clear sky               9°C       769 mm Hg    100%      3.6 m/s\n' \
                               '2017-01-31 12:00:00  broken clouds           9°C       769 mm Hg    100%      3.37 m/s\n' \
                               '2017-01-31 15:00:00  scattered clouds        11°C      768 mm Hg    100%      3.32 m/s\n' \
                               '2017-01-31 18:00:00  clear sky               10°C      767 mm Hg    100%      4.26 m/s\n' \
                               '2017-01-31 21:00:00  clear sky               9°C       766 mm Hg    100%      4.32 m/s\n' \
                               '2017-02-01 00:00:00  few clouds              10°C      765 mm Hg    100%      10.16 m/s\n' \
                               '2017-02-01 03:00:00  clear sky               11°C      763 mm Hg    100%      13.76 m/s\n' \
                               '2017-02-01 06:00:00  few clouds              12°C      761 mm Hg    100%      12.75 m/s\n' \
                               '2017-02-01 09:00:00  clear sky               11°C      761 mm Hg    100%      12.33 m/s\n' \
                               '2017-02-01 12:00:00  clear sky               11°C      761 mm Hg    100%      12.21 m/s\n' \
                               '2017-02-01 15:00:00  clear sky               10°C      762 mm Hg    100%      12.21 m/s\n' \
                               '2017-02-01 18:00:00  clear sky               9°C       763 mm Hg    100%      9.3 m/s\n' \
                               '2017-02-01 21:00:00  clear sky               8°C       764 mm Hg    100%      8.91 m/s\n' \
                               '2017-02-02 00:00:00  clear sky               8°C       764 mm Hg    100%      9.15 m/s\n' \
                               '2017-02-02 03:00:00  clear sky               10°C      763 mm Hg    100%      8.95 m/s\n' \
                               '2017-02-02 06:00:00  clear sky               11°C      762 mm Hg    100%      7.56 m/s\n' \
                               '2017-02-02 09:00:00  clear sky               11°C      764 mm Hg    100%      8.31 m/s\n' \
                               '2017-02-02 12:00:00  clear sky               10°C      764 mm Hg    100%      8.87 m/s\n' \
                               '2017-02-02 15:00:00  clear sky               10°C      764 mm Hg    100%      8.73 m/s\n' \
                               '2017-02-02 18:00:00  clear sky               10°C      764 mm Hg    100%      7.8 m/s\n' \
                               '2017-02-02 21:00:00  clear sky               10°C      765 mm Hg    100%      5.92 m/s\n' \
                               '2017-02-03 00:00:00  clear sky               10°C      766 mm Hg    100%      1.83 m/s\n' \
                               '2017-02-03 03:00:00  clear sky               11°C      765 mm Hg    100%      1.01 m/s\n' \
                               '2017-02-03 06:00:00  clear sky               12°C      764 mm Hg    100%      0.71 m/s\n' \
                               '2017-02-03 09:00:00  clear sky               12°C      764 mm Hg    100%      1.51 m/s\n' \
                               '2017-02-03 12:00:00  clear sky               12°C      765 mm Hg    100%      3.68 m/s\n' \
                               '2017-02-03 15:00:00  clear sky               12°C      764 mm Hg    100%      3.36 m/s\n' \
                               '2017-02-03 18:00:00  clear sky               11°C      764 mm Hg    100%      1.66 m/s\n' \
                               '2017-02-03 21:00:00  clear sky               10°C      764 mm Hg    100%      3.77 m/s\n' \
                               '2017-02-04 00:00:00  clear sky               9°C       765 mm Hg    100%      2.91 m/s\n' \
                               '2017-02-04 03:00:00  clear sky               9°C       764 mm Hg    100%      0.22 m/s\n' \
                               '2017-02-04 06:00:00  clear sky               11°C      763 mm Hg    100%      1.88 m/s\n' \
                               '2017-02-04 09:00:00  few clouds              12°C      763 mm Hg    100%      3.02 m/s\n' \
                               '2017-02-04 12:00:00  scattered clouds        12°C      763 mm Hg    100%      3.77 m/s\n' \
                               '2017-02-04 15:00:00  scattered clouds        12°C      762 mm Hg    100%      2.97 m/s\n'
            self.assertEqual(response, correct_response)


class NegativeTests(unittest.TestCase):
    def test_wrong_address_in_weather(self):
        with StdOutRedirector():
            print_forecast('http://samples.openweathermap.org/data/2.5/weather', ['JKIDJBFHJsbafhjdsbdfjhBhbdhs'],
                           'fae8fb5c89bba98d73b24e12cb1c2eae')
            response = sys.stdout.getvalue()
            self.assertEqual(response, 'Wrong address!\n')

    def test_wrong_address_in_forecast(self):
        with StdOutRedirector():
            print_forecast('http://samples.openweathermap.org/data/2.5/forecast', ['JKIDJBFHJsbafhjdsbdfjhBhbdhs'],
                           'fae8fb5c89bba98d73b24e12cb1c2eae')
            response = sys.stdout.getvalue()
            self.assertEqual(response, 'Wrong address!\n')


if __name__ == '__main__':
    unittest.main()
