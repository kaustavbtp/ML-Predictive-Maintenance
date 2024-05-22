import streamlit as st
import requests

st.title("Machine Break Prediction")

with st.form(key='my_form'):
    voltage = st.text_input('Voltage in Volt', value="0")
    runtime = st.text_input('Runtime in Minutes', value="0")
    speed = st.text_input('Speed in RPM', value="0")
    vibration = st.text_input('Motor Vibration in Hertz', value="0")
    weight = st.text_input('Total Packed Goods Weight in Grams', value="0")
    temperature = st.text_input('Temperature of Motor in Celsius', value="0")
    submit_button = st.form_submit_button(label='Predict Probability')

if submit_button:
    data = {
        "voltage": int(voltage),
        "runtime": int(runtime),
        "speed": int(speed),
        "vibration": int(vibration),
        "weight": int(weight),
        "temperature": int(temperature)
    }

    # Assuming your FastAPI backend is running on localhost port 8000
    response = requests.post("http://localhost:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(result['message'])
    else:
        st.error("Failed to get response from the API: " + response.text)
