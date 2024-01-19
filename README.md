# Music Finder
## Dataset 
Untuk dataset yang didapat, bersumber dari laman kaggle.com, yaitu laman penyedia dataset-dataset yang bersifat publik. Dataset yang dipakai bernama Music Dataset dari Zulqarnain Ali. Musik-musik yang ada dalam dataset berjumlah 28371 dan musik-musiknya rilis tahun dari 1960 hingga 2019, cocok untuk user yang ingin bernostalgia. Atribut-atribut yang ada adalah artist_name, track_name, release_date, genre, lyrics, len, dating, violence, world/life, night/time, shake the audience, family/gospel, romantic, communication, obscene, music, movement/places, light/visual perceptions, family/spiritual, like/girls, sadness, feelings, danceability, loudness, acousticness, instrumentalness, valence, energy, topic, age.

Atribut yang digunakan untuk proses pengolahan data adalah artist_name, track_name, release_date, genre, lyric, dan topic.

## Permasalahan dan Tujuan Eksperimen
Dari dataset ini, yang saya lakukan adalah membuat **Sistem Rekomendasi Musik Dengan Metode Cosine Similarity**. Dengan memasukan suatu judul lagu, maka nanti akan menghasilkan lagu-lagu yang mirip dari lagu yang dicari berdasarkan lirik dari lagu.

## Model dan Alur Tahapan Eksperimen
Model yang digunakan adalah **Cosine Similarity**, yaitu model yang membandingan tingkat kemiripan dari data A dengan data B.
Untuk alur tahapan eksperimen, yaitu:

1. Membaca file csv
2. Karena terlalu banyak lagu, maka akan dibatasi dari tahun 2000 hingga 2019
3. Mengambil 6 atribut yang nanti akan dipakai (artist_name, track_name, release_date, genre, lyric, topic).
4. Melakukan stopwords
5. Normalisasi dokumen untuk mengecilkan semua huruf dan menghilangkan *special characters* dari suatu dokumen
6. Dokumen yang diambil adalah dokumen dari atribut lyric
7. Membuat function untuk sistem rekomendasi musik dengan metode cosine similarity
8. Perlu diingat, tidak semua musik dapat dicari kecuali musik yang dicari ada pada dalam dataset, jika menjalankan program ini dan musik yang dicari tidak ada, maka hasilnya akan error, jika musik yang dicari ada, maka akan mendapatkan values berupa interger yang sama dengan musik yang ada pada dataset (ini untuk proses pengecekan musik)
9. Setelah sistem menemukan musik yang dicari user, sistem akan mencari values yang sama pada musik dalam dataset, lalu mencari musik mana saja yang mirip dengan musik yang dicari user berdasarkan kemiripan lirik
10. Nanti output yang dihasilkan adalah musik-musik yang memiliki kemiripan dengan musik yang dicari user

## Performa Model atau Uji Performa Model


## Proses Deployment
Untuk deployment, saya menggunakan 2 framework, Streamlit dan Django. 
