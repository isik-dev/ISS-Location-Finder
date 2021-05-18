import requests
from datetime import datetime

MY_LAT = 37.566536
MY_LNG = 126.977966

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)

# # in case we omit a letter from the url then we get the following response:
# response = requests.get(url="http://api.open-notify.org/is-now.json")
# print(response)
# print(response.status_code)

# in order to deal with the errors, we can specify their type and details as follows:

# response = requests.get(url="http://api.open-notify.org/is-now.json")
# response.raise_for_status()

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
