import requests

def get_weather():
    
    try:
        ip_response = requests.get('https://ipinfo.io/json')
        ip_data = ip_response.json()
        
        # ipinfo returns location as a string "lat,lon"
        lat, lon = ip_data['loc'].split(',')
        city = ip_data['city']
        # print(f"Location found: {city} (Lat: {lat}, Lon: {lon})")
        
    except Exception as e:
        print("Could not detect location. Please check your internet connection.")
        return
    
    API_KEY = "c72c37b4c8ce68127db5e35219eb6713"
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temp = weather_data['main']['temp']
            return (f"Today's Temperature is {temp}°C")
            
        else:
            return (f"Error fetching weather: {weather_response.json().get('message')}")
            
    except Exception as e:
        return ("Could not connect to the weather service.")

if __name__ == "__main__":
    get_weather()