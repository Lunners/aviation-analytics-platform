import requests
import pandas as pd
from sqlalchemy import create_engine

# Supabase connection
connection_string = "postgresql://postgres.hquzysqzmuctivjhddyz:Zwanenveld52-23@aws-0-eu-north-1.pooler.supabase.com:6543/postgres"

engine = create_engine(connection_string)

# OpenSky API
url = "https://opensky-network.org/api/states/all"

response = requests.get(url)

data = response.json()

states = data["states"]

records = []

for aircraft in states[:100]:  # Start with first 100 records
    records.append({
        "icao24": aircraft[0],
        "callsign": aircraft[1],
        "origin_country": aircraft[2],
        "longitude": aircraft[5],
        "latitude": aircraft[6],
        "altitude": aircraft[7],
        "velocity": aircraft[9],
        "heading": aircraft[10]
    })

df = pd.DataFrame(records)

df.to_sql(
    "flight_states",
    engine,
    if_exists="append",
    index=False
)

print(f"Inserted {len(df)} records")