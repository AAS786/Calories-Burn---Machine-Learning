import streamlit as st

import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

loaded_model = pickle.load(open('Calories_model.sav','rb'))

def check(input_data):

    array_input = np.array(input_data)

    reshaped_input = array_input.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_input)

    return format(prediction[0])

def main():
    st.title("Calories Burn  Prediction")

    User_ID = st.number_input("User_ID")

    Gender = st.number_input("Gender")

    Age = st.number_input("Age")

    Height = st.number_input("Height")

    Weight = st.number_input("Weight")

    Duration = st.number_input("Duration")

    Heart_Rate = st.number_input("Heart_Rate")

    Body_Temp = st.number_input("Body_Temp")

    pred = ""
    if st.button("Click Here for Calories Calculation"):
        pred = check([User_ID,Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp])

    st.success(f"Your Calories Burn  is {pred}")

if __name__=='__main__':
    main()
    