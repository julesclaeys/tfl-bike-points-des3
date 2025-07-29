#Loading Data in s3 bucket
#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
import os
import boto3
from dotenv import load_dotenv

def load_bikes(): 

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

    #Setting up variables

    try: 
        files = os.listdir('data')
        for file in files:
            if not file.startswith('.'):
                filename = "data/" + file
                s3_file = 'bike-point/' + file
                print(filename)
        
                try: 
                #Upoading File
                    s3_client.upload_file(filename, aws_bucket, s3_file)
                    print('Upload Successful')
                    os.remove(filename)
                    print('Deleted File')
                except: 
                    print('Could not Upload')
    except: 
        print('no files')