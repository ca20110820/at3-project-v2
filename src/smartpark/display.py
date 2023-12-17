from collections import deque
import tkinter as tk


class Display:

    fields = ['Temperature', 'Time', 'Available Bays', 'Num of Cars']

    def __init__(self,
                 id,
                 car_park,
                 message="",
                 is_on=False,
                 max_len=100,
                 ):
        self._id = id
        self._message = message
        self._is_on = is_on
        self._car_park = car_park
        self._car_park.register(self)

        self._data = deque(maxlen=max_len)

    @property
    def id(self):
        return self._id

    @property
    def is_on(self):
        return self._is_on

    @property
    def car_park(self):
        return self._car_park

    @property
    def latest_data(self):
        return self._data[-1] if self._data else None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def __str__(self):
        return f"Display {self._id} is {'ON' if self._is_on else 'OFF'}"

    def get_data(self) -> list:
        return list(self._data)

    def update(self, data: dict) -> None:
        # time: datetime, available_bays: int, temperature: float
        self._data.append(data)

        try:
            self._message = data['message']
        except KeyError:
            pass

    def show(self, *args, **kwargs):
        """Override and Implement the Show method.

        This method could be used to define an event-loop for GUI application.
        """
        raise NotImplementedError()


class TkDisplay(Display):

    DISPLAY_INIT = '– – – – – –'
    SEP = ':'  # field name separator

    def __init__(self, title: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = tk.Tk()
        self.window.title(f'{title}: Parking')
        self.window.geometry('1150x400')
        self.window.resizable(False, False)

        self.gui_elements = {}
        for i, field in enumerate(self.fields):
            # create the elements
            self.gui_elements[f'lbl_field_{i}'] = tk.Label(
                self.window, text=field + self.SEP, font=('Arial', 50))
            self.gui_elements[f'lbl_value_{i}'] = tk.Label(
                self.window, text=self.DISPLAY_INIT, font=('Arial', 50))

            # position the elements
            self.gui_elements[f'lbl_field_{i}'].grid(
                row=i, column=0, sticky=tk.E, padx=5, pady=5)
            self.gui_elements[f'lbl_value_{i}'].grid(
                row=i, column=2, sticky=tk.W, padx=10)

    def show(self):
        self.window.mainloop()

    def update(self, data: dict):
        """Update the values displayed in the GUI. Expects a dictionary with keys matching the field names
        passed to the constructor."""

        super().update(data)

        temp_data = {}
        for k, v in data.items():
            if k == "temperature":
                temp_data["Temperature"] = v
            elif k == "time":
                temp_data["Time"] = v.strftime('%Y-%m-%d %H:%M:%S')
            elif k == "available_bays":
                temp_data["Available Bays"] = v
            elif k == "num_plates":
                temp_data["Num of Cars"] = v
            else:
                raise KeyError(f"Key '{k}' does not exist!")

        for field in self.gui_elements:
            if field.startswith('lbl_field'):
                field_value = field.replace('field', 'value')
                self.gui_elements[field_value].configure(
                    text=temp_data[self.gui_elements[field].cget('text').rstrip(self.SEP)])
        self.window.update()
