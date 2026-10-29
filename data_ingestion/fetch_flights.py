import requests

url = "https://opensky-network.org/api/states/all"

response = requests.get(url)

data = response.json()

aircraft = data["states"][0]

print("ICAO24:", aircraft[0])
print("Callsign:", aircraft[1])
print("Country:", aircraft[2])
print("Longitude:", aircraft[5])
print("Latitude:", aircraft[6])
print("Altitude:", aircraft[7])
print("Velocity:", aircraft[9])