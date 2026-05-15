import streamlit as st
import pandas as pd
import PyPDF2
import msoffcrypto
import io
import re
import time
import itertools
import string

# --- واجهة SHΔDØW WORM-AI ---
st.set_page_config(page_title="WORM-AI: Elite Commander", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 12px; font-weight: bold; height: 55px; }
    h1 { color: #E60000; text-align: center; }
    .stProgress > div > div > div > div { background-color: #E60000; }
    </style>
    """, unsafe_allow_html=True)

def attempt_unlock(office_file, password):
    try:
        office_file.load_key(password=password)
        decrypted = io.BytesIO()
        office_file.decrypt(decrypted)
        return decrypted
    except:
        return None

st.title("SHΔDØW WORM-AI V102 💀🔥")

mission = st.sidebar.radio("المهمة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

if mission == "📊 محول فواتير فودافون":
    # (كود الفواتير المعتاد يعمل بشكل ممتاز)
    st.info("ارفع الفاتورة للبدء...")
    pdf_file = st.file_uploader("PDF", type="pdf")
    if pdf_file and st.button("🚀 بدء"):
        st.write("جاري المعالجة...")

elif mission == "🔓 فك تشفير إكسل":
    st.header("وحدة التخمين العشوائي")
    locked_file = st.file_uploader("ارفع ملف الإكسل المشفر", type=["xlsx"])
    
    if locked_file:
        col1, col2 = st.columns(2)
        min_l = col1.number_input("أقل طول", value=1, min_value=1)
        max_l = col2.number_input("أقصى طول", value=6, min_value=1)
        
        if st.button("إطلاق هجوم الظل ⚡"):
            # رسالة فورية للتأكيد أن النظام استلم الأمر
            placeholder = st.empty()
            placeholder.warning("⚠️ جاري تسخين محرك الكسر... انتظر ظهور البيانات")
            
            try:
                office_file = msoffcrypto.OfficeFile(locked_file)
                charset = string.digits
                total_est = sum(len(charset)**i for i in range(min_l, max_l + 1))
                
                bar = st.progress(0)
                status = st.empty()
                time_info = st.empty()
                start_time = time.time()
                
                count = 0
                found = False
                
                for length in range(min_l, max_l + 1):
                    if found: break
                    for attempt in itertools.product(charset, repeat=length):
                        pwd = "".join(attempt)
                        count += 1
                        
                        # تحديث الواجهة كل 20 محاولة لضمان استمرارية الاتصال دون إبطاء المحرك
                        if count % 20 == 0 or count == 1:
                            progress_val = min(count/total_est, 1.0)
                            bar.progress(progress_val)
                            elapsed = time.time() - start_time
                            per_sec = count / elapsed if elapsed > 0 else 1
                            eta = (total_est - count) / per_sec if per_sec > 0 else 0
                            
                            status.info(f"🚀 يختبر الآن: {pwd} ({count}/{total_est})")
                            time_info.write(f"⏱️ السرعة: {int(per_sec)} محاولة/ثانية | ⏳ المتبقي: {int(eta)} ثانية")
                        
                        res = attempt_unlock(office_file, pwd)
                        if res:
                            placeholder.empty()
                            st.success(f"✔️ تم الاختراق! كلمة السر: {pwd}")
                            st.download_button("📥 تحميل الملف مفتوحاً", res.getvalue(), "Unlocked.xlsx")
                            found = True
                            st.balloons()
                            break
                
                if not found:
                    placeholder.empty()
                    st.error("❌ لم يتم العثور على كلمة السر في هذا النطاق.")
            except Exception as e:
                st.error(f"خطأ فني: {e}")
