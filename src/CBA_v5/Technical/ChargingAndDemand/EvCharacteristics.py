from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class EvCharacteristics(QObject):
    evBatteryVoltageChanged = Signal()
    capacityChanged = Signal()
    maxPowerRatingChanged = Signal()
    ampereHourRatingChanged = Signal()

    def __init__(self,
        # required
        ampere_hour_rating:float = 67.5,

        ev_battery_voltage:float = 800,
        capacity:float = 54,
        max_power_rating:float = 270
    ):
        super().__init__()
        self._ev_battery_voltage = ev_battery_voltage
        self._capacity = capacity
        self._max_power_rating = max_power_rating
        self._ampere_hour_rating = ampere_hour_rating

        self.capacityChanged.connect(self.updateAmpereHourRating)
        self.evBatteryVoltageChanged.connect(self.updateAmpereHourRating)

    def emitUpdateSignals(self):
        self.evBatteryVoltageChanged.emit()
        self.capacityChanged.emit()
        self.maxPowerRatingChanged.emit()
        self.ampereHourRatingChanged.emit()

    @Property(str, notify=evBatteryVoltageChanged) #getter
    def evBatteryVoltage(self) -> str:
        return str(self._ev_battery_voltage)

    @evBatteryVoltage.setter
    def evBatteryVoltage(self, ev_battery_voltage:str):
        self._ev_battery_voltage = float(ev_battery_voltage)
        self.evBatteryVoltageChanged.emit()

    @Property(str, notify=capacityChanged) #getter
    def capacity(self) -> str:
        return str(self._capacity)

    @capacity.setter
    def capacity(self, capacity:str):
        self._capacity = float(capacity)
        self.capacityChanged.emit()

    @Property(str, notify=maxPowerRatingChanged) #getter
    def maxPowerRating(self) -> str:
        return str(self._max_power_rating)

    @maxPowerRating.setter
    def maxPowerRating(self, max_power_rating:str):
        self._max_power_rating = float(max_power_rating)
        self.maxPowerRatingChanged.emit()
    
    @Property(str, notify=ampereHourRatingChanged) #getter
    def ampereHourRating(self) -> str:
        return str(self._ampere_hour_rating)

    @ampereHourRating.setter
    def ampereHourRating(self, ampere_hour_rating:str):
        self._ampere_hour_rating = float(ampere_hour_rating)
        self.ampereHourRatingChanged.emit()

    @Slot()
    def updateAmpereHourRating(self):
        self._ampere_hour_rating = (self._capacity / self._ev_battery_voltage) * 1000
        self.ampereHourRatingChanged.emit()