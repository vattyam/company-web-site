import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title("The Best Company")

content = """ 
The Best Company is a visionary organization dedicated
         to delivering exceptional quality and innovative solutions across diverse industries.
         """
st.write(content)
st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5,0.5,1.5,0.5,1.5])

df = pandas.read_csv("data.csv")
print(df)

with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])







