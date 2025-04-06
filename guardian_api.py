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
s3_folder = 'guardian_api'
s3_filename = 'guardian_api'


s3_path = f"s3://{s3_bucket}/{s3_folder}/{s3_filename}"

# Fetch data from API


baseurl = 'https://content.guardianapis.com/search'

params = {
        'api-key': 'test',
        'q': 'Nigeria',
        'from-date': '2025-01-01',
        'to-date': '2025-03-25',
        'page-size': 100
    }
response = requests.get(baseurl, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data['response']['results']
else:
    print("Error: Unable to fetch data from the API")


def nigeria_2025():
    list_of_articles = []
    for article in articles:
        data_list = {
                "Title": article["webTitle"],
                "URL": article["webUrl"],
                "Section_name": article["sectionName"],
                "Publication_date": article["webPublicationDate"]
            }
        list_of_articles.append(data_list)
    return list_of_articles


result = nigeria_2025()


df_nigeria = pd.DataFrame(result)

session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
# Upload dataframe as a parquet file to s3
wr.s3.to_parquet(
    df_nigeria,
    path=s3_path,
    dataset=True,
    mode='append',
    index=False,
    boto3_session=session)


logging.info(f"Data successfully uploaded to {s3_path}")
