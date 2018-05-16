"""
This module contains all the functions and classes to create and run weather application.
"""

import sys

from PyQt5 import QtGui, QtWidgets

import supertool.weather_window as ww
from supertool.weather import get_weather, get_five_day_forecast
from supertool.io_redirect import StdOutRedirector


class MainApplication(QtWidgets.QMainWindow):
    """
    Instances of this class will be weather applications.
    """
    def __init__(self):
        """
        Constructor of class MainApplication.
        """
        super(MainApplication, self).__init__()
        self.ui = ww.WeatherUIMainWindow()
        self.ui.setupUi(self)
        self.ui.button_forecast.clicked.connect(self.forecast_pressed)
        self.ui.button_weather.clicked.connect(self.weather_pressed)

    def forecast_pressed(self):
        """
        This method is called when the button '5-day forecast' is pressed. It displays the 5-day forecast in the
        ui.table.
        """
        self.ui.table.clear()
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        appid = "fae8fb5c89bba98d73b24e12cb1c2eae"
        with StdOutRedirector():
            forecast = get_five_day_forecast(url, self.ui.address.displayText(), appid)
        if forecast:
            n_lines = 1 + len(forecast)
            self.ui.table.setColumnCount(6)
            self.ui.table.setRowCount(n_lines)
            self.ui.table.setHorizontalHeaderLabels(
                ['Date', 'Sky', 'Temperature', 'Pressure', 'Humidity', 'Wind speed'])
            line = 1
            for date in forecast:
                self.ui.table.setItem(line, 0, QtWidgets.QTableWidgetItem(date))
                self.ui.table.setItem(line, 1, QtWidgets.QTableWidgetItem(forecast[date][0]))
                self.ui.table.setItem(line, 2, QtWidgets.QTableWidgetItem(str(forecast[date][1]) + " °C"))
                self.ui.table.setItem(line, 3, QtWidgets.QTableWidgetItem(str(forecast[date][2]) + " mm Hg"))
                self.ui.table.setItem(line, 4, QtWidgets.QTableWidgetItem(str(forecast[date][3]) + '%'))
                self.ui.table.setItem(line, 5, QtWidgets.QTableWidgetItem(str(forecast[date][4]) + ' m/s'))
                line += 1
            self.ui.table.resizeColumnsToContents()
            self.ui.table.resizeRowsToContents()
        else:
            self.ui.table.setColumnCount(1)
            self.ui.table.setRowCount(0)
            self.ui.table.setHorizontalHeaderLabels(['Wrong address!'])

    def weather_pressed(self):
        """
        This method is called when the button 'Current weather' is pressed. It displays the current weather in the
        ui.table.
        """
        self.ui.table.clear()
        url = 'http://api.openweathermap.org/data/2.5/weather'
        appid = "fae8fb5c89bba98d73b24e12cb1c2eae"
        with StdOutRedirector():
            weather = get_weather(url, self.ui.address.displayText(), appid)
        if weather:
            self.ui.table.setColumnCount(5)
            self.ui.table.setRowCount(2)
            self.ui.table.setHorizontalHeaderLabels(
                ['Sky', 'Temperature', 'Pressure', 'Humidity', 'Wind speed'])
            self.ui.table.setItem(1, 0, QtWidgets.QTableWidgetItem(weather['weather'][0]['description']))
            self.ui.table.setItem(1, 1, QtWidgets.QTableWidgetItem(str(round(weather['main']['temp'] - 274)) + " °C"))
            self.ui.table.setItem(1, 2, QtWidgets.QTableWidgetItem(str(round(weather['main']['pressure'] * 0.750062))
                                                                   + " mm Hg"))
            self.ui.table.setItem(1, 3, QtWidgets.QTableWidgetItem(str(weather['main']['humidity']) + '%'))
            self.ui.table.setItem(1, 4, QtWidgets.QTableWidgetItem(str(weather['wind']['speed']) + ' m/s'))
        else:
            self.ui.table.setColumnCount(1)
            self.ui.table.setRowCount(0)
            self.ui.table.setHorizontalHeaderLabels(['Wrong address!'])


def run_weather_app():
    """
    This function runs an instance of class MainWindow (the weather application).
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())
