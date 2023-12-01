from typing import List
from pathlib import Path
import json

from src.sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark
from src.display import Display, TkDisplay


class Config:
    # Note: One json file only represent one instance of CarPark.
    def __init__(self, config_path: str | Path, display_type):
        if not isinstance(config_path, (str, Path)):
            raise TypeError("Configuration Path must be a valid string or pathlib.Path")

        self._config_path = str(config_path)

        self._display_type = display_type

        self._car_park: CarPark | None = None
        self._sensors: List[Sensor] = []
        self._displays: List[Display] = []

        self._create_initial_car_park()
        self._create_sensors()
        self._create_displays()

    @property
    def car_park(self):
        return self._car_park

    @property
    def sensors(self):
        return self._sensors

    @property
    def displays(self):
        return self._displays

    def _create_initial_car_park(self) -> None:
        """Creates Car Park with No Plates, Sensors, or Displays"""
        with open(self._config_path, 'r') as file:
            conf_dict = json.load(file)

        self._car_park = CarPark(conf_dict['location'], conf_dict['capacity'])

    def _create_sensors(self) -> None:
        with open(self._config_path, 'r') as file:
            conf_dict = json.load(file)
            conf_sensors = conf_dict['sensors']

        for conf_sensor in conf_sensors:
            if conf_sensor['type'] == 'entry':
                self._sensors.append(EntrySensor(conf_sensor['id'], conf_sensor['is_active'], self._car_park))

            elif conf_sensor['type'] == 'exit':
                self._sensors.append(ExitSensor(conf_sensor['id'], conf_sensor['is_active'], self._car_park))

    def _create_displays(self) -> None:
        with open(self._config_path, 'r') as file:
            conf_dict = json.load(file)
            conf_displays: List[dict] = conf_dict['displays']

        for conf_display in conf_displays:
            max_len = conf_display.get('max_len')

            temp_display = \
                self._display_type(conf_display['id'],
                                   self._car_park,
                                   is_on=conf_display['is_on'],
                                   max_len=max_len if max_len is not None else 100
                                   )

            self._displays.append(temp_display)


if __name__ == "__main__":
    # Example
    Config(Path(__file__).resolve().parent / 'sample_config.json', Display)
