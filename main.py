import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "email_address"
MY_PASSWORD = "password"

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


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 9
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 9

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
