**Spotify Song Prediction**

The Problem
Saat ini kemampuan untuk memprediksi sesuatu yang mungkin akan menjadi popular adalah riset yang penting bagi setiap industri. Terutama sekali bagi pertumbuhan dan kompetisi pada industri music. Sejak meluasnya penggunaan platform musik digital (Spotify, Billboard, Lastfm), data sangatlah mudah dijangkau dan perilaku pendengar bisa dengan mudah diobservasi. Hal ini memberikan kemudahan bagi teknik peramalan dan juga kerapkali digunakan pada sistem rekomendasi.

**Goals & Success**
Metrik yang digunakan adalah popularity. The Spotify Popularity Index memiliki range dari 0-sampai-100 yang menunjukkan peringkat seberapa popular seorang artis atau lagu relative terhadap artis dan track pada spotify.

**Key Solution**
Untuk melakukan analisa prediktif, didapatkan dataset dari 
Dataset yang digunakan adalah sebagai berikut :
1.	Accousticness   :	ukuran dari 0.0 to 1.0 apakah suatu track adalah akusting, dengan 1.0 merepresentasikan angka keyakinan yang tinggi bahwa suatu track adalah akustik.
2.	Danceability      :	Mendeskripsikan seberapa cocok suatu track untuk digunakan berdasa berdasarkan kombinasi dari elemen music termasuk tempo, stabilitas ritme, kekuatan beat dan keseluruhan Nilai 0.0 adalah kurang cocok untuk berdansa dan 1.0 adalah sangat cocok
3.	Duration            :	Panjang track dalam millisecond
4.	Energy               :	Ukuran dari 0.0 sampai dengan 1.0 yang merepresentasikan ukuran intensitas dan aktifitas. Track yang berenergi akan terasa capat dan riuh.
5.	Explicit	Apakah suatu track memiliki lirik yang eksplisit
6.	ID                     :	ID Spotify untuk suatu track
7.	Instumentalness :	Memprediksi agar suatu track tidak memiliki
8.	Key                   :	Kunci yang digunakan suatu track, menggunakan notasi standard pitch
9.	Liveliness           :	Mendeteksi keberadaan penonton di dalam rekaman. Nilai yang tinggi menunjukkan kemungkinan bahwa track direkam secara langsung. 
10.	Loudness           :	Tingkat kebisingan track dalam decibel (db)
11.	Mode                :	Mode mengindikasikan modality (mayor atau minor) dari suatu track, tipe dari tangga nada yang menurunkan melodi 
12.	Name               :	Nama
13.	Popularity         :	Popularitas dari track dengan nilai antara 0 dan 100, dengan 100 adalah paling popular. Dihitung  oleh algoritma dan didasarkan pada total jumlah suatu track diputar dan pemutaran terkini.
14.	Release Data     :	Tahun perilisan
15.	Speechiness      :	Mendeteksi keberadaan kata-kata dalam suatu track.
16.	Tempo             :	Tempo dari suatu track dalam ukuran beats per minute (BPM). 

Data diambil dari Kaggle dan algoritma yang digunakan untuk prediksi adalah  Random Forest.



**Key Flow**s
Project pipeline yang digunakan adalah end to end machine learning hingga deployment model. Struktur data dari Project disesuaikan dengan best practice dalam pembuatan machine learning di mana terdapat beberapa script phyton utama yang dijalankan yaitu :
1.	data_pipeline.py : berisikan modul terkait data collection, data validation
2.	preprocessing.py : berisikan modul terkait handling missing values
3.	Modeling : modul terkait baseline model, evaluation
4.	Pytest : modul pengetesan coding python
5.	Api.py dan Streamlit.Py : modul terkait API sebagai penghubung dengan user dan streamlit sebagai user interface. 
Untuk service API dan streamlit ditunjang menggunakan docker service sebagai virtual environment

**Launch Readiness**
Project dari timeline sesuai dengan deadline dari pengerjaan tugas proyek ML Process tanggal 9 November 2024

**Artifact**
Komponen yang digunakan dalam proyek ini yaitu Visual Studio Code, Jupyter Notebook, Google Chrome User, Git Hub, Git Bash, Docker. Adapun modul python yang digunakan adalah pandas, numpy, sklearn, matplotlib, seaborn, dan seterusnya

**References**
Spotify Data Analysis and Song Popularity Prediction : Sivasai Bhavanasi, Sahil Malla, V Manichetan, CVNJ Dhanush, Dr B Prakash
https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year
