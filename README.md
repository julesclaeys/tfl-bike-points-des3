# DES 3 - Mailchimp Project

This project follows the same logic as the amplitude project (https://github.com/julesclaeys/Deng3-amplitude)
If you want to know more about the process please follow the readme in there. The main difference is we did not perform the orchestration using kestra this time. There is space to organise this in the future.

Here is the pipeline we built for our Mailchimp data:
<img width="1141" height="320" alt="image" src="https://github.com/user-attachments/assets/911eb344-007a-49e7-8954-6522b57ad0d0" />

Mailchimp is an all in one marketing platform focusing on email marketing. The documentation for the API we used to acces our data can be found here: https://mailchimp.com/developer/marketing/api/root/

## 1. Extract & Load

Extract and load were done in python, both python script can be found, they include logging and documentation. We extracted email activity and campaign tables from mailchimp, directly loading them into our s3 bucket. Error handling assured that both campaigns and email activities were saved to a directory in the process assuring data is present before trying to load it into the bucket. 

## 2. Transformations

After reviewing the documentation, this is the normalised schema I came up with for my silver layer:

<img width="1317" height="760" alt="image" src="https://github.com/user-attachments/assets/45b7eff6-ed49-4835-b9fb-715abaf71536" />

### In dbt

We used the raw data from snowflake as our starting point, this means we needed to ensure in our staging layer that the data was extracted from the json arrays, renamed appropriately. 
Our intermediate layer focused on a first round of transformation for normalisation, unlike in Amplitude, I opted for this extra layer to help catch any data quality issues and for a better more understandle process. I only recreated the email activity and campaign tables, hashing all the fields required in this step as a table to avoid extra processing power being required to run the pipeline. 
The marts or gold layer then includes the tables present in our schema, opting to create them with the hashing already done allows us to build them as views, taking little storage space and even less computing power as the processing is done in the table in the previous step. 

<img width="1047" height="968" alt="image" src="https://github.com/user-attachments/assets/2cf18dfb-1388-45c0-8984-5c5d39d103fe" />

### In snowflake

The schema wass directly build from the raw tables, this should be optimised if we had more data or were working at a larger scale. However for this project, it was quicker to just build all the tables including hashing as one, then to create a single procedure which would run everything based on the last run of the python script being more recent than the data present in the current snowflake table. 

## 3. Next Steps

Our next step should focus on orchestrating this whole pipeline, potentially using Kestra, or maybe via github actions for a change from the Amplitude project. 

