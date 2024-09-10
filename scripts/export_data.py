import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def export_to_database(df: pd.DataFrame, table_name: str) -> None:
    """
    Export the data to the specified table in the database.

    :param df: pd.DataFrame to be exported
    :param table_name: Name of the table to export the data
    :return: None
    """
    encoded_pass = quote_plus(DB_PASSWORD)
    url = f'postgresql://{DB_USER}:{encoded_pass}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(url)

    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data exported to {table_name} table successfully.")
    except Exception as e:
        print(f"Unable to export data to {table_name} table: {e}")
