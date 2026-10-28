import requests

url = "https://opensky-network.org/api/states/all"

response = requests.get(url)

data = response.json()

first_aircraft = data["states"][0]

print(first_aircraft)
