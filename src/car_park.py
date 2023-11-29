import random
from datetime import datetime

from src.sensor import Sensor
from src.display import Display


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 sensors=None,
                 displays=None
                 ):

        if capacity < 1:
            raise ValueError("Capacity cannot be less than 1!")

        self._location = location
        self._sensors = sensors or []  # Composition (typically instantiated inside)
        self._capacity = capacity  # Constant Value
        self._plates = plates or []
        self._displays = displays or []  # Aggregation (typically instantiated outside)

        self._time_func = lambda: datetime.now()  # Default Time Generator
        self._temperature_func = lambda: random.randint(20, 30)  # Default Temperature Generator

    @property
    def location(self):
        return self._location
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def sensors(self):
        return self._sensors

    @property
    def displays(self):
        return self._displays
    
    @property
    def available_bays(self):
        return max(0, self._capacity - self.num_plates)
    
    @property
    def plates(self):
        return self._plates
    
    @property
    def num_plates(self):
        return len(self._plates)

    @property
    def temperature(self):
        return self._temperature_func()

    @temperature.setter
    def temperature(self, func):
        self._temperature_func = func

    @property
    def time(self):
        return self._time_func()

    @time.setter
    def time(self, func):
        self._time_func = func
    
    def __str__(self):
        # Return a string containing the car park's location and capacity
        return f"Car Park at {self._location}, with {self._capacity} bays."

    def register(self, obj: Sensor | Display):
        if not isinstance(obj, (Sensor, Display)):
            raise TypeError("Object must either be Sensor or Display.")

        if isinstance(obj, Sensor):
            assert obj.car_park == self, "The object have different car park!"
            self._sensors.append(obj)
        elif isinstance(obj, Display):
            self._displays.append(obj)

    def add_car(self, plate: str):
        self._plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        self._plates.remove(plate)
        # self.plates = [p for p in self.plates if p != plate]
        self.update_displays()

    def update_displays(self):
        if self.temperature is None or self.time is None:
            raise ValueError("Temperature or Time is None! It needs to be updated & modified.")

        data = {'temperature': self.temperature,
                'time': self.time,
                'available_bays': self.available_bays,
                'num_plates': self.num_plates
                }

        for display in self._displays:
            display.update(data)
