import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Alper Özarslan | Portfolio", page_icon="📊", layout="wide")

# Başlık
st.title("👋 Merhaba, ben Alper Özarslan")
st.subheader("Veri Bilimi | Makine Öğrenmesi | Derin Öğrenme")

# Hakkımda
st.markdown("""
Merhaba! Ben **Alper Özarslan**, veri bilimi ve yapay zeka alanında çalışan bir bilgisayar bilimleri öğrencisiyim.  
Python, PyTorch ve veri analizi üzerine projeler geliştiriyorum. 🚀  
""")

# Projeler
st.header("📌 Projelerim")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Ev Fiyat Tahmini")
    st.write("Makine öğrenmesi ile ev satış fiyatlarını tahmin eden model.")
    st.markdown("[GitHub Repo](https://github.com/)")

with col2:
    st.subheader("🩺 Kanser Analizi")
    st.write("Veri bilimi ile erken teşhis için sınıflandırma modeli.")
    st.markdown("[GitHub Repo](https://github.com/)")

col3, col4 = st.columns(2)

with col3:
    st.subheader("🏭 Makine Bakım Tahmini")
    st.write("Endüstride arızaları önceden tahmin eden model.")
    st.markdown("[GitHub Repo](https://github.com/)")

with col4:
    st.subheader("🌆 Şehir Yapıları Analizi")
    st.write("Datathon projesi: şehir verilerinde deep learning uygulamaları.")
    st.markdown("[GitHub Repo](https://github.com/)")

# İletişim
st.header("📬 İletişim")
st.write("📧 Email: alper@example.com")  
st.write("💼 LinkedIn: [linkedin.com/in/alperozarslan](https://linkedin.com)")  
st.write("🐙 GitHub: [github.com/alperozarslan](https://github.com)")  