import numpy as np
import pickle 
import streamlit as st

# Load the trained model
load_model = pickle.load(open('trained_model.sav', 'rb'))

# Function to make predictions
def prediction_cariac(ip_data):
    input_data_as_numpy_array = np.asarray(ip_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = load_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
   
def main():
    st.title("Cardiac Prediction")

    with st.form("prediction_form"):
        st.header("Patient Information")

        col1, col2 = st.columns(2)

        with col1:
            male = st.selectbox('Gender', ('Male', 'Female'))
            age = st.number_input('Age', min_value=0, max_value=120, step=1)
            education = st.selectbox('Education Level', ('1', '2', '3', '4'))
            currentSmoker = st.selectbox('Current Smoker', ('Yes', 'No'))
            cigsPerDay = st.number_input('Cigarettes per day', min_value=0, step=1)
            BPMeds = st.selectbox('On Blood Pressure Medication', ('Yes', 'No'))

        with col2:
            prevalentStroke = st.selectbox('Prevalent Stroke', ('Yes', 'No'))
            prevalentHyp = st.selectbox('Prevalent Hypertension', ('Yes', 'No'))
            diabetes = st.selectbox('Diabetes', ('Yes', 'No'))
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
            BPMeds = 1 if BPMeds == 'Yes' else 0
            prevalentStroke = 1 if prevalentStroke == 'Yes' else 0
            prevalentHyp = 1 if prevalentHyp == 'Yes' else 0
            diabetes = 1 if diabetes == 'Yes' else 0

            input_data = [male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]
            prediction = prediction_cariac(input_data)
            st.success(prediction)

    # # Collecting user input
    # male = st.text_input('Are you male? (1 for Yes, 0 for No)')
    # age = st.text_input('Age')
    # education = st.text_input('Education level (1-4)')
    # currentSmoker = st.text_input('Are you a current smoker? (1 for Yes, 0 for No)')
    # cigsPerDay = st.text_input('Cigarettes per day')
    # BPMeds = st.text_input('On blood pressure medication? (1 for Yes, 0 for No)')
    # prevalentStroke = st.text_input('Have you had a prevalent stroke? (1 for Yes, 0 for No)')
    # prevalentHyp = st.text_input('Have you had prevalent hypertension? (1 for Yes, 0 for No)')
    # diabetes = st.text_input('Do you have diabetes? (1 for Yes, 0 for No)')
    # totChol = st.text_input('Total cholesterol')
    # sysBP = st.text_input('Systolic blood pressure')
    # diaBP = st.text_input('Diastolic blood pressure')
    # BMI = st.text_input('Body mass index')
    # heartRate = st.text_input('Heart rate')
    # glucose = st.text_input('Glucose level')

    # prediction = ''

    # # Button for prediction
    # if st.button('Diabetic Test Result'):
    #     prediction = prediction_cariac([male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose])
    
    # st.success(prediction)

if __name__ == '__main__':
    main()
