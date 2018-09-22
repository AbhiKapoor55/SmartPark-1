"""
Represents a Parking establishment, which contains the Parking's location, name, address, rate, and general ratings
based on the user's location
"""


class ParkingClass:

    def __init__(self, location: tuple, name: str, address: str, rate_per_half_hour: float):
        """
        Creates a new Parking object
        """
        self.location = location
        self.name = name
        self.address = address
        self.rate_per_hour = rate_per_half_hour

    def __str__(self) -> str:
        """
        Returns a String representation of this Parking object
        """
        return "Parking Name: {}, Latitude: {}, Longitude: {}, Address: {}, Rate: {}".format(self.name,
                                                                                             self.location[0],
                                                                                             self.location[1],
                                                                                             self.address,
                                                                                             self.rate_per_hour)

    def getLocationTuple(self) -> tuple:
        """
        Returns a tuple containing two floats representing the latitude and longitude of this parking
        """
        return self.location