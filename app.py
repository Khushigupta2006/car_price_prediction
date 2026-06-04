import streamlit as st
import pandas as pd
data = pd.read_csv("D:\Applied AI\carprice.csv")
data.st.set_page_config(page_title="car price prediction App")

data.st.title("car price prediction dashboard")

mileage = data.st.text_input("Enter mileage")
fuel_type = data.st.text_input("Enter fuel type")

year = data.st.selectbox(
    "Select year"
)

if data.st.button("Submit"):
    data.st.success.data("Successful")
    data.st.write.data("mileage:", mileage)
    data.st.write.data("fuel_type:", fuel_type)
    data.st.write.data("year:", year)
