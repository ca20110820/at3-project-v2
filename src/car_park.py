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

        self._location = location
        self._sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self._capacity = capacity  # Constant Value
        self._plates = plates or []
        self._displays = displays or []

    @property
    def available_bays(self):
        if len(self._plates) <= self._capacity:
            return self._capacity - len(self._plates)
        else:
            return 0
    
    @property
    def plates(self):
        return self._plates
    
    def __str__(self):
        # Return a string containing the car park's location and capacity
        return f"Car Park at {self._location}, with {self._capacity} bays."

    def register(self, obj: Sensor | Display):
        if isinstance(obj, Sensor):
            self._sensors.append(obj)
        elif isinstance(obj, Display):
            self._displays.append(obj)
        else:
            raise TypeError(f"Object must either be Sensor or Display.")

    def add_car(self, plate: str):
        self._plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        self._plates.remove(plate)
        # self.plates = [p for p in self.plates if p != plate]
        self.update_displays()

    def update_displays(self):
        for display in self._displays:
            display.update()
            print(f"Updating {display} ...")
