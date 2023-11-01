# Judul project
Analisis Waktu Penyelesaian Tindak Kejahatan Pencurian di Kota Austin sepanjang Tahun 2016

# Tujuan project 
Menganalisa waktu terselesaikannya tindak kejahatan 'Theft' yang merupakan tindak kejahatan paling banyak pada Kota Austin sepanjang tahun 2016

# Masalah yang diselesaikan
Perbandingan Tingkat Kejahatan Theft dengan Kejahatan Lainnya

# Latar belakang masalah
Kota Austin, seperti banyak wilayah perkotaan lainnya, memiliki berbagai tantangan dalam menjaga keamanan dan ketertiban masyarakat. Salah satu jenis kejahatan yang kerap menjadi perhatian adalah kejahatan pencurian (Theft). Kejahatan ini dapat merugikan warga, mengganggu stabilitas sosial, dan menciptakan ketidakamanan di dalam masyarakat. Selama tahun 2016, kejahatan Theft di Kota Austin tampaknya menjadi salah satu tindak kejahatan yang paling sering terjadi.

# Output project
Laporan analisis kejahatan pencurian tahun 2016 di kota Austin.

# Data yang digunakan
BigQuery
```
SELECT *                                        # Mengambil semua kolom yang ada
FROM bigquery-public-data.austin_crime.crime    # Tabel asal BigQuery
```

# Metode yang dipakai
Menggunakan SQL untuk mengambil data yang diperlukan dalam melakukan analisis permasalahan yang akan diteliti

# Stack yang dipakai
- SQL & Python (Bahasa Pemrograman)

# Penjelasan file yang digunakan 
- File yang digunakan berasal dari BigQuery tentang kota Austin

# Kelebihan dan kekurangan project
- Kelebihan
Tidak perlu membuka web BigQuery sehingga lebih mudah untuk mengambil data

- Kekurangan
Kurangnya visualisasi untuk memahami isi secara optimal