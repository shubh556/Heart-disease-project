import pandas as pd

age = 25
sex = 'Male'
chest_pain = 'TA'
resting_bp = 100
cholesterol = 300
fasting_bs = 'No'
resting_ecg = 'ST'
max_hr = 120
exercise_angina = 'Y'
oldpeak = 1.0
st_slope = 'Up'

raw_input = {
    'Age': age,
    'RestingBP': resting_bp,
    'Cholesterol': cholesterol,
    'FastingBS': 1 if fasting_bs == 'Yes' else 0,
    'MaxHR': max_hr,
    'Oldpeak': oldpeak,
    'Sex_M': 1 if sex == 'Male' else 0,
    'ChestPainType_' + chest_pain: 1,
    'RestingECG_' + resting_ecg: 1,
    'ExerciseAngina_' + exercise_angina: 1,
    'ST_Slope_' + st_slope: 1
}

cols = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
        'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_LVH'
        , 'Sex_M', 'ChestPainType_ASY', 'ChestPainType_ATA',
        'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_N',
        'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up']

for col in cols:
    if col not in raw_input:
        raw_input[col] = 0

print(raw_input)

df = pd.DataFrame([raw_input])
print(df)