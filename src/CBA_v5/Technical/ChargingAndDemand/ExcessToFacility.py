from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ExcessToFacility(QObject):
    electricityPerDayChanged = Signal()
    electricityPerYearChanged = Signal()

    def __init__(self,
        # required
        electricity_per_day:float
    ):
        super().__init__()
        self._electricity_per_day = electricity_per_day
        self._electricity_per_year = electricity_per_day * 365

    @Property(str, notify=electricityPerDayChanged) #getter
    def electricityPerDay(self) -> str:
        return str(self._electricity_per_day)

    @electricityPerDay.setter
    def electricityPerDay(self, electricity_per_day:str):
        self._electricity_per_day = float(electricity_per_day)
        self._electricity_per_year = self._electricity_per_day * 365

    @Property(str, notify=electricityPerYearChanged) #getter
    def electricityPerYear(self) -> str:
        return str(self._electricity_per_year)

    @electricityPerYear.setter
    def electricityPerYear(self, electricity_per_year:str):
        self._electricity_per_year = float(electricity_per_year)