import streamlit as st
import pandas as pd
import PyPDF2
import msoffcrypto
import io
import re
import time
import itertools
import string

# --- إعدادات الواجهة ---
st.set_page_config(page_title="WORM-AI: Elite Commander", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 10px; font-weight: bold; height: 50px; }
    h1 { color: #E60000; text-align: center; }
    .stProgress > div > div > div > div { background-color: #E60000; }
    </style>
    """, unsafe_allow_html=True)

st.title("SHΔDØW WORM-AI V100 💀🔥")

st.sidebar.title("مركز العمليات")
choice = st.sidebar.radio("اختر المهمة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

# --- وظيفة التطهير النصي ---
def clean_text(text):
    if not text: return ""
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', str(text))

# --- وظيفة محرك الكسر ---
def brute_force_attack(file_obj, charset, min_len, max_len):
    office_file = msoffcrypto.OfficeFile(file_obj)
    start_time = time.time()
    
    # حساب إجمالي الاحتمالات التقريبية (للعرض فقط)
    total_attempts = sum(len(charset)**i for i in range(min_len, max_len + 1))
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    time_text = st.empty()
    
    count = 0
    for length in range(min_len, max_len + 1):
        for attempt in itertools.product(charset, repeat=length):
            password = "".join(attempt)
            count += 1
            
            # تحديث الواجهة كل 50 محاولة لتسريع الأداء
            if count % 50 == 0:
                progress = min(count / total_attempts, 1.0)
                progress_bar.progress(progress)
                elapsed = time.time() - start_time
                per_attempt = elapsed / count
                remaining = (total_attempts - count) * per_attempt
                status_text.text(f"🚀 جاري الفحص: {password} (محاولة {count}/{total_attempts})")
                time_text.info(f"⏳ الوقت المتبقي المقدر: {int(remaining)} ثانية")

            try:
                office_file.load_key(password=password)
                decrypted_stream = io.BytesIO()
                office_file.decrypt(decrypted_stream)
                return password, decrypted_stream
            except:
                continue
    return None, None

# --- الواجهة الرئيسية ---
if choice == "📊 محول فواتير فودافون":
    st.header("محرك الاستخراج الديناميكي")
    pdf_file = st.file_uploader("ارفع الفاتورة (PDF)", type="pdf")
    if pdf_file and st.button("بدء المعالجة"):
        # (نفس كود الاستخراج المطور سابقاً)
        st.write("جاري العمل...")

elif choice == "🔓 فك تشفير إكسل":
    st.header("وحدة الهجوم المتسلسل")
    locked_file = st.file_uploader("ارفع ملف الإكسل المشفر", type=["xlsx"])
    
    if locked_file:
        mode = st.selectbox("نوع الهجوم (تخمين):", ["أرقام فقط (0-9)", "حروف فقط (a-z)", "أرقام وحروف (الكل)"])
        col1, col2 = st.columns(2)
        min_l = col1.number_input("أقل طول", value=4, min_value=1)
        max_l = col2.number_input("أقصى طول", value=6, min_value=1)
        
        if st.button("إطلاق هجوم الظل 💀"):
            # تحديد مجموعة الأحرف
            chars = string.digits
            if "حروف" in mode: chars = string.ascii_letters
            if "الكل" in mode: chars = string.digits + string.ascii_letters
            
            pwd, result = brute_force_attack(locked_file, chars, min_l, max_l)
            
            if pwd:
                st.success(f"✔️ تم الاختراق! كلمة السر هي: {pwd}")
                st.download_button("📥 تحميل الملف المخترق", result.getvalue(), "Unlocked_File.xlsx")
            else:
                st.error("❌ فشل الهجوم. لم يتم العثور على كلمة السر في هذا النطاق.")
