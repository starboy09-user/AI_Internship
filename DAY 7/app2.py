import streamlit as st
import pandas as pd

st.title("Smart House Price Predictor")

area = st.number_input("Area (sq ft)", min_value=100, value=1000)
bedrooms = st.slider("Bedrooms", 1, 10, 2)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
parking = st.selectbox("Parking", ["Yes", "No"])

if st.button("Predict Price"):

    price = area * 5000
    price += bedrooms * 300000
    price += bathrooms * 200000

    if parking == "Yes":
        price += 500000

    st.success(f"Estimated Price: ₹{price:,}")

    # Category
    if price < 5000000:
        category = "Budget House"
        rating = 3
    elif price < 10000000:
        category = "Mid-Range House"
        rating = 4
    else:
        category = "Luxury House"
        rating = 5

    st.write("Category:", category)
    st.write("Rating:", "⭐" * rating)

    # Price Breakdown Chart
    data = pd.DataFrame({
        "Feature": ["Area", "Bedrooms", "Bathrooms"],
        "Value": [area * 5000, bedrooms * 300000, bathrooms * 200000]
    })

    st.subheader("Price Breakdown")
    st.bar_chart(data.set_index("Feature"))

    # Download Report
    report = f"""
House Price Report

Area: {area} sq ft
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}
Parking: {parking}

Category: {category}
Estimated Price: ₹{price}
"""

    st.download_button(
        "Download Report",
        report,
        file_name="house_report.txt"
    )