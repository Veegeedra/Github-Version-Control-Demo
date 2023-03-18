import streamlit as st
import pandas as pd
import numpy as np

"""
# App
"""

st.subheader("Manual Dataframe")

st.write("Currency Conversion Rate, 04 Mar 2023")

frame_data = pd.DataFrame({
    'Currency': [
        "Euro",
        "British Pound",
        "Indian Rupee",
        "Australian Dollar",
        "Canadian Dollar",
        "Singapore Dollar",
        "Japanese Yen"
    ],
    'From 1.00 USD': [
        0.940238,
        0.830462,
        81.712488,
        1.477665,
        1.361745,
        1.344201,
        135.867351
    ],
    'To 1.00 USD': [
        1.063560,
        1.204149,
        0.012238,
        0.676744,
        0.734352,
        0.743936,
        0.007360
    ]
})

st.write(frame_data)


st.subheader("Line chart:")

st.write("CD PROJEKT SA (CDR), 2022")
chart_data = pd.DataFrame({
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Terakhir' : [180.06, 168.40, 173.74, 120.98, 108.66, 95.68, 90.81, 84.12, 100.20, 127.10, 130.98, 129.64],
    'Tertinggi' : [208.10, 188.00, 187.14, 179.92, 125.40, 110.62, 105.92, 96.69, 108.50, 128.60, 153.50, 143.00],
    'Terendah' : [166.10, 150.20, 155.00, 119.78, 105.88, 86.69, 86.60, 80.86, 76.83, 96.61, 126.24, 122.58]
})

chart_data = chart_data.set_index('Month')
st.line_chart(chart_data)


#Data from: x-rates.com, investing.com
#Reference: https://discuss.streamlit.io/t/date-at-x-axis-of-line-chart/853/3