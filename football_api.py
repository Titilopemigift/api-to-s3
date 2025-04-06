import logging
import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

secret_key = os.getenv("MY_SECRET_KEY")
access_key = os.getenv("MY_ACCESS_KEY")
region_key = os.getenv("REGION_KEY")

# s3 Bucket details
s3_bucket = 'titilope-bucket'
s3_folder = 'football_api'
s3_filename = 'football'

s3_path = f"s3://{s3_bucket}/{s3_folder}/{s3_filename}"


# Fetch data from API
response = requests.get('http://api.football-data.org/v4/competitions/')

if response.status_code == 200:
    data = response.json()
    result = data["competitions"]
    result
else:
    print("Error: Unable to fetch data from the API")

competition_names = [item["name"] for item in data]

# convert to dataframe
df_football = pd.DataFrame(competition_names)

df_football.columns = df_football.columns.astype(str)


session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
# Upload dataframe as a parquet file to S3
wr.s3.to_parquet(
    df_football, path=s3_path,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)


logging.info(f"Data successfully uploaded to {s3_path}")
