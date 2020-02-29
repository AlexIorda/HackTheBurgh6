import json
import requests
with open ('api/ireland_atm.json') as f:
    atm_data = json.load(f)
lat = float(atm_data["data"]["Brand"][0]["ATM"][0]["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"])
long = float(atm_data["data"]["Brand"][0]["ATM"][0]["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Longitude"])

#print (lat,long)
#print(float(atm_data["data"]["Brand"][0]["ATM"][3]["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"]))


for atm in atm_data["data"]["Brand"][0]["ATM"]:
    lat_atm = atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"]
    long_atm = atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Longitude"]
    print(lat_atm,long_atm)

# printing current location
res = requests.get("https://ipinfo.io/")
loc_data = res.json()
print(loc_data["loc"])