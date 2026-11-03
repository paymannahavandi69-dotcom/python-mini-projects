import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name (English):")

if city:
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6892&longitude=51.3890&current_weather=true"
    
    response = requests.get(url)
    data = response.json()
    
    temperature = data["current_weather"]["temperature"]
    windspeed = data["current_weather"]["windspeed"]
    
    st.success(f"Weather in {city}")
    st.write(f"Temperature: {temperature} °C")
    st.write(f"Wind Speed: {windspeed} km/h")