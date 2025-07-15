#Running functions from extract and load functions

#Imports
import json
from datetime import datetime
import time
import requests
import os
import boto3
from dotenv import load_dotenv

#Import Function
from extract_bike import extract_bikes  
from load_dev import load_bikes  

extract_bikes()
load_bikes()