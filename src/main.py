from src.sensor import EntrySensor, ExitSensor
from src.detector import TkDetector
from src.car_park import CarPark
from src.display import TkDisplay


if __name__ == "__main__":
    car_park = CarPark("Moondaloop", 100)

    entry_sensor = EntrySensor(1, True, car_park)
    exit_sensor = ExitSensor(2, True, car_park)

    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    detector = TkDetector(entry_sensor, exit_sensor)

    display = TkDisplay("Moondaloop Display", 1, car_park)
    car_park.register(display)

    detector.start_sensing()
    display.show()
