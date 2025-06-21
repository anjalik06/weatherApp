import streamlit as st
import pandas as pd
from weather_fetcher import fetch_weather_data
from visualize import plot_temperature_chart,plot_humidity_chart

API_KEY = st.secrets["API_KEY"]

st.set_page_config(
    page_title=" Weather Forecast Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Weather Forecast Dashboard")
city = st.text_input("Enter city name", "Bangalore")

if city:
    data, forecast_df = fetch_weather_data(city, API_KEY)

    if data and forecast_df is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{data['current']['temp_c']} °C")
            st.metric("Condition", data['current']['condition']['text'])
        with col2:
            st.metric("Humidity", f"{data['current']['humidity']}%")
            st.metric("Wind Speed", f"{data['current']['wind_kph']} kph")

        st.subheader("Temperature Forecast")
        plot_temperature_chart(forecast_df)
        plot_humidity_chart(forecast_df)  

    else:
        st.error("❌ Could not fetch weather data. Please check the city name or API key.")
