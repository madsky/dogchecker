#dogchecker.py

import requests
from bs4 import BeautifulSoup
import time

import boto3

total = 0
newtotal = 0

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="KEY",
    aws_secret_access_key="KEY",
    region_name="eu-west-1"
)

while True:
    print(time.asctime() + ": Starting new check...")
    page = requests.get("https://www.pets4homes.co.uk/search/?type_id=3&breed_id=441&advert_type=1&location=manchester&distance=50&maxprice=1500&results=20&sort=datenew")
    soup = BeautifulSoup(page.text, 'html.parser')
    grp = soup.select("b")
    newtotal = int(grp[0].get_text())
    if newtotal != total:
        print("Something has changed. Old count was: " + str(total) + ", New count is: " + str(newtotal) + ". ")
        # Send your sms message.
        client.publish(
            PhoneNumber="+44MOBILENUMBER",
            Message="There are now " + str(newtotal) + " listings (there were " + str(total) + " last time I checked). Check it out here: 'https://bit.ly/3gnzDzZ'" 
        )
    else:
        print("No change (" + str(total) + ")")
    total = newtotal
    time.sleep(900) #15mins