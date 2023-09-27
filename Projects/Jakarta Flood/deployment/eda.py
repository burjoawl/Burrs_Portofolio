import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title = 'Banjir Kota Jakarta - EDA'
)

def run():
        
    # Membuat Title
    st.title ('Prediksi Banjir Atau Tidaknya Kota Jakarta')

    # Membuat Sub Header
    st.subheader ('EDA untuk Analisa Dataset')

    # Menambahkan Gambar
    image = Image.open('img1.jpg')
    st.image(image, caption ='Monas, Jakarta')

    # Menambahkan Deskripsi
    st.write ('Page ini dibuat oleh **Farhan** untuk pengerjaan tugas Fase 1 Graded Challenge 3')

    # Membuat Garis Lurus
    st.markdown ('---')

    # Magic Syntax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana.

    Dataset yang digunakan dalah dataset hearth failure.

    Dataset ini berasal dari data Hacktiv8
    '''

    # Show DataFrame
    st.write ('### Data Excel')
    df = pd.read_csv ('E:/2. Kerja/Hacktiv8/Phase 1/Tugas/streamlit/H8-Banjir-Jakarta/h8dsft_P1M2_Farhan_trim.csv')
    df.rename(columns={'suhu_min': 'Suhu Minimal',
                       'suhu_max': 'Suhu Maksimal',
                       'suhu_rata': 'Suhu Rata-Rata',
                       'kelembaban_rata': 'Kelembaban Rata-Rata',
                       'curah_hujan_rata': 'Curah Hujan Rata-Rata',
                       'durasi_cerah': 'Durasi Cerah',
                       'kecepatan_angin_max': 'Kecepatan Angin Maksimal',
                       'arah_angin_max': 'Arah Angin Maksimal',
                       'kecepatan_angin_rata': 'Kecepatan Angin Rata-Rata',
                       'nama_daerah': 'Nama Daerah',
                       'banjir': 'Banjir'}
                       , inplace=True)
    st.dataframe(df)

    # Show statistik
    st.write('### Data Statistik')
    st.dataframe(df.describe().T)

    st.write('### Korelasi Kolom')
    numeric_features = df.select_dtypes(include=np.number).columns.tolist()
    fig, ax = plt.subplots()
    fig = px.imshow(df[numeric_features].corr().abs())
    st.write(fig)

    # Membuat Garis Lurus
    st.markdown ('---')

    # Filter Banjir atau tidak
    st.write ('# Kondisi')
    pilihan_kondisi = st.sidebar.selectbox ('Pilih Kondisi :', ('Banjir', 'Tidak Banjir'))
    kolom = ['Suhu Minimal', 'Suhu Maksimal', 'Suhu Rata-Rata', 'Kelembaban Rata-Rata', 'Curah Hujan Rata-Rata', 'Durasi Cerah', 
         'Kecepatan Angin Maksimal', 'Arah Angin Maksimal','Kecepatan Angin Rata-Rata', 'Nama Daerah']
    data_banjir         = df[df['Banjir'] == 1][kolom]
    data_tidak_banjir   = df[df['Banjir'] == 0][kolom]
    
    if pilihan_kondisi == 'Banjir':
        kondisi = data_banjir
    else:
        kondisi = data_tidak_banjir

    # Membuat Pie Chart

    st.write('### Pie Chart Banjir')
    fig = px.pie(kondisi, names='Nama Daerah')
    fig.update_traces(hovertemplate='%{label}: %{value} (%{percent})')
    st.plotly_chart(fig)

    # Membuat Plotly Plot
    st.write ('### Grafik Perbandingan Antar Kolom')
    if pilihan_kondisi == 'Banjir':
        st.write('#### Data Banjir')
    else:
        st.write('#### Data Tidak Banjir')

    col1, col2 = st.columns(2)
    selected_column_x = col1.selectbox("Kolom X", kondisi.columns, index=0)
    selected_column_y = col2.selectbox("Kolom Y", kondisi.columns, index=1)

    fig = px.scatter(kondisi, x=selected_column_x, y=selected_column_y)
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()