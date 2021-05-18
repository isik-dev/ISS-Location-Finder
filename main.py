import requests

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

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)