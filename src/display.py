from collections import deque


class Display:
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

        self._data = deque(maxlen=max_len)

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

    def show(self, *args, **kwargs):
        """Override and Implement the Show method.

        This method could be used to define an event-loop for GUI application.
        """
        raise NotImplementedError()
