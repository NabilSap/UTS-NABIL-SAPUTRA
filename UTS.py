ESSAY

1.Jelaskan apa yang dimaksud dengan Machine Learning?
Machine Learning (Pembelajaran Mesin) adalah cabang dari kecerdasan buatan (Artificial Intelligence) yang memungkinkan sistem untuk belajar dan meningkatkan kinerja mereka secara otomatis melalui pengalaman tanpa harus diprogram secara eksplisit. Dalam praktiknya, machine learning melibatkan penggunaan algoritma dan model statistik untuk menganalisis dan menarik kesimpulan dari data, serta membuat prediksi atau keputusan berdasarkan pola yang telah dikenali dalam data tersebut.

2.Berikan contoh penerapan implemetasi dalam kehidupan sehari-hari terkait Machine Learning. Dan
jelaskan mengapa membutuhkannya dan manfaatnya?

  Sistem Rekomendasi (Recommendation Systems)
Contoh: Netflix, Spotify, Amazon.
Mengapa dibutuhkan: Untuk menyarankan konten atau produk yang relevan kepada pengguna 	berdasarkan preferensi dan perilaku mereka.
Manfaat: Meningkatkan pengalaman pengguna dengan menyediakan konten yang sesuai dengan minat 	mereka, meningkatkan keterlibatan pengguna, dan meningkatkan penjualan atau konsumsi konten.

3.Jelaskan macam-macam taxonomi dalam pengerapan Machine Learning?

Dalam penerapan machine learning, algoritma dan model dapat diklasifikasikan ke dalam beberapa kategori berdasarkan cara mereka belajar dan jenis masalah yang mereka selesaikan. Berikut adalah beberapa taksonomi utama dalam machine learning:

* Pembelajaran Terawasi (Supervised Learning)
Penjelasan: Algoritma ini dilatih menggunakan data berlabel, di mana setiap input memiliki label output yang diketahui.
Contoh Algoritma: Regresi Linear, K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Random Forest.
Penggunaan: Prediksi harga rumah, klasifikasi email spam, diagnosis medis.
Manfaat: Memberikan prediksi yang akurat dan dapat diandalkan ketika data label tersedia.

* Pembelajaran Tak Terawasi (Unsupervised Learning)
Penjelasan: Algoritma ini digunakan dengan data yang tidak berlabel, bertujuan untuk menemukan struktur atau pola yang tersembunyi dalam data.
Contoh Algoritma: K-Means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA), Association Rules.
Penggunaan: Segmentasi pelanggan, deteksi anomali, pengurangan dimensi data.
Manfaat: Membantu mengidentifikasi pola yang tidak terduga dan menemukan informasi yang berguna tanpa memerlukan label data.

* Pembelajaran Semi-Terawasi (Semi-Supervised Learning)
Penjelasan: Algoritma ini memanfaatkan kombinasi data berlabel dan tidak berlabel untuk meningkatkan pembelajaran.
Contoh Algoritma: Semi-Supervised SVM, Label Propagation, Co-Training.
Penggunaan: Situasi di mana pelabelan data mahal atau sulit, seperti dalam pengenalan gambar dan analisis teks.
Manfaat: Mengurangi kebutuhan akan data berlabel yang besar dan mahal, sementara tetap meningkatkan kinerja model.

STUDY KASUS

1.) a) Berapa rata-rata mahasiswa datang pada minggu ini?
Rata-rata mahasiswa datang pada minggu ini adalah 3.2 orang per hari. Rata-rata = Total datang / Total hari = 19 / 7 = 3.2 orang per hari
b) Kapan biaya tertinggi terjadi?
Biaya tertinggi terjadi pada hari Sabtu, dengan total biaya Rp 150.000.
c) Hari apa biaya lebih dari 110000?
Biaya lebih dari 110.000 terjadi pada hari Selasa dan Sabtu.
d) Siapa yang paling banyak datang ke kampus?
Ani paling banyak datang ke kampus, dengan total 11 hari.
e) Siapa yang datang pada hari Minggu?
Ani dan Budi datang pada hari Minggu.
f) Berapa biaya tertinggi dan terendah?
Biaya tertinggi adalah Rp 150.000 pada hari Sabtu, dan biaya terendah adalah Rp 15.000 pada hari Kamis.
g) Berapa frekuensi datang tertinggi dan terendah?
Frekuensi datang tertinggi adalah 5 kali, terjadi pada Ani pada hari Sabtu.
Frekuensi datang terendah adalah 1 kali, terjadi pada Lono pada hari Kamis.

2.) import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "fakultas": ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"],
    "jumlah_mahasiswa": [260, 28, 284, 465, 735],
    "akreditasi": ["A", "A", "B", "A", "A"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df["fakultas"], df["jumlah_mahasiswa"], color=['red', 'green', 'blue', 'cyan', 'magenta'])

# Adding the text labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom') # va: vertical alignment

# Labels and title
plt.xlabel("Fakultas")
plt.ylabel("Jumlah Mahasiswa")
plt.title("Jumlah Mahasiswa per Fakultas")
plt.show()
