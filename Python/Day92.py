import requests
import json
timezone = "GMT"
latitude = 6.524379
longitude = 3.379206

result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
# print(json.dumps(user, indent=2))

Date = user["daily"]["time"][0]
minimum = user["daily"]["temperature_2m_min"][0]
maximum = user["daily"]["temperature_2m_max"][0]
weather_code = user["daily"]["weathercode"][0]

print(f"""
For today : {Date}
Your location is: Longitude {user["longitude"]} and latitude {user["latitude"]}
Minimum: {minimum}
Maximum: {maximum}
Weather Code: {weather_code}
""")
