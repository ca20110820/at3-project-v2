from src.sensor import EntrySensor, ExitSensor
from src.car_park import CarPark
from src.display import Display


def main():
    car_park = CarPark("Moondaloop", 5)

    entry_sensor = EntrySensor(1, True, car_park)
    exit_sensor = ExitSensor(2, True, car_park)

    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    display = Display(1, car_park, message="Display1", is_on=True)
    car_park.register(display)

    exit_sensor.detect_car()

    entry_sensor.detect_car()
    entry_sensor.detect_car()

    exit_sensor.detect_car()
    assert car_park.available_bays == 4
    assert car_park.num_plates == 1

    exit_sensor.detect_car()
    assert car_park.available_bays == 5
    assert car_park.num_plates == 0

    exit_sensor.detect_car()
    exit_sensor.detect_car()

    entry_sensor.detect_car()
    entry_sensor.detect_car()
    entry_sensor.detect_car()
    entry_sensor.detect_car()
    entry_sensor.detect_car()
    assert car_park.available_bays == 0
    assert car_park.num_plates == 5

    entry_sensor.detect_car()
    assert car_park.available_bays == 0
    assert car_park.num_plates == 6


if __name__ == "__main__":
    main()
