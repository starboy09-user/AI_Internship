import streamlit as st

st.title("House Price Prediction App")

st.write("Enter the house area to predict the price.")

area = st.number_input(
    "House Area (Square Feet)",
    min_value=100,
    value=1000
)

if st.button("Predict Price"):
    predicted_price = area * 5000

    st.success(
        f"Predicted House Price: ₹{predicted_price}"
    )