# ❤️ Heart Disease Prediction

A machine learning project that predicts a patient's risk of heart disease from clinical measurements, with an interactive **Streamlit** web app for real-time predictions.

## 🩺 Overview

This project trains classification models on patient health data (age, blood pressure, cholesterol, ECG results, etc.) to predict whether a person is at **low** or **high risk** of heart disease. The final model is deployed through a simple, interactive web interface built with Streamlit.

## ✨ Features

- Interactive web app for entering patient details and getting instant predictions
- Trained **K-Nearest Neighbors (KNN)** classifier (used in the deployed app)
- **Logistic Regression** model also trained for comparison
- Data preprocessing pipeline (scaling of numerical features, one-hot encoding of categorical features)
- Jupyter notebooks documenting data exploration, preprocessing, and model training

## 📂 Project Structure

```
Heart-disease-project/
├── app.py                          # Streamlit web application
├── hearts.ipynb                    # Data analysis & model training notebook
├── heart.csv                       # Heart disease dataset
├── _KNN_hearts.pkl                 # Trained KNN model (used by app.py)
├── _logistic_regression_hearts.pkl # Trained Logistic Regression model
├── scalar.pkl                      # Fitted scaler for numerical features
├── columns.pkl                     # Column/feature order used at inference time
```

## 📊 Input Features

The model takes the following patient details as input:

| Feature | Description |
|---|---|
| Age | Age of the patient |
| Sex | Male / Female |
| Chest Pain Type | ATA, NAP, TA, or ASY |
| Resting Blood Pressure | Resting BP in mm Hg |
| Cholesterol | Serum cholesterol in mg/dL |
| Fasting Blood Sugar | Whether fasting blood sugar > 120 mg/dL |
| Resting ECG | Normal, ST, or LVH |
| Max Heart Rate | Maximum heart rate achieved |
| Exercise Induced Angina | Yes / No |
| Oldpeak | ST depression induced by exercise |
| ST Slope | Up, Flat, or Down |

The output is a simple prediction: **Low risk** or **High risk** of heart disease.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shubh556/Heart-disease-project.git
   cd Heart-disease-project
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit pandas scikit-learn joblib
   ```

### Running the App

```bash
streamlit run app.py
```

This will launch the web app in your browser, where you can enter patient details and get an instant heart disease risk prediction.

## 🧠 Model

The deployed app uses a **K-Nearest Neighbors (KNN)** classifier trained on the dataset in `heart.csv`. Numerical features (age, resting BP, cholesterol, max heart rate, oldpeak) are scaled using a saved `StandardScaler` (`scalar.pkl`) before being passed to the model, and categorical features are one-hot encoded to match the column order stored in `columns.pkl`. A Logistic Regression model was also trained for comparison and is saved as `_logistic_regression_hearts.pkl`. The full training and evaluation workflow, including exploratory data analysis, is available in `hearts.ipynb`.

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Please consult a qualified healthcare provider for any medical concerns.

## 👤 Author

**Shubh** — [shubh556](https://github.com/shubh556)

## 📄 License

This project currently has no license specified. Feel free to reach out to the author regarding usage.
