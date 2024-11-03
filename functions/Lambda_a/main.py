import json
import pandas as pd
import requests as rq
import boto3
import os
import datetime
from io import StringIO

def etl(url):
    #env_variable
    bucket_name = os.getenv('Bucket')
    #S3 client
    s3_client = boto3.client('s3')
    #file_name
    # Get the current date
    current_date = datetime.datetime.now()
    # Format the date to get the abbreviated month name
    abbreviated_month = current_date.strftime('%b')
    file_key = "{}/{}.csv".format(abbreviated_month,current_date)
    # Making a GET request
    response = rq.get(url)
    # Checking the status code of the response
    if response.status_code == 200:
        # If successful, get the content
        data = response.json()  # Assuming the API returns JSON data
        df = pd.DataFrame(data)
        df['creation_date'] = pd.Timestamp.today().date()
        csv_buffer = StringIO()
        df.to_csv(csv_buffer,sep=";",index=False)
        try:
            # Upload the CSV content to S3
            s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=csv_buffer.getvalue())
            print(f"File uploaded successfully to s3://{bucket_name}/{file_key}")
        except Exception as e:
            print(f"Failed to upload the file: {str(e)}")
                
    
    

def lambda_handler(event, context):
    
    etl("https://jsonplaceholder.typicode.com/posts")
    
    