from sqlalchemy import create_engine

connection_string = "postgresql://postgres.hquzysqzmuctivjhddyz:Zwanenveld52-23@aws-0-eu-north-1.pooler.supabase.com:6543/postgres"

try:
    engine = create_engine(connection_string)

    with engine.connect() as conn:
        print("Connected successfully!")

except Exception as e:
    print("ERROR:")
    print(e)