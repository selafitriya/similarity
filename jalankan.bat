@echo off
setlocal
echo ========================================================
echo   Menjalankan Aplikasi Cosine Similarity...
echo ========================================================

if exist "C:\Users\LENOVO\miniconda3\python.exe" (
    "C:\Users\LENOVO\miniconda3\python.exe" -m streamlit run app.py
) else if exist "C:\Users\LENOVO\miniconda3\Scripts\streamlit.exe" (
    "C:\Users\LENOVO\miniconda3\Scripts\streamlit.exe" run app.py
) else (
    python -m streamlit run app.py
)

if errorlevel 1 (
    echo.
    echo Ada kendala saat menjalankan Streamlit.
    pause
)
endlocal
