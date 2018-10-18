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

# Create the csv writer
csvWriter = csv.writer(open('weather.csv', 'wb+'))

baseUrl = "https://api.darksky.net/forecast/" + apiKey + "/" + latitude + "," + longitude + ","
exclude = "?exclude=" + excludedFlags

csvWriter.writerow(["summary",
		    "icon",
		    "precipIntensity",
		    "precipIntensityMax",
		    "temperatureHigh",
		    "temperatureHigTime",
		    "temperatureLow",
		    "temperatureLowTime",
		    "humidity",
		    "pressure",
		    "windSpeed",
		    "cloudCover",
		    "visibility"])

while timestamp < limit:
    weatherRequest = requests.get(baseUrl + str(timestamp) + exclude)
    weatherJson = weatherRequest.json()

    for data in weatherJson['daily']['data']:
        csvWriter.writerow([data["summary"],
			    data["icon"],
			    data["precipIntensity"],
			    data["precipIntensityMax"],
			    data["temperatureHigh"],
			    data["temperatureHighTime"],
			    data["temperatureLow"],
			    data["temperatureLowTime"],
			    data["humidity"],
			    data["pressure"],
			    data["windSpeed"],
			    data["cloudCover"],
			    data["visibility"]])

    print("Weather from: " + datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y"))
    timestamp += 604800

print ("weather.csv is ready! :)")
