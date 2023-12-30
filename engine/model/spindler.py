class Spindler:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date  # Make sure this is a date object
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        service_threshold_mileage = self.last_service_mileage + 3 * 365  # Assuming an average of 365 miles per year
        return self.current_mileage >= service_threshold_mileage
