import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title = 'Churn Risk - EDA'
)

def run():
        
    # Membuat Title
    st.title ('Farhan\'s Churn Rate Illustration')

    # Membuat Sub Header
    st.subheader ('EDA for Churn Analyst')

    # Menambahkan Gambar
    image = Image.open('img1.jpg')
    st.image(image, caption ='Churn Illustration')

    # Menambahkan Deskripsi
    st.write ('Page created by **Farhan** for Phase 2 Milestone 1 Hacktiv8 Assignment')

    # Membuat Garis Lurus
    st.markdown ('---')

    # Show DataFrame
    st.write ('### Excel Data')
    df = pd.read_csv ('https://huggingface.co/spaces/burjoawl/H8_Churn_Risk_Score/raw/main/churn.csv')
    st.dataframe(df)

    # Show statistik
    st.write('### Statistical Data')
    st.dataframe(df.describe().T)

    # Membuat Garis Lurus
    st.markdown ('---')

    # Filter Churn
    st.write ('# Churn Situation')
    pilihan_kondisi = st.sidebar.selectbox ('Select :', ('Churn', 'Not Churn'))
    kolom = ['age', 'gender', 'region_category', 'membership_category',
       'joining_date', 'joined_through_referral', 'preferred_offer_types',
       'medium_of_operation', 'internet_option', 'last_visit_time',
       'days_since_last_login', 'avg_time_spent', 'avg_transaction_value',
       'avg_frequency_login_days', 'points_in_wallet', 'used_special_discount',
       'offer_application_preference', 'past_complaint', 'complaint_status',
       'feedback']
    
    data_churn         = df[df['churn_risk_score'] == 1][kolom]
    data_tidak_churn   = df[df['churn_risk_score'] == 0][kolom]
    
    if pilihan_kondisi == 'Churn':
        kondisi = data_churn
    else:
        kondisi = data_tidak_churn
    kondisi['gender'] = kondisi['gender'].map({'M': 'Male', 'F': 'Female', 'null':'Not Defined'})

    # Mulai pembuatan grafik

    # Membuat Bar Chart Age
    st.write(f'### Age Distribution of {pilihan_kondisi}')
    age_counts = kondisi['age'].value_counts()
    st.bar_chart(data=age_counts.rename("Age Counts"))

    # Membuat Pie Chart Gender
    st.write(f'### Gender Comparison of {pilihan_kondisi}')
    fig = px.pie (kondisi, names = 'gender')
    fig.update_traces(hovertemplate='%{label}: %{value} (%{percent})')
    st.plotly_chart(fig)

    # Membuat Pie Chart Region
    st.write(f'### Region Comparison of {pilihan_kondisi}')
    fig = px.pie (kondisi, names = 'region_category')
    fig.update_traces(hovertemplate='%{label}: %{value} (%{percent})')
    st.plotly_chart(fig)

    # Membuat Bar Chart Age
    st.write(f'### Membership Distribution of {pilihan_kondisi}')
    membership_counts = kondisi['membership_category'].value_counts()
    membership_order = ['No Membership', 'Basic Membership', 'Silver Membership', 'Platinum Membership', 'Gold Membership', 'Premium Membership']
    membership_counts = membership_counts.reindex(membership_order)
    
    fig = px.bar(x=membership_counts.index, y=membership_counts, labels={'x': 'Membership Category', 'y': 'Membership Counts'})

    st.plotly_chart(fig)

    # Membuat Bar Chart Media
    st.write(f'### Medium Operation of {pilihan_kondisi}')
    medium_counts = kondisi['medium_of_operation'].value_counts()
    medium_order = ['Desktop', 'Smartphone', 'Both']
    medium_counts = medium_counts.reindex(medium_order)
    
    fig = px.bar(x=medium_counts.index, y=medium_counts, labels={'x': 'Medium Category', 'y': 'Medium Counts'})

    st.plotly_chart(fig)

if __name__ == '__main__':
    run()