import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name (English):")

if city:
    # Step 1: Get coordinates from city name
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    
    if "results" not in geo_data:
        st.error("City not found!")
    else:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        
        # Step 2: Get weather from coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        temperature = weather_data["current_weather"]["temperature"]
        windspeed = weather_data["current_weather"]["windspeed"]
        
        st.success(f"Weather in {city}")
        st.write(f"Temperature: {temperature} °C")
        st.write(f"Wind Speed: {windspeed} km/h")