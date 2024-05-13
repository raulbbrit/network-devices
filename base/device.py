from abc import ABC, abstractmethod


class BaseDevice(ABC):
  def __init__(
    self,
    ip: str,
    username: str,
    password: str,
    version: str
    ):

    self.__ip = ip
    self.__username = username
    self.__password = password
    self.__version = version

  @abstractmethod
  def connect_device(self, ip: str, username: str, \
                     password: str) -> str:
    ...

  @abstractmethod
  def disconnect_device(self) -> str:
    ...

  @abstractmethod
  def send_command(self, command: str, \
    expected_result: str, version: str) -> str:
    ...