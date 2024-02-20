import streamlit as st
import requests


# Define the FastAPI server URL
FASTAPI_URL = "http://localhost:8000"  # Change this to match your FastAPI server URL


# Function to send a prediction request to FastAPI server
def get_prediction(weather_variable, days):
    url = f"{FASTAPI_URL}/predict"
    payload = {"weather_variable": weather_variable, "days": days}
    response = requests.post(url, data=payload)
    return response.json()


# Streamlit UI
def main():
    st.title("Forecast")

    # User inputs
    weather_variable = st.text_input("Weather Variable", "")
    days = st.number_input("Days", min_value=1, max_value=365, value=7)

    # Button to trigger prediction
    if st.button("Get Prediction"):
        if weather_variable and days:  # Check if both fields are filled
            prediction = get_prediction(weather_variable, days)
            for key, value in prediction["forecast"].items():
                st.write(key, "-", f"{value:.2f}")
        else:
            st.error("Please provide values for both Weather Variable and Days.")


if __name__ == "__main__":
    main()
