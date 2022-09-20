import streamlit as st
import joblib

#load the joblib model
model_nb  = joblib.load('gas-diesel')

st.title('GAS-DIESEL CLASSIFIER')
ip = st.text_input('Enter car name :')

op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
