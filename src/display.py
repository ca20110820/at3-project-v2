from pprint import pprint


class Display:
    def __init__(self,
                 id,
                 car_park,
                 message="",
                 is_on=False
                 ):
        self._id = id
        self._message = message
        self._is_on = is_on
        self._car_park = car_park

    def __str__(self):
        return f"Display {self._id} is {'ON' if self._is_on else 'OFF'}"

    def update(self, data: dict) -> None:
        # Time:int, AvailableBays:int, Temperature: float
        pprint(data)
