import csv
import requests

from datetime import datetime

apiKey = "7d21e4370d68439b4ffd363d1dd7acf4"

# We only want the daily informations
excludedFlags = "currently,flags,hourly,minutely"

# Latitude and longitude of Chicago
latitude = "41.8781"
longitude = "-87.6298"

# Timestamp for the 1st January 2007 at 12pm (Chicago hour)
timestamp = 1167670800

# Limit is set to 31th December 2017 at 12pm (Chicago hour)
limit = 1514739600

# Open file for writing
weatherCsv = open('weather.csv', 'w')

# Create the csv writer
csvWriter = csv.writer(weatherCsv)

baseUrl = "https://api.darksky.net/forecast/" + apiKey + "/" + latitude + "," + longitude + ","
exclude = "?exclude=" + excludedFlags

header = False

while timestamp < limit:
    weatherRequest = requests.get(baseUrl + str(timestamp) + exclude)
    weatherJson = weatherRequest.json()

    for data in weatherJson['daily']['data']:
        if header == False:
            csvWriter.writerow(data.keys())
            header = True
        csvWriter.writerow(data.values())
    print("Weather from: " + datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y"))
    timestamp += 604800


print ("weather.csv is ready! :)")