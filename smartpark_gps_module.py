"""
Main backend file for SmartPark project.
Created by:
Yosef Leibman
Abhishek Kapoor
Sultan Sidhu
for TD Bank Elevate Hackathon, 22 September 2018.
"""
from gmaps import Geocoding
from json import JSONDecoder
import json

instance = Geocoding(api_key="<your api key>")  # todo: read api key from a txt file.
file = open("/Users/sultansidhu/Desktop/DataFiles/greenPParking2015.json")
stuff = file.read()
jsonstuff = json.loads(stuff)
# for x in jsonstuff['carparks']:
#     print(x, end="\n\n\n\n\n")


class ParkingClass:

    def __init__(self, location: tuple, address: str, rate_per_half_hour: float, capacity: int):
        """
        Creates a new Parking object
        """
        self.location = location
        self.address = address
        self.rate_per_hour = rate_per_half_hour
        self.capacity = capacity
        self.proximity_rating = 0
        self.rph_rating = 0
        self.payment_options = []

    def __str__(self) -> str:
        """
        Returns a String representation of this Parking object
        """
        return "Latitude: {}, Longitude: {}, Address: {}, Rate: {}, Capacity: {}, Payment Options: {}".format(self.location[0],
                                                                           self.location[1],
                                                                           self.address,
                                                                           self.rate_per_hour,
                                                                           self.capacity,
                                                                           self.payment_options)

    def getLocationTuple(self) -> tuple:
        """
        Returns a tuple containing two floats representing the latitude and longitude of this parking
        """
        return self.location

    def setPaymentOptions(self, payment_option_list):
        """Sets the payment options for a specific object."""
        self.payment_options = payment_option_list


def createParkingArray(jason):
    """Creates an array of all parking objects."""
    parkingArray = []
    for i in range(len(jason['carparks'])):
        address = jason['carparks'][i]['address']
        lattitude = jason['carparks'][i]['lat']
        longitude = jason['carparks'][i]['lng']
        rate = jason['carparks'][i]['rate_half_hour']
        capacity = jason['carparks'][i]['capacity']
        new_object = ParkingClass((lattitude, longitude), address, rate, capacity)
        new_object.setPaymentOptions(jason['carparks'][i]['payment_options'])
        parkingArray.append(new_object)
    return parkingArray

thestuff = createParkingArray(jsonstuff)
print(len(thestuff))
for x in thestuff:
    print(x, end="\n\n")
