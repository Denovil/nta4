import streamlit as st
st.write("My first application")
Username = st.text_input("Enter Username")
Age = st.number_input("Enter Age")
if 18 =< Age >= 100:
  st.write("vote ")
else:
  st.write("Can't vote ")
