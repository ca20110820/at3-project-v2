from abc import ABC, abstractmethod
import random
import string


class Sensor(ABC):
    def __init__(self,
                 id,
                 is_active,
                 car_park
                 ):
        self._id = id
        self._is_active = is_active
        self._car_park = car_park
        self._car_park.register(self)

    @property
    def car_park(self):
        return self._car_park

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"id={self._id};is_active={self._is_active}"

    @abstractmethod
    def update_car_park(self, plate: str):
        pass

    def detect_car(self):
        plate = self.scan_plate()
        self.update_car_park(plate)

    @abstractmethod
    def scan_plate(self):
        # Random Plate Generator (Entry) or Selector (Exit)
        pass


class EntrySensor(Sensor):
    def update_car_park(self, plate: str):
        self.car_park.add_car(plate)

    def scan_plate(self) -> str:
        """Generate Random Plate for Entering Car"""
        format_string = random.choice(["LLL-NNN", "NLL-NNN", "NLLL-NNN", "LL-NNNN", "TAXI-NNNN", "LLL-NNNN"])

        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(format_string.count("L")))
        numbers = ''.join(random.choice(string.digits) for _ in range(format_string.count("N")))

        license_plate = format_string
        for char in format_string:
            if char == "L":
                license_plate = license_plate.replace(char, letters[0], 1)
                letters = letters[1:]
            elif char == "N":
                license_plate = license_plate.replace(char, numbers[0], 1)
                numbers = numbers[1:]

        return license_plate


class ExitSensor(Sensor):
    def update_car_park(self, plate: str):
        if plate is not None:
            self.car_park.remove_car(plate)
        else:
            print(f"No Cars in the {self.car_park}")

    def scan_plate(self) -> str | None:
        """Randomly Select Car to Exit, if exists."""
        return random.choice(self._car_park.plates) if len(self._car_park.plates) > 0 else None
