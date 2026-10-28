CREATE TABLE flight_states (
    id BIGSERIAL PRIMARY KEY,
    collected_at TIMESTAMP DEFAULT NOW(),

    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),

    latitude NUMERIC,
    longitude NUMERIC,

    altitude NUMERIC,
    velocity NUMERIC,
    heading NUMERIC
);