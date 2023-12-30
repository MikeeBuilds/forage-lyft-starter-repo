from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        
        @abstractmethod
        def engine_should_service(self):
            pass