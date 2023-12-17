import unittest

from smartpark.car_park import CarPark
from smartpark.sensor import Sensor, EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):
    def setUp(self) -> None:
        self.car_park = CarPark("123 Example Street", 100)

        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_register_sensor(self):
        self.assertIn(self.entry_sensor, self.car_park.sensors)
        self.assertIn(self.exit_sensor, self.car_park.sensors)
        self.assertEqual(len(self.car_park.sensors), 2)

    def test_sensor_initialization(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_entry_update_car_park(self):
        self.entry_sensor.detect_car()
        self.assertEqual(self.car_park.available_bays, 99)
        self.assertEqual(self.car_park.num_plates, 1)

        self.entry_sensor.detect_car()
        self.assertEqual(self.car_park.available_bays, 98)
        self.assertEqual(self.car_park.num_plates, 2)

    def test_exit_update_car_park(self):
        self.entry_sensor.detect_car()
        self.assertEqual(self.car_park.available_bays, 99)
        self.assertEqual(self.car_park.num_plates, 1)

        self.exit_sensor.detect_car()
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.num_plates, 0)

    def test_overfill_the_car_park(self):
        for _ in range(100):
            self.entry_sensor.detect_car()

        self.assertEqual(self.car_park.available_bays, 0)
        self.assertEqual(self.car_park.num_plates, 100)

        self.entry_sensor.detect_car()
        self.assertEqual(self.car_park.available_bays, 0)
        self.assertEqual(self.car_park.num_plates, 101)

    def test_removing_a_car_that_does_not_exist(self):
        self.exit_sensor.detect_car()

        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.num_plates, 0)
        self.assertIsNone(self.exit_sensor.scan_plate())


if __name__ == "__main__":
    unittest.main()
