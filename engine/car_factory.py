from typing import List
from datetime import datetime, date
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.model.spindler import Spindler

class CarFactory:
    @staticmethod
    def create_car(car_type: str, *args):
        if car_type == "Calliope":
            return Calliope(datetime.today().date(), *args)  # Adjust parameters as needed
        elif car_type == "Glissade":
            return Glissade(datetime.today().date(), *args)  # Adjust parameters as needed
        elif car_type == "Palindrome":
            return Palindrome(datetime.today().date(), *args)  # Adjust parameters as needed
        elif car_type == "Rorschach":
            return Rorschach(datetime.today().date(), *args)  # Adjust parameters as needed
        elif car_type == "Thovex":
            return Thovex(datetime.today().date(), *args)  # Adjust parameters as needed
        elif car_type == "Spindler":
            if len(args) >= 3:
                last_service_date = datetime.strptime(args[0], "%Y-%m-%d").date()
                current_mileage = int(args[1])
                last_service_mileage = int(args[2])
                return Spindler(last_service_date, current_mileage, last_service_mileage)
            else:
                raise ValueError("Insufficient arguments for Spindler initialization")
        else:
            raise ValueError(f"Invalid car type: {car_type}")
