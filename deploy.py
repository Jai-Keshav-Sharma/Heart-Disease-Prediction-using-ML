import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# Load the model and the scaler
heart_disease_model = pickle.load(open('heart_disease_prediction_logisticRegression.sav', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))  # Load the scaler if used

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Heart Disease Prediction'],
                          icons=['activity', 'heart', 'person'],
                          default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Collecting input values
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (1 = male; 0 = female)')

    with col3:
        cp = st.text_input('Chest Pain types (0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            inputs = [
                float(age),
                int(sex),
                int(cp),
                float(trestbps),
                float(chol),
                int(fbs),
                float(restecg),  # Allow float for restecg
                float(thalach),
                int(exang),
                float(oldpeak),  # Allow float for oldpeak
                int(slope),
                int(ca),
                int(thal)
            ]

            # Scale the inputs if a scaler was used during training
            inputs_array = np.array([inputs])
            inputs_scaled = scaler.transform(inputs_array)  # Apply the scaler

            heart_prediction = heart_disease_model.predict(inputs_scaled)

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        except ValueError:
            st.error("Please ensure all inputs are valid numeric values.")

    st.success(heart_diagnosis)
