import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title = 'Gagal Jantung - EDA'
)

def run():
        
    # Membuat Title
    st.title ('Prediksi Pasien Gagal Jantung')

    # Membuat Sub Header
    st.subheader ('EDA untuk Analisa Dataset Hearth Failure')

    # Menambahkan Gambar
    image = Image.open('img1.png')
    st.image(image, caption ='Gagal Jantung Sistolik dan Diastolik')

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
    df = pd.read_csv ('https://huggingface.co/spaces/burjoawl/deployment/raw/main/h8dsft_P1G3_Farhan.csv')
    df.rename(columns={'age': 'Usia',
                       'anaemia': 'Anemia',
                       'creatinine_phosphokinase': 'Kreatinin Fosfokinase', 
                       'diabetes': 'Diabetes',
                       'ejection_fraction': 'Ejection Fraction',
                       'high_blood_pressure': 'Tekanan Darah Tinggi',
                       'platelets': 'Platelet',
                       'serum_creatinine': 'Kreatinin Serum',
                       'serum_sodium': 'Natrium Serum',
                       'sex': 'Jenis Kelamin', 
                       'smoking': 'Perokok',
                       'time': 'Waktu Penangangan',
                       'DEATH_EVENT': 'Meninggal'}
                       , inplace=True)
    st.dataframe(df)

    # Show statistik
    st.write('### Data Statistik')
    st.dataframe(df.describe().T)

    st.write('### Korelasi Kolom')
    fig, ax = plt.subplots()
    fig = px.imshow(df.corr().abs())
    st.write(fig)

    # Membuat Garis Lurus
    st.markdown ('---')

    # Filter Meninggal atau tidak
    st.write ('# Kondisi Pasien')
    pilihan_pasien = st.sidebar.selectbox ('Pilih Kondisi :', ('Meninggal', 'Tidak Meninggal'))
    data_meninggal  = df[df['Meninggal'] == 1][['Usia', 'Anemia', 'Kreatinin Fosfokinase', 'Diabetes',
                                            'Ejection Fraction', 'Tekanan Darah Tinggi', 'Platelet',
                                            'Kreatinin Serum', 'Natrium Serum', 'Jenis Kelamin', 'Perokok', 'Waktu Penangangan']]
    data_hidup      = df[df['Meninggal'] == 0][['Usia', 'Anemia', 'Kreatinin Fosfokinase', 'Diabetes',
                                            'Ejection Fraction', 'Tekanan Darah Tinggi', 'Platelet',
                                            'Kreatinin Serum', 'Natrium Serum', 'Jenis Kelamin', 'Perokok', 'Waktu Penangangan']]
    
    if pilihan_pasien == 'Meninggal':
        data_pasien = data_meninggal
    else:
        data_pasien = data_hidup

    # Membuat Histogram Berdasarkan Input
    st.write ('### Pie Chart pada tiap kategori')
    if pilihan_pasien == 'Meninggal':
        st.write ('### Data Meninggal')
    else:
        st.write ('### Data Hidup')
    pilihan = st.radio ('Pilih Kategori :', ('Anemia', 'Diabetes', 'Tekanan Darah Tinggi', 'Jenis Kelamin', 'Perokok'), horizontal=True)
    if pilihan == 'Jenis Kelamin':
        data_pasien[pilihan] = data_pasien[pilihan].map({0: 'Perempuan', 1: 'Laki-Laki'})
    else:
        data_pasien[pilihan] = data_pasien[pilihan].map({0: 'Tidak', 1: 'Ya'})
    
    fig = px.pie (data_pasien, names = pilihan)
    fig.update_traces(hovertemplate='%{label}: %{value} (%{percent})')
    st.plotly_chart(fig)
    
    # Membuat Barplot
    st.write('### Distribusi Usia')
    if pilihan_pasien == 'Meninggal':
        st.write ('### Data Meninggal')
    else:
        st.write ('### Data Hidup')
    age_counts = df['Usia'].value_counts()
    st.bar_chart(data=age_counts.rename("Jumlah Pasien"))

    # Membuat Histogram dari Waktu Penanganan
    st.write('### Distibusi Waktu Penanganan')
    if pilihan_pasien == 'Meninggal':
        st.write ('### Data Meninggal')
    else:
        st.write ('### Data Hidup')
    fig = plt.figure(figsize=(15, 5))
    ax = sns.histplot(data_pasien['Waktu Penangangan'], bins=30)
    st.pyplot (fig)

    # Membuat Plotly Plot
    st.write ('### Grafik Perbandingan Antar Kolom')
    if pilihan_pasien == 'Meninggal':
        st.write ('#### Data Meninggal')
    else:
        st.write ('#### Data Hidup')

    col1, col2 = st.columns(2)
    selected_column_x = col1.selectbox("Kolom X", data_pasien.columns, index=0)
    selected_column_y = col2.selectbox("Kolom Y", data_pasien.columns, index=1)

    fig = px.scatter(data_pasien, x=selected_column_x, y=selected_column_y, hover_data=['Usia', 'Jenis Kelamin', 'Perokok'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()