import streamlit as st
import pickle
import numpy as np
from django.conf import settings
import os
import mysql.connector
# from .prediction_model import heart

            
heart_path = app_static_dir = os.path.join(settings.STATICFILES_DIRS, 'prediction_model', 'heart_disease_model.sav')
heart_model = pickle.load(open(heart_path, 'rb'))
# heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))

def heart_prediction(input_data):
        global global_prediction
        input_data_as_np_array = np.asarray(input_data)
        input_reshaped_data =  input_data_as_np_array.reshape(1,-1)
        #prediction
        prediction = heart_model.predict(input_reshaped_data)
        #prediction_data_type = type(prediction[0])
        #print(prediction_data_type)
        global_prediction = prediction[0]
        if global_prediction==0:
            return 'No worries!! Your heart is safe'
        else:
            return 'Alert!! Your heart is at risk'

# Establish a connection to MySQL database
def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123",
        database="dt_data"
        )

# Function to fetch data from MySQL database
    def get_data():
        query = "SELECT * FROM manager_patient_data WHERE patient_id = %s"
                # query = "SELECT * FROM user_data WHERE id = %s"
        values = (Id,)
        cursor = mydb.cursor()
        cursor.execute(query, values)

        # Fetch all rows
        data = cursor.fetchall()
        return data
    global Id
    Id = int(st.number_input("Enter your Id", format='%.0f'))
    st.write("Your ID is", Id)
    data = get_data()
    for item in data:
        #Name = st.write(f" Hi!! {item[5]}, Look at your health status")
        #Age = st.write(f" Age: {item[7]}")
        #Address = st.write(f" Address: {item[9]}")
        #Prediabetic = st.write(f" Prediabetic: {item[15]}, 0-No/1-Yes")
        #Glucose =  st.write(f" Glucose Level is: {item[11]}")
        #BloodPressure =  st.write(f" Blood Pressure Level: {item[12]}")
        #Insulin =  st.write(f"Insulin Level:{item[13]}")
        #BMI =  st.write(f" Body Mass Index Level: {item[14]}")
        #DiabetesPedigreeFunction =  st.write(f"Diabetes Pedigree Function value: {item[16]}")
        #Cholestrol =  st.write(f" Cholestrol Level: {item[17]}")
        #Exercise =  st.write(f" Total Exercise duration/day: {item[18]} hrs")
        #Brushing =  st.write(f" Brushing Habit: {item[19]} times a day")
        Name = st.write(f" Hi!! {item[1]}")
            
    diagnosis = ''
        
    #creating a button for prediction
        
    if st.button('heart Test Result'):
        diagnosis = heart_prediction([item[7], item[8], item[10], item[12]])
        # diagnosis = heart_prediction([item[7], item[8], item[10], item[12], item[17], item[15], item[21]])
        update_query = "UPDATE user_data SET heart_outcome = CAST(%s AS UNSIGNED) WHERE id = %s"
        outcome_value = int(global_prediction)
        value = (outcome_value,Id)
        cursor = mydb.cursor()
        cursor.execute(update_query, value)
        mydb.commit()

        st.success(diagnosis)
        st.markdown(diagnosis, unsafe_allow_html=True)