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
s3_folder = 'name_api'
s3_filename = 'gender'
s3_filename2 = 'dob'
s3_filename3 = 'fullname'


s3_path = f"s3://{s3_bucket}/{s3_folder}/{s3_filename}"
s3_path2 = f"s3://{s3_bucket}/{s3_folder}/{s3_filename2}"
s3_path3 = f"s3://{s3_bucket}/{s3_folder}/{s3_filename3}"

# Fetch data from API
response = requests.get('https://randomuser.me/api/?results=500')

if response.status_code == 200:
    data = response.json()
    result = data["results"]
    result
else:
    print("Error: Unable to fetch data from the API")


# Male and Female list
gender = [item["gender"]for item in data]


# Male list
male_gender = []
for identity in gender:
    if identity == "male":
        male_gender.append(identity)


# Female list
female_gender = []
for identity in gender:
    if identity == "female":
        female_gender.append(identity)


# Extract Date of Birth(DOB)

dob = [item["dob"]["date"]for item in data]


# Concatenate first name and last name
names = [item["name"] for item in data]

full_name = [item["first"] + " " + item["last"] for item in names]


# convert to dataframe
df_gender = pd.DataFrame(gender)
df_dob = pd.DataFrame(dob)
df_fullname = pd.DataFrame(full_name)


df_gender.columns = df_gender.columns.astype(str)
df_dob.columns = df_dob.columns.astype(str)
df_fullname.columns = df_fullname.columns.astype(str)


session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
# Upload dataframe as a parquet file to s3
wr.s3.to_parquet(
    df_gender,
    path=s3_path,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)

wr.s3.to_parquet(
    df_dob,
    path=s3_path2,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)

wr.s3.to_parquet(
    df_fullname,
    path=s3_path3,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)


logging.info(f"Data successfully uploaded to {s3_path}")
logging.info(f"Data successfully uploaded to {s3_path2}")
logging.info(f"Data successfully uploaded to {s3_path3}")
