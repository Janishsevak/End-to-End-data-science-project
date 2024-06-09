import os
import sys
from src.exception.exception import CustomException
from src.logger.logging import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

import pickle
import numpy as np

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("reading sql database started")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("connection establised",mydb)

        df = pd.read_sql_query("select * from student",mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e)
