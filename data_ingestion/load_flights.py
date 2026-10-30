import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Supabase Connection
connection_string = (
    "postgresql://postgres.hquzysqzmuctivjhddyz:"
    "Zwanenveld52-23"
    "@aws-0-eu-north-1.pooler.supabase.com:6543/postgres"
)

engine = create_engine(connection_string)

# OpenSky API
url = "https://opensky-network.org/api/states/all"

response = requests.get(url)
data = response.json()

states = data["states"]

records = []

for aircraft in states:

    # Skip records with missing coordinates
    if aircraft[5] is None or aircraft[6] is None:
        continue

    longitude = aircraft[5]
    latitude = aircraft[6]

    # Hong Kong area filter
    if (
        21.5 <= latitude <= 23.5
        and
        113.0 <= longitude <= 115.5
    ):

        records.append({
            "icao24": aircraft[0],
            "callsign": aircraft[1].strip() if aircraft[1] else None,
            "origin_country": aircraft[2],

	    "time_position": datetime.fromtimestamp(aircraft[3]) if aircraft[3] else None,
	    "last_contact": datetime.fromtimestamp(aircraft[4]) if aircraft[4] else None,

            "longitude": longitude,
            "latitude": latitude,

            "altitude": aircraft[7],
            "velocity": aircraft[9],
            "heading": aircraft[10]
        })

df = pd.DataFrame(records)

print(df.head())
print(f"Found {len(df)} flights near Hong Kong")

df.to_sql(
    "flight_states",
    engine,
    if_exists="append",
    index=False
)

print(f"Inserted {len(df)} records")