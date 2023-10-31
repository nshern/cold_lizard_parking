from datetime import datetime

import pandas as pd

overview = pd.read_csv("../parking_overview.csv")
print(overview)


class Registration:
    def __init__(self, license_plate, phone_number, email, parkingspot_id):
        self.license_plate = license_plate
        self.phone_number = phone_number
        self.email = email
        self.parkingspot_id = parkingspot_id
        self.time_of_registration = datetime.now()
