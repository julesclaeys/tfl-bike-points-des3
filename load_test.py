#Testing Connection to S3 Bucket
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

#Creating our Variables from .env
aws_acces = os.getenv("ACCESS_KEY")
aws_secret = os.getenv("SECRET_KEY")
aws_bucket = os.getenv("AWS_BUCKET_NAME")

#Setting client up
s3_client = boto3.client(
    's3',
    aws_access_key_id = aws_acces,
    aws_secret_access_key = aws_secret
)

#Setting up files
filename = "data/2025-07-15_10-13-36.json"
s3_file = 'bike-point/2025-07-15_10-13-36.json'

s3_client.upload_file(filename, aws_bucket, s3_file)
