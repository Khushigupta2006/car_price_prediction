import streamlit as st
data = pd.read_csv("D:\Applied AI\carprice.csv")
st.set_page_config(page_title="car price prediction App")

st.title("car price prediction dashboard")

mileage = st.text_input("Enter mileage")
fuel_type = st.text_input("Enter fuel type")

year = st.selectbox(
    "Select year",
    [data]
)

if st.button("Submit"):
    st.success("Successful")
    st.write("mileage:", mileage)
    st.write("fuel type:", fuel type)
    st.write("year:", year)
