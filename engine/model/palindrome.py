from datetime import datetime

from engine.sternman_engine import SternmanEngine
from vehicle import Vehicle


class Palindrome(SternmanEngine, Vehicle):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_service():
            return True
        else:
            return False
