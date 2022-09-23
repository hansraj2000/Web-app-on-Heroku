# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:29:26 2022

@author: Hans Raj
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# laoding the saved models

diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))

heart_model = pickle.load(open("heart_diease_model.sav",'rb'))

parkinsons_model = pickle.load(open("parkinsons_model.sav",'rb'))

breast_cancer_model = pickle.load(open("breast_cancer_model.sav",'rb'))

### sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons = ['activity','heart','person-fill',"gender-female"],
                           
                           default_index=0)
    
# Diabetes Prediction page
if selected == 'Diabetes Prediction':
    
    # page title
    st.title('Diabetes Prediction')
    
    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number od Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
          
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    
    with col1:
        DiabetesPedigramFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the Person")
    
    
    
    ## code fo prediction
    diab_dignosis = ''
    
    ## Creating a button for Prediction
    
    if st.button('Submit'):
        st.write("Diabetes Test Result")
        diab_dignosis = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                                                 Insulin,BMI,DiabetesPedigramFunction,Age]])
    
        if diab_dignosis[0] == 1:
            diab_dignosis = "The Person is Diabetic"
        else:
            diab_dignosis = "The Person is not Diabetic"

    st.success(diab_dignosis)


# Heart Disease Prediction page
if selected == 'Heart Disease Prediction':
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1 , col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex: 1=Male;0=Female',('select',1,0),index=0)
    with col3:
        cp = st.text_input('Chest Pain type')
    
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl')
    with col3:
        fbs = st.text_input("Fasting blood sugar>120mg/dl")
    
    with col1:
        restecg = st.text_input("Resting electrocardiographic result(values 0,1,2")
    with col2:
        thalach = st.text_input("Maximum heart rate achieved")
    with col3:
        exang = st.text_input("Exersice induced angina")
    
    with col1:
        oldpeak = st.text_input("Old Peak")
    with col2:
        slope = st.text_input("The Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    ## Code for Prediction
    diagnosis =''
    
    ## Creating a Button for prediction
    
    if st.button('Submit'):
        
        st.write("Heart Disease Test Result")
        res = heart_model.predict([[age, sex, cp, trestbps,
                                    chol, fbs, restecg, thalach, exang,
                                    oldpeak, slope, ca, thal]])        
        if res[0] == 0:
            diagnosis = 'The Person does not have a Heart Disease'
        else:
            diagnosis = "The Person has Heart Disease"
    
    st.success(diagnosis)
    
    
# Parkinsons Disease prediction page
if selected == 'Parkinsons Prediction':
    
    # page title
    st.title('Parkinsons Disease Prediction')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        FO = st.text_input('MDVP:Fo(Hz)')
    with col2:
        FHI = st .text_input('MDVP:Fhi(Hz)')
    with col3:
        FLO = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter = st.text_input('MDVPJitter(%)')
    
    with col1:
        jitter1 = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        RAP = st.text_input('MDVP:RAP')
    with col3:
        PPQ = st.text_input('MDVP:PPQ')
    with col4:
        DDP = st.text_input('Jitter:DDP')
    
    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col2:
        Shimmer1 = st.text_input('MDVP:Shimmer(dB)')
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        Spread1 = st.text_input('Spread 1')
    with col4:
        Spread2 = st.text_input('Spread 2')
        
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    ## Code for Predictoon
    diagnosis = ''
    
    ## Creating Button for Prediction
    if st.button('Submit'):
        
        st.write("Parkinsons Disease Test Result")
        res = parkinsons_model.predict([[FO, FHI, FLO, jitter, jitter1, RAP, PPQ, DDP,Shimmer,Shimmer1, APQ3, APQ5, APQ,
                                         DDA, NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]])
        
        if res[0] == 0:
            diagnosis = 'The Person does not have Parkinsons Disease'
        else:
            diagnosis = 'The Person have Parkinsons Disease'
            
    st.success(diagnosis)
        
        
# Breast Cancer prediction page
if selected == 'Breast Cancer Prediction':
    
    # page title
    st.title('Breast Cancer Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input("Mean Radius")
    with col2:
        mean_texture = st.text_input("Mean Texture")
    with col3:
        mean_perimeter = st.text_input("Mean Perimeter")
    
    with col1:
        mean_area = st.text_input("Mean Area")
    with col2:
        mean_smoothness = st.text_input("Mean Smoothness")
    with col3:
        mean_compactness = st.text_input("Mean Compactness")
    
    with col1:
        mean_cancavity = st.text_input("Mean Concavity")
    with col2:
        mean_cancave = st.text_input("Mean Concave points")
    with col3:
        mean_symmetry = st.text_input("Mean Symmetry")
    
    with col1:
        mean_fractal = st.text_input('Mean Fractal dimension')
    with col2:
        radius_error = st.text_input("Radius Error")
    with col3:
        texture_error = st.text_input("Texture Error")
    
    with col1:
        perimeter_error = st.text_input("Perimeter Error")
    with col2:
        area_error = st.text_input("Area Error")
    with col3:
        smoothness_error = st.text_input("Smoothness Error")
    
    with col1:
        compactness_error = st.text_input("Compactness Error")
    with col2:
        concavity_error = st.text_input("Concavity Error")
    with col3:
        concave_points = st.text_input('Concave Points Error')
    
    with col1:
        symmetry_error = st.text_input("Symmetry Error")
    with col2:
        fractal_error = st.text_input("Fractal Dimension Error")
    with col3:
        worst_radius = st.text_input("Worst Radius")
    
    with col1:
        worst_texture = st.text_input('Worst Texture')
    with col2:
        worst_perimeter = st.text_input('Worst Perimeter')
    with col3:
        worst_area = st.text_input("Worst Area")
    
    with col1:
        worst_smoothness = st.text_input("Worst Smoothness")
    with col2:
        worst_compactness = st.text_input("Worst Compactness")
    with col3:
        worst_concavity = st.text_input("Worst Concavity")
    
    with col1:
        worst_concave = st.text_input("Worst Concave Points")
    with col2:
        worst_symmetry = st.text_input("Worst Symmetry")
    with col3:
        worst_fractal = st.text_input("Worst Fractal Dimension")
        
    ## code for Prediction
    diagnosis = ''
    
    ## Creating button for Prediction
    
    if st.button("Submit"):
        
        st.write('Breast Cancer Test Result')
        res = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_cancavity, mean_cancave, mean_symmetry,
                                            mean_fractal, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points,
                                            symmetry_error, fractal_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity,
                                            worst_concave, worst_symmetry, worst_fractal]])
        
        if res[0] == 0:
            diagnosis = 'The Breast Cancer is Malignant'
        else:
            diagnosis = 'The Breast Cancer is Benign'
    
    st.success(diagnosis)
        
        
        
        
        
        
        
        
    