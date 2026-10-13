import math
import re
import html
import pandas as pd
import altair as alt
import streamlit as st

# ==============================================================================
# KONFIGURASI HALAMAN
# ==============================================================================
st.set_page_config(
    page_title="Kalkulator Kemiripan Kalimat (Cosine Similarity)",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# CUSTOM CSS: TEMA CERAH, SEGAR, MODERN & WARNA HARMONIS (TIDAK NABRAK)
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Background Utama: Nuansa Terang, Lembut & Bersih */
.stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #f0fdf4 45%, #fff7ed 80%, #fdf2f8 100%) !important;
    color: #1e293b;
}

/* Header Banner: Biru Laut Cerah dengan Sentuhan Modern */
.hero-container {
    background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
    border: 1.5px solid #bae6fd;
    border-radius: 20px;
    padding: 24px 28px;
    margin-bottom: 22px;
    box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.12);
    position: relative;
    overflow: hidden;
}

.hero-container::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, #0284c7 0%, #10b981 35%, #f59e0b 70%, #ec4899 100%);
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #e0f2fe;
    border: 1px solid #7dd3fc;
    color: #0369a1;
    padding: 5px 14px;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero-title {
    font-size: 2.1rem;
    font-weight: 800;
    margin: 0 0 6px 0;
    color: #0f172a;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    font-size: 1.02rem;
    color: #475569;
    margin: 0;
    line-height: 1.5;
}

/* Header Kotak Input: Biru Laut & Pink Manis */
.card-header-a {
    background: #e0f2fe;
    border-left: 5px solid #0284c7;
    border-top: 1px solid #bae6fd;
    border-right: 1px solid #bae6fd;
    padding: 10px 16px;
    border-radius: 14px 14px 0 0;
    font-weight: 700;
    color: #0369a1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.95rem;
}

.card-header-b {
    background: #fce7f3;
    border-left: 5px solid #ec4899;
    border-top: 1px solid #fbcfe8;
    border-right: 1px solid #fbcfe8;
    padding: 10px 16px;
    border-radius: 14px 14px 0 0;
    font-weight: 700;
    color: #9d174d;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.95rem;
}

.token-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    background: #ffffff;
    padding: 3px 10px;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    color: #334155;
    font-weight: 600;
}

/* Tombol Hitung: Gradasi Biru Laut ke Hijau Segar */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 50%, #10b981 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 1.08rem !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 14px 28px !important;
    box-shadow: 0 4px 15px rgba(2, 132, 199, 0.28) !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
    margin-top: 6px !important;
    margin-bottom: 18px !important;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(2, 132, 199, 0.4) !important;
}

/* Tiga Kartu Ringkas Atas */
.summary-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    text-align: center;
    border: 1.5px solid #e2e8f0;
}

.summary-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}

.summary-number {
    font-size: 2.3rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 4px;
}

.summary-desc {
    font-size: 0.84rem;
    color: #64748b;
}

/* =======================================================
   KARTU-KARTU PENJELASAN WARNA-WARNI CERAH & HARMONIS
   ======================================================= */

/* Kotak Rumus Utama */
.box-formula-hero {
    background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
    border: 2px solid #0284c7;
    border-radius: 18px;
    padding: 24px 26px;
    margin-bottom: 24px;
    box-shadow: 0 6px 20px rgba(2, 132, 199, 0.08);
}

