import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

connection_string = os.environ["DB_CONNECTION_STRING"]


def load_data():
    conn = pyodbc.connect(connection_string)
    data = pd.read_sql(
        "SELECT EMAIL, NAME, UID, BRANCH, SEM, COURSE, CATEGORY, PERIOD FROM ENROLMENTS",
        conn,
    )
    data.rename(columns=lambda x: x.lower(), inplace=True)
    data["branch"] = data["branch"].astype("category")
    data["course"] = data["course"].astype("category")
    data["category"] = data["category"].astype("category")
    data["period"] = data["period"].str[:-1]
    data["period"] = data["period"].astype("category")
    # print(data["period"].unique())
    return data


# def get_dataframes():
#     """Returns"""
#     df = load_data()
#     odd_sem_22_23 = df[df['period'] == 'ODD_SEM_22_23']
#     even_sem_22_23 = df[df['period'] == 'EVEN_SEM_22_23']
#     odd_sem_23_24 = df[df['period'] == 'ODD_SEM_23_24']
#     even_sem_23_24 = df[df['period'] == 'EVEN_SEM_23_24']
#     acad_year_22_23 = pd.concat(odd_sem_22_23, even_sem_22_23)
#     acad_year_23_24 = pd.concat(odd_sem_23_24, even_sem_23_24)
#     return df
