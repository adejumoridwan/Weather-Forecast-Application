import streamlit as st
import pandas as pd
import prophet as Prophet


@st.cache_data
def get_data():
    data = pd.read_csv("DailyDelhiClimateTrain.csv")
    data.columns = ["date", "temperature", "humidity", "wind_speed", "pressure"]
    return data


data = get_data()

weather_variable = st.selectbox("Weather Variable", data.columns[1:])

st.line_chart(data.set_index("date")[weather_variable])
