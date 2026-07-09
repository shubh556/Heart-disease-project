import streamlit as st
import pandas as pd
import joblib

model = joblib.load('_KNN_hearts.pkl')     
scalar = joblib.load('scalar.pkl')
columns = joblib.load('columns.pkl')

st.title('Heart Disease Prediction By SHUBH')
st.markdown('Provide following details about Patient')

age = st.slider('Age', 18, 100, 40)
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input('Cholesterol (mg/dL)', 100, 600, 200)
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['Yes', 'No'])
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
max_hr = st.slider('Maximum Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
oldpeak = st.slider('Oldpeak (ST Depression)', 0.0, 6.0, 1.0)
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

if st.button('Predict Heart Disease'):
    raw_input = {
        'Age' : age,
        'RestingBP' : resting_bp,
        'Cholesterol' : cholesterol,
        'FastingBS' : 1 if fasting_bs == 'Yes' else 0,
        'MaxHR' : max_hr,
        'Oldpeak' : oldpeak, 
        'Sex_M' : 1 if sex == 'Male' else 0, 
        'ChestPainType_ASY' : 1 if chest_pain == 'ASY' else 0, 
        'ChestPainType_ATA' : 1 if chest_pain == 'ATA' else 0,
       'ChestPainType_NAP' : 1 if chest_pain == 'NAP' else 0, 
       'ChestPainType_TA' : 1 if chest_pain == 'TA' else 0, 
       'RestingECG_LVH' : 1 if resting_ecg == 'LVH' else 0,
       'RestingECG_Normal' : 1 if resting_ecg == 'Normal' else 0, 
       'RestingECG_ST' : 1 if resting_ecg == 'ST' else 0, 
       'ExerciseAngina_N' : 1 if exercise_angina == 'No' else 0,
       'ExerciseAngina_Y' : 1 if exercise_angina == 'Yes' else 0,
        'ST_Slope_Down' : 1 if st_slope == 'Down' else 0, 
        'ST_Slope_Flat' : 1 if st_slope == 'Flat' else 0, 
        'ST_Slope_Up' : 1 if st_slope == 'Up' else 0
    }

    df = pd.DataFrame([raw_input])
    scale_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    df[scale_cols] = scalar.transform(df[scale_cols])
    pred = model.predict(df)[0]

    if pred == 0:
        st.success('Low risk of Heart Disease')
    else:
        st.error('High risk of Heart Disease')
