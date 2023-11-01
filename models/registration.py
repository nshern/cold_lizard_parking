from datetime import datetime

import pandas as pd


class Registration:
    def __init__(self, license_plate, phone_number, email, parkingspot_id):
        self.license_plate = license_plate
        self.phone_number = phone_number
        self.email = email
        self.parkingspot_id = parkingspot_id
        self.time_of_registration = datetime.now()
        self.update_overview()

    def update_overview(self):
        path = "../parking_overview.csv"
        overview = pd.read_csv(path)
        new_data = pd.DataFrame(
            [
                [
                    self.license_plate,
                    self.phone_number,
                    self.email,
                    self.parkingspot_id,
                    self.time_of_registration,
                ]
            ],
            columns=[
                "license_plate",
                "phone_number",
                "email",
                "parkingspot_id",
                "time_of_registration",
            ],
        )
        # overview = overview.append(new_data, ignore_index=True)
        # overview.to_csv("../parking_overview.csv", index=False)
        frames = [overview, new_data]
        res = pd.concat(frames)
        res.to_csv(path, index=False)
        print(res)
        # pd.concat(overview, new_data)
        # print(overview)


if __name__ == "__main__":
    r = Registration(
        license_plate="13ty",
        phone_number="1234567",
        email="test@test.dk",
        parkingspot_id=5,
    )
