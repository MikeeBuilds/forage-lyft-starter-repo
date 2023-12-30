import sys
print(sys.path)

import unittest
from datetime import datetime, date
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.model.spindler import Spindler
from engine.car_factory import CarFactory

class TestCar(unittest.TestCase):
    def test_calliope_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_palindrome_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = True

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_rorschach_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
    def test_spindler_battery_needs_service(self):  
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 40000
        last_service_mileage = 0

        car = Spindler(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())


    def test_carrigan_tire_needs_service(self):  
        tire_wear_array = [0.1, 0.3, 0.5, 0.95]
        car = CarFactory.create_car("Spindler", "2023-01-01", 50000, 45000)
        self.assertTrue(car.needs_service())

    def test_octoprime_tire_needs_service(self):  
        tire_wear_array = [0.8, 0.9, 0.5, 0.7]
        car = CarFactory.create_car("Spindler", "2023-01-01", 50000, 45000)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()
