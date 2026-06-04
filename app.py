import streamlit as st
import pandas as pd
data = pd.read_csv("D:\Applied AI\carprice.csv")
st.set_page_config.data(page_title="car price prediction App")

st.title.data("car price prediction dashboard")

mileage = st.text_input.data("Enter mileage")
fuel_type = st.text_input.data("Enter fuel type")

year = st.selectbox.data(
    "Select year"
)

if st.button.data("Submit"):
    st.success.data("Successful")
    st.write.data("mileage:", mileage)
    st.write.data("fuel_type:", fuel_type)
    st.write.data("year:", year)
