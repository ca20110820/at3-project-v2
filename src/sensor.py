from abc import ABC, abstractmethod

from src.car_park import CarPark


class Sensor(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    def detect_car(self):
        pass

    def _scan_plate(self) -> str:
        # Random Plate Generator
        return f""


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
