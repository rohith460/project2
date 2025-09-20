import requests

API_KEY = "cef038f47237acf380b153fa71197390"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != "404":
        weather = data["main"]
        temp = weather["temp"]
        humidity = weather["humidity"]
        description = data["weather"][0]["description"]
        print(f"\n🌍 City: {city}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {description}")
    else:
        print("❌ City not found!")

# Example
city = input("Enter city: ")
get_weather(city)
