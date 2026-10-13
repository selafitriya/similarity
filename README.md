# ✨ Kalkulator Kemiripan Kalimat (Cosine Similarity)

Aplikasi web interaktif dan edukatif berbasis **Streamlit** untuk membandingkan tingkat kemiripan antara dua kalimat menggunakan metode **Cosine Similarity**. 

Aplikasi ini tidak hanya menampilkan skor angka, tetapi juga **menjelaskan alasan**, **menyorot kata-kata yang cocok**, dan **membedah langkah perhitungannya** dengan bahasa santai yang mudah dipahami!

---

## 🚀 Cara Menjalankan Aplikasi

### Cara 1: Paling Mudah (Tinggal Klik 2x)
Cukup **klik dua kali** file [`jalankan.bat`](file:///c:/Users/LENOVO/Downloads/cosinus%20similarity/jalankan.bat). Aplikasi akan otomatis membuka terminal dan browser di `http://localhost:8501`.

### Cara 2: Lewat Terminal / PowerShell
Buka Terminal atau PowerShell di folder ini, lalu jalankan salah satu perintah berikut:
```bash
streamlit run app.py
```
atau jika perintah di atas belum terdeteksi di terminal lama:
```bash
python -m streamlit run app.py
```

Setelah itu, buka browser di alamat:  
👉 **http://localhost:8501**

---

## 💡 Fitur Utama yang Menyenangkan

1. **🎯 Tombol Coba Cepat (Presets)**  
   Coba langsung berbagai skenario menarik:
   - 🍔 **Kuliner** (Kemiripan Tinggi)
   - 💻 **Belajar Coding** (Kemiripan Sedang-Tinggi)
   - ☕ **Santai & Hobi** (Kemiripan Sedang)
   - 🪐 **Beda Total (0%)** (Topik sama sekali berbeda)

2. **👀 Peta Kata yang Cocok (Visual Word Highlighter)**  
   Kata-kata yang muncul di kedua kalimat langsung disorot dengan warna hijau toska terang, sehingga kamu langsung tahu kata apa saja yang membuat kedua kalimat tersebut mirip!

3. **💬 Mengapa Skornya Segitu? (Penjelasan Alasan)**  
   Menceritakan secara logis berapa kata yang sama, berapa kata unik masing-masing kalimat, dan kenapa skornya bisa segitu.

4. **🧮 Langkah Demi Langkah (Step-by-Step Perhitungan)**  
   Membongkar rumus matematika menjadi 5 langkah santai:
   - **Langkah 1**: Pembersihan Kata (Preprocessing)
   - **Langkah 2**: Mengumpulkan Kamus Kata Unik (Vocabulary)
   - **Langkah 3**: Menghitung Skor Kata yang Sama (Dot Product)
   - **Langkah 4**: Menghitung Panjang Kalimat (Norma Euclidean)
   - **Langkah 5**: Pembagian Akhir (Skor Cosine)

5. **📊 Daftar Kata & Grafik Perbandingan**  
   Tabel frekuensi kata yang rapi dan grafik batang interaktif untuk melihat distribusi kata.

6. **💡 Analogi Santai & Konsep Dasar**  
   Penjelasan analogi arah panah dan pesanan makanan restoran agar konsep Cosine Similarity benar-benar nempel di kepala.

---

## 📁 Struktur File
- [`app.py`](file:///c:/Users/LENOVO/Downloads/cosinus%20similarity/app.py) : Kode aplikasi Streamlit utama.
- [`jalankan.bat`](file:///c:/Users/LENOVO/Downloads/cosinus%20similarity/jalankan.bat) : Skrip instan sekali klik untuk menjalankan aplikasi di Windows.
- [`requirements.txt`](file:///c:/Users/LENOVO/Downloads/cosinus%20similarity/requirements.txt) : Daftar pustaka Python (`streamlit`, `pandas`, `altair`).
