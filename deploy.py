# -*- coding: utf-8 -*-
"""
Created on Friday October 18 08:04:15 2024

@author: Jai-Keshav-Sharma
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
heart_disease_model = pickle.load(open('heart_disease_prediction_logisticRegression.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Input fields arranged in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, step=1)
        
    with col2:
        sex = st.selectbox('Sex (1 = Male, 0 = Female)', options=[1, 0])
        
    with col3:
        cp = st.selectbox('Chest Pain Types (0-3)', options=[0, 1, 2, 3])
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure (in mm Hg)', step=1)
        
    with col2:
        chol = st.number_input('Serum Cholesterol in mg/dl', step=1)
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', options=[1, 0])
        
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results (0-2)', options=[0, 1, 2])
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', step=1)
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', options=[1, 0])
        
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', format="%.2f")
        
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment (0-2)', options=[0, 1, 2])
        
    with col3:
        ca = st.selectbox('Major Vessels Colored by Fluoroscopy (0-3)', options=[0, 1, 2, 3])
        
    with col1:
        thal = st.selectbox('Thal (1 = Fixed Defect, 2 = Normal, 3 = Reversible Defect)', options=[1, 2, 3])
        
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to a list of numeric values
            input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            
            # Make prediction
            heart_prediction = heart_disease_model.predict(input_data)
            
            # Display result
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
                
        except ValueError:
            st.error("Please enter valid numeric values.")
        
    st.success(heart_diagnosis)
