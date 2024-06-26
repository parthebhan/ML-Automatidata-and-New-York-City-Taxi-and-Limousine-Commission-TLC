import os
import pickle
import streamlit as st

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
model = pickle.load(open(f'{working_dir}/Automatidata.sav', 'rb'))

# Define the function for making predictions
def automatidata(VendorID, passenger_count, Distance, Duration, rush_hour):
    inputs = [[VendorID, passenger_count, Distance, Duration, rush_hour]]
    prediction = model.predict(inputs) 
    prediction_value = prediction[0][0]
    return f"Predicted fare amount (Approx.) = {round(prediction_value, 2)} $"

# Create Streamlit interface
st.title("New York City Taxi and Limousine Commission (TLC) - Taxi Fares Estimator")
st.write("")
st.write("Predicting Taxi Fare Amount Using Machine Learning        -         Created by: Parthebhan Pari")
st.write("")


VendorID = st.slider("VendorID - [1 or 2]", 1, 2, 1)
passenger_count = st.slider("Passenger Count - [1 to 6]", 0, 6, 1)
Distance = st.number_input("Distance in miles")
Duration = st.number_input("Duration in mins")
rush_hour = st.slider("Rush Hour - [0 or 1]", 0, 1, 0)

if st.button("Predict Fare"):
    result = automatidata(VendorID, passenger_count, Distance, Duration, rush_hour)
    st.write("")
    st.write("")
    st.write(result)

st.write("--------------")
st.write("")
st.write("Example Inputs:")
st.write("")
st.write("[VendorID, Passenger Count, Distance, Duration, Rush Hour]")
st.write("[2, 1, 2.33, 15.09, 0]")
st.write("[1, 2, 4.22, 24.29, 0]")
st.write("[1, 1, 0.71, 6.66, 0]")
st.write("[2, 1, 0.97, 8.37, 0]")
st.write("[2, 3, 1.48, 8.92, 0]")
st.write("")
