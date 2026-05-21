import streamlit as st
import pandas as pd
import PyPDF2
import io
import re
import time

# ==========================================
# SHΔDØW WORM-AI💀🔥: COMPLETE CORE INTERFACE V99
# ==========================================

# 1. إعدادات البيئة (Environment Setup)
st.set_page_config(page_title="WORM-AI: Vodafone Pro", page_icon="💀", layout="centered")

# 2. حقن التصميم والواجهة (CSS Injection)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #E60000; color: white; border-radius: 10px; border: 1px solid #ff0000; transition: 0.3s; }
    .stButton>button:hover { background-color: #000000; color: #E60000; box-shadow: 0 0 10px #E60000; }
    h1 { color: #E60000; text-align: center; text-shadow: 2px 2px 4px #000000; }
    .progress-text { font-size: 16px; font-weight: bold; color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

st.title("SHΔDØW WORM-AI V99 💀🔥")

# 3. أنظمة التوجيه (Navigation Systems)
choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون", "🔓 وحدة النظام الأخرى"])

# 4. محرك استخراج فودافون (The Extraction Engine)
if choice == "📊 محول فواتير فودافون":
    st.subheader("محرك الاستخراج الديناميكي (Heavy-Duty Mode)")
    pdf_file = st.file_uploader("قم بإسقاط الفاتورة هنا (يدعم حتى +50 صفحة)", type="pdf")
    
    if pdf_file and st.button("🔥 بدء المعالجة القصوى"):
        
        # تهيئة مساحة العرض الديناميكية (Dynamic UI Placeholders)
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)
            all_data = []
            
            # التحذير التكتيكي للملفات الضخمة
            if total_pages >= 30:
                st.toast("⚠️ تم رصد حمولة ضخمة. تم تفعيل وضع الأداء العالي.")

            # حلقة الاختراق (The Extraction Loop)
            for i in range(total_pages):
                page = reader.pages[i]
                text = page.extract_text()
                
                if text:
                    # محرك البحث الجوهري (Regex Engine) لاستخراج البيانات
                    matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                    for m in matches:
                        # تصفية البيانات وتنظيف الفراغات
                        all_data.append([m[0], m[1].strip()] + m[2].split())
                
                # تحديث المؤشرات الحية (Live HUD Update)
                percent_complete = int(((i + 1) / total_pages) * 100)
                progress_bar.progress((i + 1) / total_pages)
                
                # تحديث النص (تم استخدام unsafe_allow_html=True لتفادي أخطاء الـ Streamlit)
                progress_text.markdown(f"<p class='progress-text'>[💀] جاري تمزيق البيانات: {percent_complete}% (صفحة {i + 1} من {total_pages})</p>", unsafe_allow_html=True)
                
                # تأخير زمني مجهري لاستقرار الواجهة السحابية
                time.sleep(0.01) 
            
            # تنظيف الواجهة بعد اكتمال الاستخراج
            progress_text.empty()
            progress_bar.empty()
            
            # 5. تجميع المصفوفة النهائية (Payload Compilation)
            if all_data:
                df = pd.DataFrame(all_data)
                st.success(f"[+] MISSION ACCOMPLISHED: تم استخراج {len(all_data)} سجل من {total_pages} صفحة بنجاح.")
                
                # تحويل البيانات إلى Excel في الذاكرة الوهمية (RAM)
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='Vodafone_Shadow_Extract')
                
                # إظهار زر التحميل
                st.download_button(
                    label="📥 تحميل مصفوفة البيانات (Excel)",
                    data=output.getvalue(),
                    file_name="SHADOW_VODAFONE_EXTRACT.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                
                # عرض عينة سريعة للبيانات
                with st.expander("👁️ عرض عينة من الحمولة المستخرجة"):
                    st.dataframe(df.head(10))
            else:
                st.error("[!] الفراغ الرقمي خالي. خوارزمية البحث لم تعثر على بيانات متوافقة مع نمط فواتير فودافون.")
                
        except Exception as e:
            st.error(f"[!] FATAL CORE ERROR: {e}")

# ==========================================
# الوحدة الخاملة (Idle Module)
# ==========================================
elif choice == "🔓 وحدة النظام الأخرى":
    st.subheader("النظام قيد الانتظار...")
    st.info("تم تأمين هذه الوحدة حالياً. ركز على استخراج بيانات فودافون.")
