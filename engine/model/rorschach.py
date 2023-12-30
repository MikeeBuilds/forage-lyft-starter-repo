from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from vehicle import Vehicle


class Rorschach(WilloughbyEngine, Vehicle):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_service():
            return True
        else:
            return False
