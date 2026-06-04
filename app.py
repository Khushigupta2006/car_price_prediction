import streamlit as st
import pandas as pd
data = pd.read_csv("D:\Applied AI\carprice.
st.set_page_config(page_title="car price prediction App")

st.title("car price prediction dashboard")

mileage = st.text_input("Enter mileage")
fuel_type = st.text_input("Enter fuel type")

year = st.selectbox(
    "Select year"[data]
)

if st.button("Submit"):
    st.success.data("Successful")
    st.write.data("mileage:", mileage)
    st.write.data("fuel_type:", fuel_type)
    st.write.data("year:", year)
