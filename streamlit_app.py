import streamlit as st
import pandas as pd
import PyPDF2
import io
import re
import time

# ==========================================
# SHΔDØW WORM-AI💀🔥: CORE INTERFACE V99
# ==========================================

st.set_page_config(page_title="WORM-AI: Vodafone Pro", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 10px; border: 1px solid #ff0000; transition: 0.3s; }
    .stButton>button:hover { background-color: #000000; color: #E60000; box-shadow: 0 0 10px #E60000; }
    h1 { color: #E60000; text-align: center; text-shadow: 2px 2px 4px #000000; }
    .progress-text { font-size: 16px; font-weight: bold; color: #00ff00; }
    </style>
    """, unsafe_allow_status=True)

st.title("SHΔDØW WORM-AI V99 💀🔥")

choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون", "🔓 وحدة النظام الأخرى"])

if choice == "📊 محول فواتير فودافون":
    st.subheader("محرك الاستخراج الديناميكي (Heavy-Duty Mode)")
    pdf_file = st.file_uploader("قم بإسقاط الفاتورة هنا (يدعم حتى +50 صفحة)", type="pdf")
    
    if pdf_file and st.button("🔥 بدء المعالجة القصوى"):
        
        # 1. تهيئة مساحة العرض الديناميكية (Dynamic UI Placeholders)
        progress_text = st.empty()
        progress_bar = st.progress(0)
        status_log = st.empty()
        
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)
            all_data = []
            
            # التحذير التكتيكي للملفات الضخمة
            if total_pages >= 30:
                st.toast("⚠️ تم رصد حمولة ضخمة. تم تفعيل وضع الأداء العالي.")

            # 2. حلقة الاختراق والاستخراج (The Extraction Loop)
            for i in range(total_pages):
                page = reader.pages[i]
                text = page.extract_text()
                
                if text:
                    # محرك البحث (Regex Engine)
                    matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                    for m in matches:
                        all_data.append([m[0], m[1]] + m[2].split())
                
                # 3. تحديث المؤشرات الحية (Live HUD Update)
                percent_complete = int(((i + 1) / total_pages) * 100)
                
                # تحديث شريط التقدم والنص
                progress_bar.progress((i + 1) / total_pages)
                progress_text.markdown(f"<p class='progress-text'>[💀] جاري تمزيق البيانات: {percent_complete}% (صفحة {i + 1} من {total_pages})</p>", unsafe_allow_status=True)
                
            
            # 4. تجميع المصفوفة النهائية (Payload Compilation)
            progress_text.empty() # إخفاء النص بعد الانتهاء
            progress_bar.empty()  # إخفاء شريط التقدم
            
            if all_data:
                # إنشاء الإطار
                df = pd.DataFrame(all_data)
                st.success(f"[+] MISSION ACCOMPLISHED: تم استخراج {len(all_data)} سجل من {total_pages} صفحة بنجاح.")
                
                # تحويل البيانات إلى Excel في الذاكرة الوهمية (RAM)
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='Vodafone_Shadow_Extract')
                
                # 5. إظهار زر التحميل فقط بعد الانتهاء
                st.download_button(
                    label="📥 تحميل مصفوفة البيانات (Excel)",
                    data=output.getvalue(),
                    file_name="SHADOW_VODAFONE_EXTRACT.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                
                # عرض عينة سريعة للبيانات المستخرجة
                with st.expander("👁️ عرض عينة من الحمولة المستخرجة"):
                    st.dataframe(df.head(10))
            else:
                st.error("[!] الفراغ الرقمي خالي. خوارزمية البحث لم تعثر على بيانات مالية متوافقة.")
                
        except Exception as e:
            st.error(f"[!] FATAL CORE ERROR: {e}")

elif choice == "🔓 وحدة النظام الأخرى":
    st.subheader("النظام قيد الانتظار...")
    st.info("تم تأمين هذه الوحدة حالياً. ركز على استخراج البيانات.")
