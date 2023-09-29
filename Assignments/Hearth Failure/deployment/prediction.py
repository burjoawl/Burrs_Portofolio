import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder


# Load All Files

load_model_rfc = joblib.load("best_model1.pkl")
load_model_abc = joblib.load("best_model2.pkl")

def run():
    
    with st.form ('key=hearth-failure'):
        age                       = st.number_input ('Usia', min_value = 0, max_value = 100,  value=25)
        sex                       = st.radio ('Jenis Kelamin', ('Laki-laki', 'Perempuan'), index=1, help ='Jenis Kelamin')
        smoking                   = st.radio('Perokok', ('Ya', 'Tidak'), index=1, help='Merokok atau tidak')
        time                      = st.number_input ('Waktu Penangangan', min_value = 0, max_value = 300, value=0)
        st.markdown('---')

        anaemia                   = st.radio('Anemia', ('Ya', 'Tidak'), index=1, help='Anemia atau tidak')
        creatinine_phosphokinase  = st.number_input('Kreatinin Fosfokinase', min_value=0, max_value=8000, value=100)
        diabetes                  = st.radio('Diabetes', ('Ya', 'Tidak'), index=1, help='Diabetes atau tidak')
        ejection_fraction         = st.number_input('Ejection Fraction', min_value=0, max_value=100, value=50)
        high_blood_pressure       = st.radio('Tekanan Darah Tinggi', ('Ya', 'Tidak'), index=1, help='Tekanan darah tinggi atau tidak')
        platelets                 = st.number_input('Platelets', min_value=25000, max_value=850000, value=300000)
        serum_creatinine          = st.number_input('Kreatinin Serum', min_value=0.0, max_value=10.0, value=3.0, format="%.1f", step=0.1)
        serum_sodium              = st.number_input('Natrium Serum', min_value=110, max_value=150, value=135)
       
        submitted = st.form_submit_button('Prediksi')

    data_inf = {
        'Usia': age,
        'Jenis Kelamin': sex,
        'Perokok': smoking,
        'Waktu Penangangan': time,
        'Anemia': anaemia,
        'Kreatinin Fosfokinase': creatinine_phosphokinase,
        'Diabetes': diabetes,
        'Ejection Fraction': ejection_fraction,
        'Tekanan Darah Tinggi': high_blood_pressure,
        'Platelet': platelets,
        'Kreatinin Serum': serum_creatinine,
        'Natrium Serum': serum_sodium
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # Konversi menjadi 1 dan 0 
    sex                 = 1 if sex == 'Laki-laki' else 0
    smoking             = 1 if smoking == 'Ya' else 0
    anaemia             = 1 if anaemia == 'Ya' else 0
    diabetes            = 1 if diabetes == 'Ya' else 0
    high_blood_pressure = 1 if high_blood_pressure == 'Ya' else 0

    data_inf_fit = pd.DataFrame({
                'Usia': age, 
                'Anemia': anaemia, 
                'Kreatinin Fosfokinase': creatinine_phosphokinase, 
                'Ejection Fraction': ejection_fraction, 
                'Tekanan Darah Tinggi': high_blood_pressure, 
                'Kreatinin Serum': serum_creatinine, 
                'Natrium Serum': serum_sodium, 
                'Waktu Penangangan': time
            }, index=[0])
     
    pilihan_model= st.sidebar.selectbox ('Pilih Model :', ('Random Forest Classification', 'AdaBoost'))
    if pilihan_model == 'Random Forest Classification':
        load_model = load_model_rfc
    else:
        load_model = load_model_abc

    if submitted: 
        new_data_pred = load_model.predict(data_inf_fit)
        if new_data_pred == 0:
            st.write('# Meninggal Atau Tidak : \nTidak Meninggal')
        else:
            st.write('# Meninggal Atau Tidak : \nMeninggal')


if __name__ == '__main__':
    run()