from abc import ABC, abstractmethod
import tkinter as tk

from smartpark.sensor import EntrySensor, ExitSensor


class Detector(ABC):
    @abstractmethod
    def start_sensing(self):
        pass


class TkDetector(Detector):
    def __init__(self, entry_sensor: EntrySensor, exit_sensor: ExitSensor):
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘', font=('Arial', 50), cursor='bottom_left_corner',
            command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.entry_sensor = entry_sensor
        self.exit_sensor = exit_sensor

    def start_sensing(self):
        self.root.mainloop()  # Blocking Thread

    def incoming_car(self):
        self.entry_sensor.detect_car()

    def outgoing_car(self):
        self.exit_sensor.detect_car()
