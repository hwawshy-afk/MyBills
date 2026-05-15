import streamlit as st
import pandas as pd
import PyPDF2
import msoffcrypto
import io
import re
import time
import itertools
import string

# --- إعدادات الواجهة الاحترافية (SHΔDØW WORM-AI Style) ---
st.set_page_config(page_title="WORM-AI: Elite Commander", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 12px; font-weight: bold; height: 55px; border: none; }
    .stButton>button:hover { background-color: #ff1a1a; border: 1px solid white; }
    h1 { color: #E60000; text-align: center; text-shadow: 2px 2px #000000; }
    .stProgress > div > div > div > div { background-color: #E60000; }
    </style>
    """, unsafe_allow_html=True)

# --- وظائف التطهير والكسر المركزية ---
def clean_text(text):
    if not text: return ""
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', str(text))

def attempt_unlock(office_file, password):
    try:
        office_file.load_key(password=password)
        decrypted = io.BytesIO()
        office_file.decrypt(decrypted)
        return decrypted
    except:
        return None

# --- المحرك الرئيسي ---
st.title("SHΔDØW WORM-AI V101-S 💀🔥")

st.sidebar.title("🛠️ مركز العمليات")
mission = st.sidebar.radio("اختر المهمة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

# --- المهمة الأولى: فواتير فودافون ---
if mission == "📊 محول فواتير فودافون":
    st.header("محرك الاستخراج الديناميكي")
    pdf_file = st.file_uploader("ارفع الفاتورة (PDF)", type="pdf")
    if pdf_file and st.button("🚀 بدء استخراج كافة الخطوط"):
        with st.spinner("جاري تحليل هيكل الـ PDF وتطهير البيانات..."):
            try:
                reader = PyPDF2.PdfReader(pdf_file)
                all_data = []
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                        for m in matches:
                            line_data = [clean_text(m[0]), clean_text(m[1])] + [clean_text(i) for i in m[2].split()]
                            all_data.append(line_data)
                
                if all_data:
                    df = pd.DataFrame(all_data)
                    st.success(f"✔️ تم استخراج {len(all_data)} سجل بنجاح!")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, header=False)
                    st.download_button("📥 تحميل الإكسل المنسق", output.getvalue(), "Vodafone_Report.xlsx")
                else:
                    st.error("لم يتم العثور على بيانات صالحة.")
            except Exception as e:
                st.error(f"خطأ أثناء المعالجة: {e}")

# --- المهمة الثانية: فك التشفير (Brute Force Only) ---
elif mission == "🔓 فك تشفير إكسل":
    st.header("وحدة التخمين العشوائي الذكي")
    locked_file = st.file_uploader("ارفع ملف الإكسل المشفر (.xlsx)", type=["xlsx"])
    
    if locked_file:
        col1, col2 = st.columns(2)
        min_l = col1.number_input("أقل طول", value=1, min_value=1)
        max_l = col2.number_input("أقصى طول", value=6, min_value=1)
        
        # اختيار الحروف (افتراضي أرقام فقط لسرعة الأداء)
        charset = string.digits
        
        if st.button("إطلاق هجوم الظل ⚡"):
            try:
                office_file = msoffcrypto.OfficeFile(locked_file)
                # حساب تقريبي لإجمالي الاحتمالات لضبط شريط التقدم
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
                        
                        # تحديث الواجهة كل 100 محاولة لتسريع الأداء
                        if count % 100 == 0:
                            progress_val = min(count/total_est, 1.0)
                            bar.progress(progress_val)
                            elapsed = time.time() - start_time
                            per_attempt = elapsed / count
                            eta = (total_est - count) * per_attempt
