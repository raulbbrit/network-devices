from .device import BaseDevice
from dataclasses import dataclass, field

@dataclass(slots=True)
class Fiberhome(BaseDevice):
    __device_connect: None = field(init=False, repr=False)

    @property.getter
    def __device_connect(self) -> None:
        return self.__device_connect

    def connect_device(
        self, ip: str, username: str, \
        password: str) -> str:
        return "Connecting to Fiberhome device"

    def disconnect_device(self) -> str:
        return "Disconnecting from Fiberhome device"

    def send_command(self, command: str, \
                     expected_result: str) -> str:
        return "Sending command to Fiberhome device"
