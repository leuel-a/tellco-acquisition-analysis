#!/usr/bin/env ptyhon3

import os
from typing import Optional
from urllib.parse import quote_plus

import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def load_data_from_postgres(query: str) -> Optional[pd.DataFrame]:
    """Connects to the postgres database and loads the data based on
    the provided SQL query

    :param query: SQL query to load the data
    :type query: str

    :return: DataFrame containing the results of the query.
    """
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        df = pd.read_sql_query(query, connection)
        connection.close()

        return df
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None


def load_data_using_sqlalchemy(query: str) -> Optional[pd.DataFrame]:
    """Connects to the PostgresSQL database and loads data based on
    the provided SQL query using SQLAlchemy

    :param query: SQL query to execute.
    :return: DataFrame containing the results of the query
    """
    try:
        encoded_pass = quote_plus(DB_PASSWORD)
        conn_str = f'postgresql+psycopg2://{DB_USER}:{encoded_pass}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

        engine = create_engine(conn_str)
        df = pd.read_sql_query(query, engine)

        return df
    except Exception as e:
        print(f'Something went wrong: {e}')
        return None
