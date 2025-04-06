import logging
import os

import awswrangler as wr
import boto3
import pandas as pd
from dotenv import load_dotenv
from utils import response

# Load environment variables from .env file
load_dotenv()

secret_key = os.getenv("MY_SECRET_KEY")
access_key = os.getenv("MY_ACCESS_KEY")
region_key = os.getenv("REGION_KEY")

# s3 Bucket details
s3_bucket = 'titilope-bucket'
s3_folder = 'job_api'
s3_filename = 'senior_role'
s3_filename2 = 'manager_role'

s3_path = f"s3://{s3_bucket}/{s3_folder}/{s3_filename}"
s3_path2 = f"s3://{s3_bucket}/{s3_folder}/{s3_filename2}"


# Fetch data from API
response.keys()

jobs = response["jobs"]

jobtitle = [item["jobTitle"]for item in jobs]


senior_role = []
manager_role = []

for job in jobtitle:
    if "Senior" in job:
        senior_role.append(job)
    if "Manager" in job:
        manager_role.append(job)

# convert to dataframe
df_senior = pd.DataFrame(senior_role)
df_manager = pd.DataFrame(manager_role)


df_senior.columns = df_senior.columns.astype(str)
df_manager.columns = df_manager.columns.astype(str)


session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
# Upload dataframe as a parquet file to s3
wr.s3.to_parquet(
    df_senior,
    path=s3_path,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)

wr.s3.to_parquet(
    df_manager,
    path=s3_path2,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)


logging.info(f"Data successfully uploaded to {s3_path}")
logging.info(f"Data successfully uploaded to {s3_path2}")
