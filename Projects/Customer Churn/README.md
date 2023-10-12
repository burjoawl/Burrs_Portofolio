## Deployment Link
https://huggingface.co/spaces/burjoawl/H8_Churn_Risk_Score

# Customer Churn
Sebuah perusahaan ingin meminimalisir resiko seorang customer untuk berhenti memakai produk yang mereka tawarkan. Bantulah perusahaan tersebut untuk memprediksi customer yang akan berhenti (churn) dari dataset yang diberikan.

## Fitur
Pada projek ini, terdapat fitur seperti:
- Data loading dan pengecekan data
- Mengkondisikan dan eksplorasi data
- Pembuatan dan pelatihan Model Machine Learning
- Deploy menggunakan Streamlit

## Teknologi
Teknologi yang digunakan adalah:
- Python (Bahasa Pemrograman)
- Scikit-Learn & Tensorflow (Machine Learning)
- Streamlit (Deployment)

## Kesimpulan
1. Eksplorasi Data
Dari data yang ada terdapat 54.1% customer churn yang dapat dilihat dari:
- Tidak terlihat adanya karakteristik pada kisaran umur.
- Lebih banyak gender *Female* dibandingkan *Male*.
- Yang terbanyak adalah bertempat tinggal di *Town*, diikuti oleh *City* dan terakhir *Village*

2. Model
Model yang paling bagus merupakan Model Functional Improvement yang memilii nilai akurasi *goodfit* sebesar 93%, model tersebut dapat memprediksi customer mana yang akan churn ataupun tidak dengan baik.