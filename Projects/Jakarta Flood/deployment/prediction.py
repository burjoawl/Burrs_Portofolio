import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder


# Load All Files

load_model = joblib.load("best_model.pkl")
pipe = joblib.load('pipeline.joblib')

def run():
    
    with st.form ('key=banjir'):
        st.write('### Masukkan Data')

        suhu_min                  = st.number_input ('Suhu Minimal', min_value = 20.0, max_value = 40.0, value=20.0, format="%.1f", step=0.1)
        suhu_max                  = st.number_input ('Suhu Maksimal', min_value = 20.0, max_value = 40.0, value=20.0, format="%.1f", step=0.1)
        suhu_rata                 = st.number_input ('Suhu Rata-rata', min_value = 20.0, max_value = 40.0, value=20.0, format="%.1f", step=0.1)
        st.markdown('---')

        kelembaban_rata           = st.number_input ('Kelembaban Rata-rata', min_value = 0.0, max_value = 100.0, value=50.0, format="%.1f", step=0.1)
        curah_hujan_rata          = st.number_input ('Curah Hujan Rata-rata', min_value = 0.0, max_value = 10.0, value=0.0, format="%.1f", step=0.1)
        durasi_cerah              = st.number_input ('Kecepatan Angin Rata-rata', min_value = 0.0, max_value = 12.0, value=0.0, format="%.1f", step=0.1)
        kecepatan_angin_max       = st.number_input ('Kecepatan Angin Maksimal', min_value = 0.0, max_value = 12.0, value=0.0, format="%.1f", step=0.1)
        arah_angin_max            = st.number_input ('Arah Angin Maksimal', min_value = 0.0, max_value = 360.0, value=0.0, format="%.1f", step=0.1)
        kecepatan_angin_rata      = st.number_input ('Kecepatan Angin Rata-rata', min_value = 0.0, max_value = 10.0, value=0.0, format="%.1f", step=0.1)
        st.markdown('---')

        nama_daerah               = st.radio ('Nama Daerah', ('Jakarta Utara', 'Jakarta Timur', 'Jakarta Pusat', 'Jakarta Selatan'), index=1, help ='Daerah')
       
        submitted = st.form_submit_button('Prediksi')
    
    data = {
        'Suhu Minimal': suhu_min,
        'Suhu Maksimal': suhu_max,
        'Suhu Rata-rata': suhu_rata,
        'Kelembaban Rata-rata': kelembaban_rata,
        'Curah Hujan Rata-rata': curah_hujan_rata,
        'Kecepatan Angin Rata-rata': durasi_cerah,
        'Kecepatan Angin Maksimal': kecepatan_angin_max,
        'Arah Angin Maksimal': arah_angin_max,
        'Kecepatan Angin Rata-rata': kecepatan_angin_rata,
        'Nama Daerah': nama_daerah
    }
    data = pd.DataFrame([data])
    st.dataframe(data)

    data_inf = pd.DataFrame({
        'suhu_min' : suhu_min,
        'suhu_max': suhu_max,
        'suhu_rata': suhu_rata,
        'kelembaban_rata': kelembaban_rata,
        'curah_hujan_rata': curah_hujan_rata,
        'durasi_cerah': durasi_cerah,
        'kecepatan_angin_max': kecepatan_angin_max,
        'arah_angin_max': arah_angin_max,
        'kecepatan_angin_rata': kecepatan_angin_rata,
        'nama_daerah': nama_daerah
    }, index=[0])

    if submitted: 
        new_data_encoded = pipe.transform(data_inf)
        new_data_pred = load_model.predict(new_data_encoded)
        if new_data_pred == 0:
            st.write('# Banjir Atau Tidak : \nTidak Banjir')
        else:
            st.write('# Banjir Atau Tidak : \nBanjir')


if __name__ == '__main__':
    run()