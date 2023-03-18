import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Charts")

st.write("Line chart")
chart_data = pd.DataFrame({
    'Year': ['2011', '2012', '2013'],
    'Volv' : [150, 180, 100],
    'Benz' : [120, 50, 80],
    'Lambo' : [20, 80, 180]
     })

st.line_chart(chart_data.set_index('Year'))


st.subheader("Widgets")

name = st.text_input("Insert your name")

x = st.slider('How many cars are you going to buy?')


if st.checkbox('I have placed my order'):
     st.write("Dear, ", name)
     st.write("You are going to buy ", x, " unit(s) for a total of ", x * 5000, " dollars")

     payment_method = st.selectbox(
          "Select your payment method",
          ["Debit", "Credit"]
     )



st.subheader("Layout")

import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
     latest_iteration.text(f'Wait until this section loads, progress: {i+1} / 100')
     bar.progress(i+1)
     time.sleep(0.1)


left_column, right_column = st.columns(2)
left_column.button('Press to reload!')
with right_column:
     with st.expander("Click to see more"):          
          tab1, tab2 = st.tabs(["Notes", "About"])
          tab1.write("This content is using tabs")
          tab2.write("Brought to you by Streamlit")
