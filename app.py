import streamlit as st
st.title('Calculate Your BMI')
wt = st.number_input('Enter your weight in kgs : ')
ht = st.number_input('Enter your height in M : ')

if ht==0:
    BMI =0
else:
    BMI = wt/ht**2
st.success(f'Your BMI is {BMI} kg/M^2')