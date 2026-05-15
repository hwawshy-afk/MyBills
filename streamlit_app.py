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
    h1 { color: #E60000; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.title("SHΔDØW WORM-AI V99 💀🔥")

# القائمة الرئيسية
st.sidebar.title("مركز العمليات")
choice = st.sidebar.radio("اختر المهمة المطلوبة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

if choice == "📊 محول فواتير فودافون":
    st.header("محرك الاستخراج الديناميكي")
    pdf_file = st.file_uploader("ارفع فاتورة فودافون (PDF)", type="pdf")
    
    if pdf_file and st.button("بدء المعالجة القصوى"):
        with st.spinner("جاري تحليل الصفحات واستخراج البيانات..."):
            try:
                reader = PyPDF2.PdfReader(pdf_file)
                all_data = []
                for page in reader.pages:
                    text = page.extract_text()
                    matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                    for m in matches:
                        all_data.append([m[0], m[1]] + m[2].split())
                
                if all_data:
                    df = pd.DataFrame(all_data)
                    st.success(f"تم بنجاح! العثور على {len(all_data)} خط.")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False)
                    st.download_button("📥 تحميل ملف Excel المنسق", output.getvalue(), "Vodafone_Report.xlsx")
                else:
                    st.error("لم يتم العثور على بيانات. تأكد من جودة ملف الـ PDF.")
            except Exception as e:
                st.error(f"حدث خطأ أثناء المعالجة: {e}")

elif choice == "🔓 فك تشفير إكسل":
    st.header("وحدة كسر الحماية الرقمية")
    locked_file = st.file_uploader("ارفع ملف Excel المشفر", type=["xlsx", "xls"])
    hint = st.text_input("تلميحات كلمة السر", placeholder="تجدد، 2026...")
    
    if locked_file and st.button("بدء عملية الكسر"):
        st.info("جاري تحليل خوارزمية التشفير...")
        # سيتم تنفيذ هجوم الـ Micro-Burst هنا
        st.warning("هذه الميزة تحت الاختبار في النسخة التجريبية.")
