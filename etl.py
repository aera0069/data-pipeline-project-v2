import pandas as pd
from sqlalchemy import create_engine
from faker import Faker

fake = Faker()
DB_URL = "postgresql://user:password@postgres:5432/sales_db"

def generate_data(n=100):
    return pd.DataFrame([{
        "order_id": fake.uuid4(),
        "date": fake.date_this_year(),
        "customer": fake.name(),
        "amount": round(fake.random_number(digits=3), 2)
    } for _ in range(n)])

def main():
    df = generate_data()
    engine = create_engine(DB_URL)
    df.to_sql("sales_raw", engine, if_exists="replace", index=False)
    print("Data loaded!")

if __name__ == "__main__":
    main()
