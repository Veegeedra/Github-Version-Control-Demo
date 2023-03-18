import streamlit as st
import pandas as pd
import numpy as np

st.subheader("1. Write and Magic")

frame_data = pd.DataFrame({
    'Name': [
        "Jack",
        "Johnson",
        "James"
    ],
    'ID' :[
        101,
        102,
        105
    ]
})

"This section is an example of Write and Magic"
frame_data



st.subheader("2. Text Elements")

st.caption("The above is using subheader element while this text is using caption element, " + 
            "below is how it's written using code")
code = '''st.subheader("2. Text Elements")'''
st.code(code, language='python')



st.subheader("3. Data display elements")

st.write("The table in first section is displayed using st.table:")
st.table(frame_data)

st.write("The json data below is using dict, displayed using st.json")
dict = {
    'Jack' : 101,
    'Johnson' : 102,
    'James' : 105
}
st.json(dict)



st.subheader("4. Chart Elements")

st.write("Map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)



st.subheader("5. Input Widget")

name = st.text_input("Insert your name")

st.radio("Gender", ["Male", "Female"])
st.date_input("Birthday")
st.selectbox("Occupation", ["-- Select Occupation--", "Lecturer", "Student"])
st.checkbox("I am married")

st.button("Submit")




st.subheader("6. Media Elements")

st.image("https://thumbs.dreamstime.com/b/examples-word-written-wood-block-examples-text-table-concept-examples-word-written-wood-block-examples-text-table-125610689.jpg")
st.video("https://youtu.be/dQw4w9WgXcQ")




st.subheader("7. Layout Containers")

with st.expander("Click to see more"):
    col1, col2 = st.columns(2)
    col1.write("Left Column")
    col2.write("Right Column")

    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    tab1.write("Content of first tab")
    tab2.write("Content of second tab")


st.subheader("8. Status Elements")

import time

st.write("Wait until progress ends to see the rest of status elements")

i = 0
my_bar = st.progress(i)

for percent_complete in range(100):
    time.sleep(0.1)
    i = i+1
    my_bar.progress(i)

    if(i >=100):
        st.balloons()
        st.success("Progress successfully ended")



st.subheader("9. Control Flow")

with st.form(key='my_form'):
    username = st.text_input("Enter your Username")
    password = st.text_input("Enter your Password")
    st.form_submit_button("Login")





st.subheader("10. Utilities")


experimental_table = pd.DataFrame({
    'Name': [
        "Jack",
        "Johnson",
        "James"
    ],
    'ID' :[
        101,
        102,
        105
    ]
})

st.experimental_show(experimental_table)