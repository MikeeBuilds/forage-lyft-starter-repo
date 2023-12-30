from abc import ABC

from engine import Engine
from vehicle import Vehicle

class SternmanEngine(Engine, Vehicle, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
