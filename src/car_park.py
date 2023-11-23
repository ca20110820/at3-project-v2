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

        self.location = location
        self.sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self.capacity = capacity  # Constant Value
        self.plates = plates or []
        self.displays = displays or []

    @property
    def available_bays(self):
        if len(self.plates) <= self.capacity:
            return self.capacity - len(self.plates)
        else:
            return 0

    def __str__(self):
        # Return a string containing the car park's location and capacity
        return f"Car Park at {self.location}, with {self.capacity} bays."

    def register(self, obj: Sensor | Display):
        if isinstance(obj, Sensor):
            self.sensors.append(obj)
        elif isinstance(obj, Display):
            self.displays.append(obj)
        else:
            raise TypeError(f"Object must either be Sensor or Display.")

    def add_car(self, plate: str):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        self.plates.remove(plate)
        # self.plates = [p for p in self.plates if p != plate]
        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update()
            print(f"Updating {display} ...")
