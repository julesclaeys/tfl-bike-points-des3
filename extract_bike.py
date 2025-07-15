import json
from datetime import datetime
import time
import requests

#Define function
def extract_bikes():

    #Make API Call
    url = "https://api.tfl.gov.uk/BikePoint"
    response = requests.get(url)

    #Setting up multiple tries
    max_tries = 5
    current_try = 0
    wait_time = 1

    while current_try < max_tries: 
    #Handle Error
        try: 
            response.raise_for_status()
            data = response.json()
            now = datetime.now()

            #Check There is enough Data
            if len(data) < 50:
                raise Exception("Empty JSON")
            
            #Set File name and write to file
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filepath = "data/" + filename + ".json"
            with open(filepath, 'w') as file:
                json.dump(data, file)
            #Check modified date is recent
            modified_dates = []
            for stations in data:
                for item in stations.get("additionalProperties", []):
                    if "modified" in item:
                        modified_dates.append(item["modified"])
            max_modified_date = datetime.strptime(max(modified_dates), "%Y-%m-%dT%H:%M:%S.%fZ")
            datediff = now-max_modified_date
            if datediff.days > 2:
                raise Exception("Data has not updated")
            
            print('Success!!!!')

            break

        #Raise Exceptions
        except requests.exceptions.RequestException as e: 
            print(e)
        except Exception as e: 
            print(e)
        except: 
            print("fail")

        current_try +=1
        print("Waiting")
        time.sleep(10)

    if current_try == max_tries:
        print("Too Many Tries")

if __name__ == '__main__': 
    extract_bikes()