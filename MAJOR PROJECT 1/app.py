import streamlit as st
import joblib

#load the joblib model
model = joblib.load('gas-diesel')

st.title('GAS-DIESEL CLASSIFIER')  #creates a title in web app
ip = st.text_input('Enter car name :')  #creates a text box in web app

op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  # st.button will create a button with name Predict

