from abc import ABC, abstractmethod

from src.car_park import CarPark


class Sensor(ABC):

    car_park: CarPark

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    @abstractmethod
    def detect_car(self):
        pass


class EntrySensor(Sensor):
    def update_car_park(self, plate: str):
        pass

    def detect_car(self):
        pass


class ExitSensor(Sensor):
    def update_car_park(self, plate: str):
        pass

    def detect_car(self):
        pass
