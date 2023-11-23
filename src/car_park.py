
class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None
                 ):

        self.location = location
        self.sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self.capacity = capacity  # Is this the Constant Value or Changing State (available bays)?
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        # Return a string containing the car park's location and capacity
        return f"Car Park at {self.location}, with N bays."

    def register(self, obj):
        ...

    def add_car(self, plate: str):
        ...

    def remove_car(self, plate: str):
        ...

    def update_display(self):
        ...
