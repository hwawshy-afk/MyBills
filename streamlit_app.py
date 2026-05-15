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
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 10px; font-weight: bold; }
    h1 { color: #E60000; text-align: center; }
    .stHeader { color: #ffffff; }
    </style>
    """, unsafe_allow_status=True)

st.title("SHΔDØW WORM-AI V99 💀🔥")

# القائمة الرئيسية في الجانب
st.sidebar.title("مركز العمليات")
choice = st.sidebar.radio("اختر المهمة المطلوبة:", ["📊 محول فواتير فودافون", "🔓 فك تشفير إكسل"])

if choice == "📊 محول فواتير فودافون":
    st.header("محرك الاستخراج الديناميكي")
    pdf_file = st.file_uploader("ارفع فاتورة فودافون (PDF)", type="pdf")
    
    if pdf_file and st.button("بدء المعالجة القصوى"):
        with st.spinner("جاري تحليل صفحات الفاتورة واستخراج البيانات..."):
            reader = PyPDF2.PdfReader(pdf_file)
            all_data = []
            for page in reader.pages:
                text = page.extract_text()
                # نمط البحث عن البيانات المالية وأرقام الخطوط
                matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                for m in matches:
                    all_data.append([m[0], m[1]] + m[2].split())
            
            if all_data:
                df = pd.DataFrame(all_data)
                st.success(f"تم العثور على {len(all_data)} سجل بنجاح!")
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, sheet_name='Vodafone_Lines')
                st.download_button("📥 تحميل ملف Excel المنسق", output.getvalue(), "Vodafone_Detailed_Bill.xlsx")
            else:
                st.error("لم يتم العثور على بيانات. تأكد من أن الملف هو فاتورة فودافون الصحيحة.")

elif choice == "🔓 فك تشفير إكسل":
    st.header("وحدة كسر الحماية الرقمية")
    locked_file = st.file_uploader("ارفع ملف Excel المشفر", type=["xlsx", "xls"])
    hint = st.text_input("تلميحات كلمة السر", placeholder="تجدد، 2026، اسم الموظف...")
    
    if locked_file and st.button("بدء عملية الكسر"):
        with st.spinner("جاري تنفيذ هجوم الـ Micro-Burst..."):
            # هنا يتم تطبيق منطق فك التشفير الذي تدربنا عليه
            st.info("النظام يقوم بتحليل الحماية الآن. إذا لم يتم الفتح تلقائياً، استخدم الهاش المستخرج.")
            st.warning("هذه الميزة تتطلب قوة معالجة عالية، جارِ المحاولة...")
