import numpy as np
import pandas as pd
import streamlit as st
import joblib

# let's load all instances required over here
with open('transformer.joblib','rb') as file :
    transformer = joblib.load(file)

# let's load model
with open('final_model.joblib','rb') as file :
    model = joblib.load(file)

st.title('INN HOTEL GROUP')
st.header(':blue[This application will predict the chance of booking cancellation]')

# Let's take input from user
amnth = st.slider('select your month of arrival',min_value =1,max_value=12,step=1)
awkd_lmda = (lambda x: 0 if x=='Mon' else 1 if x=='Tues' else 2 if x=='Wed' else 3 if x=='Thurs' else 4 if x=='Fri' else 5 if x=='Sat' else 6)
awk = awkd_lmda(st.selectbox('Select your weekday arrival',['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']))
dw = awkd_lmda(st.selectbox('Select your weekday departure',['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']))
wknd = st.number_input('How many weekends nights you stay there :',min_value = 0)
wk = st.number_input('How many week nights you stay there :',min_value = 0)
tn = wknd+wk
mkt = (lambda x: 0 if x=='Offline' else 1)(st.selectbox('How the booking has been made',['Offline','Online']))
lt = st.number_input('How many days prior the booking has been made',min_value =0)
price = st.number_input('What is the avg price per room',min_value =0)
adul = st.number_input('How many adult members in the booking ',min_value =0)
spcl = st.selectbox('Select the number of special request made ',[0,1,2,3,4,5])
park = (lambda x: 0 if x=='No' else 1 )(st.selectbox('Does guest need parking space',['Yes','No']))

# Transform the data
lt_t, price_t= transformer.transform([[lt, price]])[0]

# create an input list
input_list=[lt_t, spcl, price_t, adul, wknd, park, wk, mkt, amnth, awk, tn, dw]

#prediction
prediction = model.predict_proba([input_list])[:,1][0]

if st.button('Predict'):
    st.success(f'Cancellation chances :  {round(prediction,4)*100} %')



