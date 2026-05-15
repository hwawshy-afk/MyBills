import streamlit as st
import pandas as pd
import PyPDF2
import msoffcrypto
import io
import re

# إعدادات الواجهة للموبايل
st.set_page_config(page_title="WORM-AI: Vodafone Pro", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 10px; font-weight: bold; height: 50px; }
    h1 { color: #E60000; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

def clean_text(text):
    """حذف الرموز غير القانونية التي تسبب انهيار الإكسل"""
    if not text:
        return ""
    # حذف رموز التحكم ASCII (0-31) باستثناء السطر الجديد والمسافات
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', str(text))

st.title("SHΔDØW WORM-AI V99 💀🔥")

st.sidebar.title("مركز العمليات")
choice = st.sidebar.radio("اختر المهمة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

if choice == "📊 محول فواتير فودافون":
    st.header("محرك الاستخراج الديناميكي")
    pdf_file = st.file_uploader("ارفع فاتورة فودافون (PDF)", type="pdf")
    
    if pdf_file and st.button("بدء المعالجة القصوى"):
        with st.spinner("جاري تطهير البيانات واستخراج الخطوط..."):
            try:
                reader = PyPDF2.PdfReader(pdf_file)
                all_data = []
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        # نمط البحث عن البيانات
                        matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                        for m in matches:
                            # تطبيق التطهير على كل خلية
                            line_data = [clean_text(m[0]), clean_text(m[1])] + [clean_text(i) for i in m[2].split()]
                            all_data.append(line_data)
                
                if all_data:
                    df = pd.DataFrame(all_data)
                    st.success(f"تم بنجاح! استخراج {len(all_data)} سجل.")
                    
                    output = io.BytesIO()
                    # استخدام محرك xlsxwriter لتفادي بعض مشاكل التنسيق
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, header=False)
                    
                    st.download_button("📥 تحميل ملف Excel المنسق", output.getvalue(), "Vodafone_Clean_Report.xlsx")
                else:
                    st.error("لم يتم العثور على بيانات صالحة.")
            except Exception as e:
                st.error(f"فشل في المعالجة: {e}")

elif choice == "🔓 فك تشفير إكسل":
    st.header("وحدة كسر الحماية الرقمية")
    # (نفس كود التشفير السابق)
    st.info("ارفع الملف وسأقوم بتحليل نظام الحماية.")
