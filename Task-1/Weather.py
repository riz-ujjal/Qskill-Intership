import requests
from pydantic import BaseModel
from fastapi import FastAPI

# For getting the latitude and longitude.
send_url = "http://api.ipstack.com/check?access_key=dad5401b4a4b79cbdce4041b0139e65f"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
print("lati: " , latitude)
print("longi: ", longitude)
print("city: ", city)
app =FastAPI()
class weather(BaseModel):
    temprature : int
    city :str

@app.get("/temp/")
def get_temp ():
    url = "https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=&units=metric"
    response =requests.get(url)
    data = response.json()
    temperature = ["current_temperature"]["temperature"]
    return f"{temperature}" 

import json

send_url = "http://api.ipstack.com/check?access_key=dad5401b4a4b79cbdce4041b0139e65f"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
print("lati: " , latitude)
print("longi: ", longitude)
print("city: ", city)
