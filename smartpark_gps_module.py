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
for x in jsonstuff['carparks']:
    print(x, end="\n\n\n\n\n")
#print(jsonstuff['carparks'][0])
# for x in jsonstuff['carparks']:
#     print(x['address'])
# print(len(jsonstuff['carparks']))

