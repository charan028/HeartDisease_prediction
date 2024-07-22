import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


load_model = pickle.load(open('lgbm_model.pkl', 'rb'))


def prediction_cariac(ip_data):
    input_data_as_numpy_array = np.asarray(ip_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = load_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
    st.title("Heart Disease Prediction")


    
    with st.form("prediction_form"):
        st.header("Patient Information")

        col1, col2 = st.columns(2)

        with col1:
            male = st.selectbox('Gender', ('Male', 'Female'))
            age = st.number_input('Age', min_value=0, max_value=120, step=1)
         
            currentSmoker = st.selectbox('Current Smoker', ('Yes', 'No'))
            cigsPerDay = st.number_input('Cigarettes per day', min_value=0, step=1)
       

        with col2:

            prevalentHyp = st.selectbox('Prevalent Hypertension', ('Yes', 'No'))
            
            totChol = st.number_input('Total Cholesterol', min_value=0, step=1)
            sysBP = st.number_input('Systolic Blood Pressure', min_value=0, step=1)
            diaBP = st.number_input('Diastolic Blood Pressure', min_value=0, step=1)
            BMI = st.number_input('Body Mass Index', min_value=0.0, step=0.1)
            heartRate = st.number_input('Heart Rate', min_value=0, step=1)
            glucose = st.number_input('Glucose Level', min_value=0, step=1)

        submit_button = st.form_submit_button(label='Get Prediction')

        if submit_button:
            male = 1 if male == 'Male' else 0
            currentSmoker = 1 if currentSmoker == 'Yes' else 0
           
         
            prevalentHyp = 1 if prevalentHyp == 'Yes' else 0
           

            input_data = [male, age, currentSmoker, cigsPerDay, prevalentHyp, totChol, sysBP, diaBP, BMI, heartRate, glucose]
            prediction = prediction_cariac(input_data)
            
            st.success('Prediction: ' + ('coronary heart disease ' if prediction == 1 else 'Not coronary heart disease '))
            
            # Visualizing classification results with a confusion matrix
            true_labels = [0, 1]  # Assuming binary classification: 0 = Not Diabetic, 1 = Diabetic
            predicted_labels = [0, 1]  # Placeholder, typically you would have more data
            
         

if __name__ == '__main__':
    main()
