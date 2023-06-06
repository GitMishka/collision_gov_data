import pandas as pd
import psycopg2
import io
from google.colab import files
from sqlalchemy import create_engine
import config

uploaded = files.upload()

dataset_file = next(iter(uploaded))

df = pd.read_csv(io.BytesIO(uploaded[dataset_file]))

df.columns = df.columns.str.replace(' ', '_')

table_name = 'motor_vehicle_collisions'

engine = config.creds

df.to_sql(table_name, engine, if_exists='replace', index=False)