/* 1. Biru Laut (Langkah 1 & Tema Informasi) */
.box-ocean {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border: 1.5px solid #7dd3fc;
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.06);
}
.box-ocean-header {
    color: #0369a1;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* 2. Kuning Cerah / Amber (Langkah 2) */
.box-yellow {
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 1.5px solid #fcd34d;
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(217, 119, 6, 0.06);
}
.box-yellow-header {
    color: #92400e;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* 3. Hijau Segar (Langkah 3) */
.box-green {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 1.5px solid #86efac;
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.06);
}
.box-green-header {
    color: #166534;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* 4. Pink Manis (Langkah 4) */
.box-pink {
    background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 100%);
    border: 1.5px solid #f9a8d4;
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(236, 72, 153, 0.06);
}
.box-pink-header {
    color: #9d174d;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* 5. Gradasi Spesial Hasil Akhir (Langkah 5) */
.box-final {
    background: linear-gradient(135deg, #ecfdf5 0%, #eff6ff 100%);
    border: 2px solid #34d399;
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 16px;
    box-shadow: 0 6px 18px rgba(16, 185, 129, 0.12);
}
.box-final-header {
    color: #047857;
    font-size: 1.15rem;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Kotak Formula Bersih */
.formula-block {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 12px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.92rem;
    color: #0f172a;
    line-height: 1.7;
    margin-top: 10px;
    overflow-x: auto;
}

/* Chip / Badge Kata */
.chip-item {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 8px;
    font-size: 0.88rem;
    font-weight: 700;
    margin: 4px;
}
.chip-green {
    background: #dcfce7;
    border: 1px solid #4ade80;
    color: #15803d;
}
.chip-blue {
    background: #e0f2fe;
    border: 1px solid #38bdf8;
    color: #0369a1;
}
.chip-pink {
    background: #fce7f3;
    border: 1px solid #f472b6;
    color: #be185d;
}

/* Sidebar Cerah */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1.5px solid #e2e8f0 !important;
}

/* Tab Cerah */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    padding: 10px 20px !important;
    border-radius: 12px 12px 0 0 !important;
    background-color: #f1f5f9 !important;
    color: #64748b !important;
    border: 1px solid #e2e8f0 !important;
}

.stTabs [aria-selected="true"] {
    background-color: #ffffff !important;
    color: #0284c7 !important;
    border-bottom: 3px solid #0284c7 !important;
    box-shadow: 0 4px 10px rgba(2, 132, 199, 0.08) !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# CONTOH PRESET KALIMAT SERU & MENARIK
# ==============================================================================
PRESETS = {
    "🍔 Kuliner (Sangat Mirip)": (
        "Saya suka makan nasi goreng ayam pedas di warung tenda",
        "Saya sangat suka makan nasi goreng ayam spesial di restoran"
    ),
    "💻 Belajar Coding (Cukup Mirip)": (
        "Belajar pemrograman Python sangat asyik dan bermanfaat untuk membuat aplikasi",
        "Belajar logika coding dengan bahasa Python sangat menyenangkan bagi pemula"
    ),
    "☕ Santai & Hobi (Kemiripan Sedang)": (
        "Hari Minggu pagi enaknya berolahraga lari santai di taman kota",
        "Hari Minggu pagi sangat nikmat menikmati segelas kopi hangat sambil santai"
    ),
    "🪐 Beda Alam (0% / Sama Sekali Beda)": (
        "Kucing anggora tidur pulas di atas kasur empuk kamar tidur",
        "Roket penjelajah luar angkasa meluncur menuju stasiun planet Mars"
    )
}

# Inisialisasi Session State
if "kalimat1" not in st.session_state:
    st.session_state["kalimat1"] = PRESETS["🍔 Kuliner (Sangat Mirip)"][0]
if "kalimat2" not in st.session_state:
    st.session_state["kalimat2"] = PRESETS["🍔 Kuliner (Sangat Mirip)"][1]

# ==============================================================================
# SIDEBAR: PANDUAN CEPAT, PENGATURAN & RUMUS RESMI
# ==============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 16px 0;">
        <span style="font-size: 2.4rem;">🌈</span>
        <div style="font-size: 1.25rem; font-weight: 800; color: #0284c7; margin-top: 4px;">
            selaaa similarity
        </div>
        <div style="font-size: 0.85rem; color: #64748b;">
            Eksplorasi Cosine Similarity Santai
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚙️ Pengaturan Pembersihan Kata")
    st.caption("Pembersihan kata memastikan perbandingan dilakukan secara adil:")
    opt_lowercase = st.checkbox("Abaikan Huruf Besar/Kecil", value=True, help="Contoh: 'Makan' dan 'makan' akan dianggap sama.")
    opt_remove_punct = st.checkbox("Abaikan Tanda Baca", value=True, help="Contoh: titik, koma, dan tanda seru dihilangkan.")

    st.markdown("---")
    st.markdown("### 📐 Rumus Cosine Similarity")
    st.latex(r"\text{Similarity}(A, B) = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}")
    
    st.caption("Atau dalam bentuk komponen vektor:")
    st.latex(r"\text{Similarity}(A, B) = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \times \sqrt{\sum_{i=1}^{n} B_i^2}}")

    st.markdown("""
    <div style="font-size: 0.83rem; color: #475569; line-height: 1.6; margin-top: 8px;">
        • <b>A · B</b>: Dot product = &Sigma; A<sub>i</sub> B<sub>i</sub><br>
        • <b>||A||</b>: Norma Euclidean A = &radic;(&Sigma; A<sub>i</sub><sup>2</sup>)<br>
        • <b>||B||</b>: Norma Euclidean B = &radic;(&Sigma; B<sub>i</sub><sup>2</sup>)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("✨ Didesain cerah, segar, dan mudah dipahami siapa saja!")

# ==============================================================================
# HEADER HERO BANNER (TEMA CERAH & SEGAR)
# ==============================================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">
        <span>✨</span> SISTEM ANALISIS KEMIRIPAN TEKS
    </div>
    <h1 class="hero-title">Kalkulator Kemiripan Dua Kalimat</h1>
    <p class="hero-subtitle">
        Uji kemiripan kalimat pakai Cosine Similarity. Siapa tahu hasilnya tinggi, kayak ekspektasiku ke kamu 🤭
    </p>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# TOMBOL PRESET CONTOH CEPAT
# ==============================================================================
st.markdown("##### 🎯 Coba Contoh Cepat:")
col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns([1, 1, 1, 1, 0.8])

with col_p1:
    if st.button("🍔 Kuliner", key="p_makan", help="Contoh kalimat bertema makanan dengan kemiripan tinggi"):
        st.session_state["kalimat1"] = PRESETS["🍔 Kuliner (Sangat Mirip)"][0]
        st.session_state["kalimat2"] = PRESETS["🍔 Kuliner (Sangat Mirip)"][1]
        st.rerun()

with col_p2:
    if st.button("💻 Belajar Coding", key="p_coding", help="Contoh kalimat belajar coding"):
        st.session_state["kalimat1"] = PRESETS["💻 Belajar Coding (Cukup Mirip)"][0]
        st.session_state["kalimat2"] = PRESETS["💻 Belajar Coding (Cukup Mirip)"][1]
        st.rerun()

with col_p3:
    if st.button("☕ Santai", key="p_santai", help="Contoh kalimat dengan kemiripan sedang"):
        st.session_state["kalimat1"] = PRESETS["☕ Santai & Hobi (Kemiripan Sedang)"][0]
        st.session_state["kalimat2"] = PRESETS["☕ Santai & Hobi (Kemiripan Sedang)"][1]
        st.rerun()

with col_p4:
    if st.button("🪐 Beda Total (0%)", key="p_beda", help="Contoh dua kalimat tanpa irisan kata sama sekali"):
        st.session_state["kalimat1"] = PRESETS["🪐 Beda Alam (0% / Sama Sekali Beda)"][0]
        st.session_state["kalimat2"] = PRESETS["🪐 Beda Alam (0% / Sama Sekali Beda)"][1]
        st.rerun()

with col_p5:
    if st.button("🧹 Kosongkan", key="p_clear", help="Kosongkan kedua kotak teks"):
        st.session_state["kalimat1"] = ""
        st.session_state["kalimat2"] = ""
        st.rerun()

# ==============================================================================
# AREA INPUT KALIMAT
# ==============================================================================
st.write("")
col_in1, col_in2 = st.columns(2)

cur_t1 = st.session_state.get("kalimat1", "")
cur_t2 = st.session_state.get("kalimat2", "")

with col_in1:
    w1 = len(cur_t1.split()) if cur_t1.strip() else 0
    st.markdown(f"""
    <div class="card-header-a">
        <span>📝 Kalimat Pertama (A)</span>
        <span class="token-pill">{w1} Kata</span>
    </div>
    """, unsafe_allow_html=True)
    in_k1 = st.text_area(
        "Kalimat 1",
        value=cur_t1,
        height=110,
        placeholder="Tulis kalimat pertama di sini...",
        label_visibility="collapsed",
        key="kalimat1"
    )

with col_in2:
    w2 = len(cur_t2.split()) if cur_t2.strip() else 0
    st.markdown(f"""
    <div class="card-header-b">
        <span>📝 Kalimat Kedua (B)</span>
        <span class="token-pill">{w2} Kata</span>
    </div>
    """, unsafe_allow_html=True)
    in_k2 = st.text_area(
        "Kalimat 2",
        value=cur_t2,
        height=110,
        placeholder="Tulis kalimat kedua di sini...",
        label_visibility="collapsed",
        key="kalimat2"
    )

# Tombol Eksekusi
btn_hitung = st.button("🔍 Cek & Hitung Kemiripan Kalimat Sekarang!")

# ==============================================================================
# FUNGSI PEMROSESAN & MATEMATIKA
# ==============================================================================
def bersihkan_kalimat(teks: str, lowercase: bool, hapus_tanda_baca: bool) -> list[str]:
    if lowercase:
        teks = teks.lower()
    if hapus_tanda_baca:
        teks = re.sub(r"[^\w\s]", " ", teks)
    tokens = [t.strip() for t in teks.split() if t.strip()]
    return tokens

def tentukan_status_kemiripan(persentase: float):
    if persentase >= 90.0:
        return {
            "judul": "Hampir Kembar Identik! 👯",
            "warna": "#16a34a",
            "warna_bg": "linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%)",
            "border": "#86efac",
            "kesimpulan": "Kedua kalimat memiliki topik dan kata kunci yang hampir persis sama. Sangat sedikit variasi kata."
        }
    elif persentase >= 65.0:
        return {
            "judul": "Mirip Banget! 🤝",
            "warna": "#0284c7",
            "warna_bg": "linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%)",
            "border": "#7dd3fc",
            "kesimpulan": "Tingkat kesamaan sangat kuat. Banyak kata kunci utama yang saling berkaitan erat."
        }
    elif persentase >= 35.0:
        return {
            "judul": "Ada Miripnya (Sedang) 🤏",
            "warna": "#d97706",
            "warna_bg": "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)",
            "border": "#fcd34d",
            "kesimpulan": "Kedua kalimat memiliki beberapa kata yang sama, namun konteks atau detail lainnya berbeda."
        }
    elif persentase > 0.0:
        return {
            "judul": "Kurang Mirip 🔍",
            "warna": "#ea580c",
            "warna_bg": "linear-gradient(135deg, #ffedd5 0%, #fed7aa 100%)",
            "border": "#fdba74",
            "kesimpulan": "Hanya sedikit sekali kata yang beririsan (misalnya cuma 1 atau 2 kata umum). Sebagian besar isi kalimat berbeda."
        }
    else:
        return {
            "judul": "Beda Alam (Nggak Nyambung) 🪐",
            "warna": "#e11d48",
            "warna_bg": "linear-gradient(135deg, #ffe4e6 0%, #fecdd3 100%)",
            "border": "#fda4af",
            "kesimpulan": "Sama sekali tidak ada kata yang sama di antara kedua kalimat (skor 0%). Topiknya benar-benar berbeda!"
        }

# ==============================================================================
# LOGIKA PERHITUNGAN & TAMPILAN HASIL
# ==============================================================================
k1_teks = in_k1.strip()
k2_teks = in_k2.strip()

if k1_teks and k2_teks:
    # 1. Preprocessing token
    tokens1 = bersihkan_kalimat(k1_teks, opt_lowercase, opt_remove_punct)
    tokens2 = bersihkan_kalimat(k2_teks, opt_lowercase, opt_remove_punct)

    if not tokens1 or not tokens2:
        st.warning("⚠️ Masukkan kalimat yang mengandung kata-kata yang valid.")
    else:
        # 2. Vocabulary & Frekuensi
        set1 = set(tokens1)
        set2 = set(tokens2)
        vocab = sorted(list(set1 | set2))

        frek1 = {w: tokens1.count(w) for w in vocab}
        frek2 = {w: tokens2.count(w) for w in vocab}

        vektor1 = [frek1[w] for w in vocab]
        vektor2 = [frek2[w] for w in vocab]

        # 3. Perkalian Titik (Dot Product) = sum(A_i * B_i)
        products = [a * b for a, b in zip(vektor1, vektor2)]
        dot_product = sum(products)

        # 4. Panjang Vektor (Norma Euclidean) = sqrt(sum(A_i^2)) & sqrt(sum(B_i^2))
        sq1 = [a * a for a in vektor1]
        sq2 = [b * b for b in vektor2]
        panjang1_kuadrat = sum(sq1)
        panjang2_kuadrat = sum(sq2)

        panjang1 = math.sqrt(panjang1_kuadrat)
        panjang2 = math.sqrt(panjang2_kuadrat)

        # 5. Skor Cosine & Persentase
        if panjang1 == 0 or panjang2 == 0:
            skor_cosine = 0.0
        else:
            skor_cosine = dot_product / (panjang1 * panjang2)
            skor_cosine = max(0.0, min(1.0, skor_cosine))

        persen = skor_cosine * 100.0
        status = tentukan_status_kemiripan(persen)

        # Irisan Kata
        kata_cocok = sorted(list(set1 & set2))
        kata_unik1 = sorted(list(set1 - set2))
        kata_unik2 = sorted(list(set2 - set1))

        # ----------------------------------------------------------------------
        # TAMPILAN DASHBOARD HASIL UTAMA (BANNER CERAH)
        # ----------------------------------------------------------------------
        st.write("")
        st.markdown(f"""
        <div style="background: {status['warna_bg']}; border: 2px solid {status['border']}; border-radius: 18px; padding: 22px 28px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; box-shadow: 0 8px 24px rgba(0,0,0,0.05);">
            <div>
                <span style="font-size: 0.85rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: {status['warna']};">
                    HASIL ANALISIS KEMIRIPAN
                </span>
                <div style="font-size: 1.9rem; font-weight: 800; color: #0f172a; margin-top: 2px;">
                    {status['judul']}
                </div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 4px; font-weight: 500;">
                    {status['kesimpulan']}
                </div>
            </div>
            <div style="text-align: right; min-width: 160px;">
                <div style="font-size: 3rem; font-weight: 900; color: {status['warna']}; line-height: 1;">
                    {persen:.1f}%
                </div>
                <div style="font-size: 0.9rem; color: #475569; font-family: 'JetBrains Mono', monospace; font-weight: 600; margin-top: 4px;">
                    Skor: {skor_cosine:.4f} / 1.0
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar cerah
        st.markdown(f"""
        <div style="background: #ffffff; border-radius: 12px; padding: 10px 14px; border: 1.5px solid #e2e8f0; margin-bottom: 22px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; font-size: 0.82rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">
                <span>0% (Beda Total)</span>
                <span style="color: {status['warna']}; font-weight: 800;">Tingkat Kesamaan: {persen:.1f}%</span>
                <span>100% (Sama Persis)</span>
            </div>
            <div style="width: 100%; height: 14px; background: #f1f5f9; border-radius: 7px; overflow: hidden;">
                <div style="width: {persen}%; height: 100%; background: linear-gradient(90deg, #38bdf8 0%, #10b981 100%); border-radius: 7px; transition: width 0.8s ease;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Tiga Kartu Ringkas (Hijau, Biru Laut, Pink)
        c_m1, c_m2, c_m3 = st.columns(3)
        with c_m1:
            st.markdown(f"""
            <div class="summary-card" style="border-top: 4px solid #10b981;">
                <div class="summary-title" style="color: #15803d;">🌿 Kata yang Cocok</div>
                <div class="summary-number" style="color: #16a34a;">{len(kata_cocok)}</div>
                <div class="summary-desc">Muncul bersamaan di kedua kalimat</div>
            </div>
            """, unsafe_allow_html=True)

        with c_m2:
            st.markdown(f"""
            <div class="summary-card" style="border-top: 4px solid #0284c7;">
                <div class="summary-title" style="color: #0369a1;">🌊 Kata Unik Kalimat 1</div>
                <div class="summary-number" style="color: #0284c7;">{len(kata_unik1)}</div>
                <div class="summary-desc">Hanya ada di Kalimat Pertama</div>
            </div>
            """, unsafe_allow_html=True)

        with c_m3:
            st.markdown(f"""
            <div class="summary-card" style="border-top: 4px solid #ec4899;">
                <div class="summary-title" style="color: #be185d;">🌸 Kata Unik Kalimat 2</div>
                <div class="summary-number" style="color: #db2777;">{len(kata_unik2)}</div>
                <div class="summary-desc">Hanya ada di Kalimat Kedua</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        # ----------------------------------------------------------------------
        # TABS DETAIL: RUMUS PERSIS SESUAI GAMBAR + PENJELASAN CERAH
        # ----------------------------------------------------------------------
        tab_cerita, tab_langkah, tab_tabel, tab_konsep = st.tabs([
            "💬 1. Mengapa Skornya Segitu? (Penjelasan Alasan)",
            "🧮 2. Langkah Hitung Demi Langkah (Rumus Lengkap)",
            "📊 3. Matriks Komponen (Tabel & Grafik)",
            "💡 4. Analogi Santai & Konsep Dasar"
        ])

        # TAB 1: PENJELASAN ALASAN YANG BERSIH & RAMAH
        with tab_cerita:
            st.markdown("### 🔍 Mengapa Kedua Kalimat Ini Dinilai Seperti Itu?")
            
            # Kartu Tampilan Dua Kalimat yang Bersih & Mudah Dibaca
            st.markdown(f"""
            <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                <div style="margin-bottom: 14px;">
                    <span style="font-weight: 700; color: #0284c7; font-size: 0.9rem;">📝 Kalimat Pertama:</span>
                    <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 10px; padding: 12px 16px; margin-top: 6px; font-size: 1.02rem; color: #0f172a; line-height: 1.6;">
                        {html.escape(k1_teks)}
                    </div>
                </div>
                <div>
                    <span style="font-weight: 700; color: #db2777; font-size: 0.9rem;">📝 Kalimat Kedua:</span>
                    <div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 10px; padding: 12px 16px; margin-top: 6px; font-size: 1.02rem; color: #0f172a; line-height: 1.6;">
                        {html.escape(k2_teks)}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Rincian Kata dengan Chip Warna-Warni Segar
            st.markdown("#### 📌 Rincian Kosakata yang Ditemukan:")
            col_k1, col_k2, col_k3 = st.columns(3)

            with col_k1:
                st.markdown(f"**🌿 Kata Bersama / Cocok ({len(kata_cocok)} kata):**")
                if kata_cocok:
                    tags = "".join([f'<span class="chip-item chip-green">{w}</span>' for w in kata_cocok])
                    st.markdown(f'<div style="line-height: 2;">{tags}</div>', unsafe_allow_html=True)
                else:
                    st.info("Tidak ada kata yang sama sama sekali.")

            with col_k2:
                st.markdown(f"**🌊 Cuma Ada di Kalimat 1 ({len(kata_unik1)} kata):**")
                if kata_unik1:
                    tags = "".join([f'<span class="chip-item chip-blue">{w}</span>' for w in kata_unik1])
                    st.markdown(f'<div style="line-height: 2;">{tags}</div>', unsafe_allow_html=True)
                else:
                    st.success("Semua kata di Kalimat 1 ada di Kalimat 2!")

            with col_k3:
                st.markdown(f"**🌸 Cuma Ada di Kalimat 2 ({len(kata_unik2)} kata):**")
                if kata_unik2:
                    tags = "".join([f'<span class="chip-item chip-pink">{w}</span>' for w in kata_unik2])
                    st.markdown(f'<div style="line-height: 2;">{tags}</div>', unsafe_allow_html=True)
                else:
                    st.success("Semua kata di Kalimat 2 ada di Kalimat 1!")

            st.markdown("---")
            st.markdown(f"""
            #### 🧠 Kesimpulan Logika Sederhana:
            - **Inti Cosine Similarity**: Semakin banyak kata yang dipakai bersama, dan semakin sedikit kata yang berbeda, skornya akan makin mendekati **100%**.
            - Dari total **{len(vocab)} kata unik**, kedua kalimat bertemu pada **{len(kata_cocok)} kata yang sama**.
            - Karena itu, sistem memberikan skor kemiripan sebesar **{persen:.1f}% ({status['judul']})**.
            """)

        # TAB 2: STEP BY STEP RUMUS PERSIS SESUAI GAMBAR PENGGUNA
        with tab_langkah:
            st.markdown("### 📐 Rumus Resmi Cosine Similarity")

            # KOTAK FORMULA UTAMA SESUAI GAMBAR PERSIS
            st.markdown("""
            <div class="box-formula-hero">
                <div style="font-size: 1.15rem; font-weight: 800; color: #0284c7; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                    <span>📐 Rumus Utama Cosine Similarity:</span>
                </div>
            """, unsafe_allow_html=True)

            # Rumus 1: Bentuk Vektor
            st.latex(r"\text{Similarity}(A, B) = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}")

            st.markdown("""
                <div style="text-align: center; color: #475569; font-weight: 600; font-size: 0.95rem; margin: 14px 0 10px 0;">
                    Atau jika dijabarkan ke dalam bentuk komponen vektor:
                </div>
            """, unsafe_allow_html=True)

            # Rumus 2: Bentuk Komponen Sigma
            st.latex(r"\text{Similarity}(A, B) = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \times \sqrt{\sum_{i=1}^{n} B_i^2}}")

            st.markdown("""
                <div style="margin-top: 18px; padding-top: 14px; border-top: 1.5px solid #e2e8f0;">
                    <div style="font-weight: 800; color: #0f172a; font-size: 0.98rem; margin-bottom: 8px;">
                        Keterangan Komponen:
                    </div>
                    <ul style="color: #334155; font-size: 0.94rem; line-height: 1.85; padding-left: 20px; margin-bottom: 0;">
                        <li><b>A · B</b>: <i>Dot product</i> (hasil kali titik) antara vektor <i>A</i> dan vektor <i>B</i>, yaitu <b>&sum;<sub>i=1</sub><sup>n</sup> A<sub>i</sub> B<sub>i</sub></b>. <span style="color: #0369a1; font-weight: 700;">(TIDAK diakar pangkat!)</span></li>
                        <li><b>||A||</b>: Panjang (<i>magnitude</i> / norma Euclidean) dari vektor <i>A</i>, dihitung dengan <b>&radic;(&sum;<sub>i=1</sub><sup>n</sup> A<sub>i</sub><sup>2</sup>)</b>. <span style="color: #be185d; font-weight: 700;">(Diakar pangkat dua!)</span></li>
                        <li><b>||B||</b>: Panjang (<i>magnitude</i> / norma Euclidean) dari vektor <i>B</i>, dihitung dengan <b>&radic;(&sum;<sub>i=1</sub><sup>n</sup> B<sub>i</sub><sup>2</sup>)</b>. <span style="color: #be185d; font-weight: 700;">(Diakar pangkat dua!)</span></li>
                    </ul>
                </div>
                <div style="margin-top: 14px; background: #fefce8; border: 1.5px solid #facc15; border-radius: 10px; padding: 12px 16px; font-size: 0.88rem; color: #854d0e; line-height: 1.6;">
                    💡 <b>Catatan Penting (Jangan Tertukar ya!):</b><br>
                    • <b>Kata yang cocok (&sum; Aᵢ Bᵢ)</b> ada di bagian <u>ATAS (Pembilang)</u> dan <b>TIDAK diakar pangkat</b>, hanya dikalikan lalu dijumlahkan.<br>
                    • Yang <b>DIAKAR PANGKAT (&radic;)</b> adalah bagian <u>BAWAH (Penyebut)</u>, yaitu panjang masing-masing kalimat (&radic;&sum; Aᵢ² dan &radic;&sum; Bᵢ²) agar pembagiannya adil menghasilkan skala 0 s/d 1 (100%).
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🧮 Penerapan Nyata ke Dalam Kalimat Anda (Step-by-Step):")
            st.write("Berikut perhitungan nyata dengan angka-angka dari kalimat Anda berdasarkan rumus komponen di atas:")

            # LANGKAH 1: NUANSA BIRU LAUT 🌊
            st.markdown(f"""
            <div class="box-ocean">
                <div class="box-ocean-header">
                    <span>🌊 1️⃣ Langkah 1: Merapikan Kalimat (Pembersihan / Preprocessing)</span>
                </div>
                <div style="font-size: 0.95rem; color: #0c4a6e; line-height: 1.6;">
                    Komputer mengubah huruf kapital menjadi huruf kecil dan membuang tanda baca agar kata dihitung secara adil.
                </div>
                <div class="formula-block" style="border-color: #7dd3fc; color: #0369a1;">
                    Kalimat A diurai menjadi: {tokens1}<br>
                    Kalimat B diurai menjadi: {tokens2}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # LANGKAH 2: NUANSA KUNING CERAH ☀️
            st.markdown(f"""
            <div class="box-yellow">
                <div class="box-yellow-header">
                    <span>☀️ 2️⃣ Langkah 2: Mengumpulkan Komponen Kosakata (n = {len(vocab)} Dimensi)</span>
                </div>
                <div style="font-size: 0.95rem; color: #78350f; line-height: 1.6;">
                    Setiap kata unik menjadi satu indeks komponen vektor (<i>i = 1</i> sampai <i>n = {len(vocab)}</i>):
                </div>
                <div class="formula-block" style="border-color: #fcd34d; color: #92400e;">
                    Daftar Semua Kata (i=1..{len(vocab)}) = {vocab}<br>
                    Vektor A (Aᵢ) = {vektor1}<br>
                    Vektor B (Bᵢ) = {vektor2}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # LANGKAH 3: NUANSA HIJAU SEGAR 🌿 (PEMBILANG: A · B = SUM(A_i * B_i))
            dot_terms = [f"({frek1[w]} × {frek2[w]})" for w in vocab if frek1[w] * frek2[w] > 0]
            dot_str = " + ".join(dot_terms) if dot_terms else "0"
            st.markdown(f"""
            <div class="box-green">
                <div class="box-green-header">
                    <span>🌿 3️⃣ Langkah 3: Menghitung Pembilang: A &bull; B = &sum;<sub>i=1</sub><sup>n</sup> A<sub>i</sub> B<sub>i</sub></span>
                </div>
                <div style="font-size: 0.95rem; color: #14532d; line-height: 1.6;">
                    Mengalikan frekuensi kata yang sama di Kalimat A (<i>A<sub>i</sub></i>) dan Kalimat B (<i>B<sub>i</sub></i>), lalu menjumlahkannya:
                </div>
            """, unsafe_allow_html=True)

            st.latex(rf"\mathbf{{A}} \cdot \mathbf{{B}} = \sum_{{i=1}}^{{{len(vocab)}}} A_i B_i = {dot_str} = \mathbf{{{dot_product}}}")

            st.markdown(f"""
                <div class="formula-block" style="border-color: #86efac; color: #166534;">
                    Hasil Dot Product (Pembilang) = <b>{dot_product}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # LANGKAH 4: NUANSA PINK MANIS 🌸 (PENYEBUT: ||A|| dan ||B||)
            sq_terms1 = [str(a*a) for a in vektor1 if a > 0]
            sq_terms2 = [str(b*b) for b in vektor2 if b > 0]
            st.markdown(f"""
            <div class="box-pink">
                <div class="box-pink-header">
                    <span>🌸 4️⃣ Langkah 4: Menghitung Penyebut: ||A|| = &radic;(&sum; A<sub>i</sub><sup>2</sup>) dan ||B|| = &radic;(&sum; B<sub>i</sub><sup>2</sup>)</span>
                </div>
                <div style="font-size: 0.95rem; color: #831843; line-height: 1.6;">
                    Menghitung panjang (norma Euclidean) dari masing-masing vektor dokumen:
                </div>
            """, unsafe_allow_html=True)

            st.latex(rf"\|\mathbf{{A}}\| = \sqrt{{\sum_{{i=1}}^{{{len(vocab)}}} A_i^2}} = \sqrt{{{' + '.join(sq_terms1) or '0'}}} = \sqrt{{{panjang1_kuadrat}}} \approx \mathbf{{{panjang1:.4f}}}")
            st.latex(rf"\|\mathbf{{B}}\| = \sqrt{{\sum_{{i=1}}^{{{len(vocab)}}} B_i^2}} = \sqrt{{{' + '.join(sq_terms2) or '0'}}} = \sqrt{{{panjang2_kuadrat}}} \approx \mathbf{{{panjang2:.4f}}}")

            pembagi = panjang1 * panjang2
            st.markdown(f"""
                <div class="formula-block" style="border-color: #f9a8d4; color: #9d174d;">
                    Hasil Kali Kedua Norma (Penyebut) = ||A|| &times; ||B|| = {panjang1:.4f} &times; {panjang2:.4f} = <b>{pembagi:.4f}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # LANGKAH 5: GRADASI SPESIAL HASIL AKHIR 🌈 (SUBSTITUSI PENUH KE RUMUS)
            st.markdown(f"""
            <div class="box-final">
                <div class="box-final-header">
                    <span>🌈 5️⃣ Langkah 5: Substitusi Penuh ke Rumus Utama Cosine Similarity</span>
                </div>
                <div style="font-size: 0.98rem; color: #064e3b; line-height: 1.6;">
                    Memasukkan nilai Pembilang dan Penyebut ke dalam rumus resmi:
                </div>
            """, unsafe_allow_html=True)

            st.latex(rf"\text{{Similarity}}(A, B) = \frac{{\sum_{{i=1}}^{{{len(vocab)}}} A_i B_i}}{{\sqrt{{\sum_{{i=1}}^{{{len(vocab)}}} A_i^2}} \times \sqrt{{\sum_{{i=1}}^{{{len(vocab)}}} B_i^2}}}} = \frac{{{dot_product}}}{{{panjang1:.4f} \times {panjang2:.4f}}} = \frac{{{dot_product}}}{{{pembagi:.4f}}} = \mathbf{{{skor_cosine:.4f}}}")

            st.markdown(f"""
                <div class="formula-block" style="border-color: #6ee7b7; color: #065f46; font-size: 1.05rem; text-align: center;">
                    🎉 <b>Skor Cosine Similarity:</b> <span style="color: #059669; font-weight: 800; font-size: 1.3rem;">{skor_cosine:.4f}</span> 
                    &nbsp;&bull;&nbsp; <b>Persentase:</b> <span style="color: #0284c7; font-weight: 800; font-size: 1.3rem;">{persen:.1f}%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # TAB 3: MATRIKS KOMPONEN VEKTOR LENGKAP & GRAFIK
        with tab_tabel:
            st.markdown("### 📋 Matriks Komponen Vektor Term-Dokumen:")
            st.caption("Tabel ini menunjukkan nilai komponen Aᵢ, Bᵢ, Aᵢ², Bᵢ², serta perkalian Aᵢ × Bᵢ untuk setiap kata (i = 1 sampai n):")

            data_tabel = []
            for i, w in enumerate(vocab, 1):
                f1 = frek1[w]
                f2 = frek2[w]
                a_sq = f1 * f1
                b_sq = f2 * f2
                prod = f1 * f2
                if f1 > 0 and f2 > 0:
                    status_kata = "🌿 Muncul di Keduanya"
                elif f1 > 0:
                    status_kata = "🌊 Cuma Kalimat 1"
                else:
                    status_kata = "🌸 Cuma Kalimat 2"

                data_tabel.append({
                    "No (i)": i,
                    "Kata (Term ke-i)": w,
                    "Kalimat A (Aᵢ)": f1,
                    "Kalimat B (Bᵢ)": f2,
                    "Aᵢ²": a_sq,
                    "Bᵢ²": b_sq,
                    "Aᵢ × Bᵢ": prod,
                    "Keterangan": status_kata
                })

            df_tabel = pd.DataFrame(data_tabel)
            st.dataframe(df_tabel, width="stretch", hide_index=True)

            # Rangkuman Baris Total Sigma
            st.markdown(f"""
            <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-top: 10px; margin-bottom: 24px;">
                <div style="flex: 1; min-width: 200px; background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 12px 16px; text-align: center;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #15803d;">&sum; Aᵢ &times; Bᵢ (DOT PRODUCT)</div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: #166534;">{dot_product}</div>
                </div>
                <div style="flex: 1; min-width: 200px; background: #f0f9ff; border: 1.5px solid #7dd3fc; border-radius: 12px; padding: 12px 16px; text-align: center;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #0369a1;">&sum; Aᵢ² &rarr; &radic;(&sum; Aᵢ²)</div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: #0284c7;">{panjang1_kuadrat} &rarr; {panjang1:.4f}</div>
                </div>
                <div style="flex: 1; min-width: 200px; background: #fdf2f8; border: 1.5px solid #f9a8d4; border-radius: 12px; padding: 12px 16px; text-align: center;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #9d174d;">&sum; Bᵢ² &rarr; &radic;(&sum; Bᵢ²)</div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: #db2777;">{panjang2_kuadrat} &rarr; {panjang2:.4f}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 📊 Grafik Perbandingan Frekuensi Kata:")
            
            data_grafik = []
            for w in vocab:
                data_grafik.append({"Kata": w, "Kalimat": "Kalimat 1", "Frekuensi": frek1[w]})
                data_grafik.append({"Kata": w, "Kalimat": "Kalimat 2", "Frekuensi": frek2[w]})

            df_grafik = pd.DataFrame(data_grafik)

            chart = alt.Chart(df_grafik).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
                x=alt.X('Kata:N', sort=None, title='Daftar Kata'),
                y=alt.Y('Frekuensi:Q', title='Berapa Kali Muncul'),
                color=alt.Color(
                    'Kalimat:N',
                    scale=alt.Scale(
                        domain=['Kalimat 1', 'Kalimat 2'],
                        range=['#0284c7', '#ec4899']
                    ),
                    legend=alt.Legend(title="Kalimat", orient="top")
                ),
                xOffset='Kalimat:N',
                tooltip=['Kata', 'Kalimat', 'Frekuensi']
            ).properties(
                height=320
            ).configure_view(
                strokeWidth=0
            ).configure_axis(
                gridColor='#e2e8f0',
                labelColor='#475569',
                titleColor='#0369a1'
            ).configure_legend(
                labelColor='#334155',
                titleColor='#0369a1'
            )

            st.altair_chart(chart, width="stretch")

        # TAB 4: ANALOGI SANTAI & KONSEP DASAR (WARNA CERAH)
        with tab_konsep:
            st.markdown("### 💡 Analogi Santai Supaya Lebih Mudah Memahami")
            
            col_a1, col_a2 = st.columns(2)

            with col_a1:
                st.markdown("""
                <div class="box-ocean">
                    <div class="box-ocean-header">🎯 Analogi Arah Panah (Vektor)</div>
                    <div style="font-size: 0.94rem; color: #0c4a6e; line-height: 1.6;">
                        Bayangkan setiap kalimat adalah sebuah <b>panah</b>:<br>
                        • Jika dua panah menunjuk ke <b>arah yang sama persis</b> (sudut 0°), kesamaannya bernilai <b>1 (100%)</b>.<br>
                        • Jika satu menunjuk ke utara dan satu ke timur (<b>tegak lurus</b>, sudut 90°), mereka tidak searah, bernilai <b>0 (0%)</b>.<br>
                        • Cosine Similarity mengukur sudut arah tersebut!
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col_a2:
                st.markdown("""
                <div class="box-pink">
                    <div class="box-pink-header">🍕 Analogi Pesanan Makanan Restoran</div>
                    <div style="font-size: 0.94rem; color: #831843; line-height: 1.6;">
                        Bayangkan dua orang teman memesan makanan:<br>
                        • Teman A: <i>Nasi Goreng, Ayam, Es Teh</i>.<br>
                        • Teman B: <i>Nasi Goreng, Ayam, Jus Jeruk</i>.<br>
                        • Dua dari tiga pesanan sama! Selera mereka <b>sangat mirip</b>.<br>
                        • Kalau Teman B memesan <i>Sate Kambing, Gulai, Soda</i>, maka seleranya <b>berbeda total</b>!
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("""
            #### ❓ Pertanyaan yang Sering Muncul (FAQ):
            1. **Kenapa namanya Cosine (Kosinus)?**  
               Dalam matematika trigonometri, nilai kosinus sudut 0° adalah **1**, dan nilai kosinus sudut 90° adalah **0**. Karena mengukur sudut kemiripan arah, metode ini dinamai Cosine Similarity.
            2. **Apakah urutan kata berpengaruh?**  
               Pada metode dasar (Bag of Words / Vektor Frekuensi), urutan kata tidak mempengaruhi skor. Yang dihitung adalah keberadaan dan frekuensi kemunculan katanya.
            3. **Di mana metode ini dipakai di dunia nyata?**  
               - Mesin pencari Google (mencari kesamaan kata kunci pencarian dengan artikel).
               - Sistem pendeteksi plagiarisme (mencari kesamaan dokumen tugas).
               - Rekomendasi berita dan artikel terkait.
            """)

else:
    st.info("👆 Masukkan kalimat di kotak Kalimat 1 dan Kalimat 2, atau klik salah satu tombol **Coba Contoh Cepat** di atas!")

# ==============================================================================
# FOOTER CERAH & ELEGAN
# ==============================================================================
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 22px 0; border-top: 1.5px solid #e2e8f0; font-size: 0.92rem; color: #64748b;">
    dibuat buat ngukur kemiripan kalimat, bukan buat nyari alasan ngobrol sama kamu. tapi kalau kamu yang mulai duluan, boleh juga. 🤭
</div>
""", unsafe_allow_html=True)
