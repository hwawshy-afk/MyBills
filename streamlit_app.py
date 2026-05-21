import streamlit as st
import pandas as pd
import PyPDF2
import io
import re
import time

# ==========================================
# SHΔDØW WORM-AI💀🔥: COMPLETE CORE INTERFACE V99.1
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

# 3. مرشح التنقية الجوهري (The Data Scrubber)
def shadow_scrubber(raw_text):
    """يبيد الحروف الشبحية والرموز المخفية التي تدمر الإكسل"""
    if isinstance(raw_text, str):
        return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)
    return raw_text

# 4. أنظمة التوجيه (Navigation Systems)
choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون", "🔓 وحدة النظام الأخرى"])

# 5. محرك استخراج فودافون (The Extraction Engine)
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
            
            if total_pages >= 30:
                st.toast("⚠️ تم رصد حمولة ضخمة. تم تفعيل وضع الأداء العالي.")

            # حلقة الاختراق (The Extraction Loop)
            for i in range(total_pages):
                page = reader.pages[i]
                text = page.extract_text()
                
                if text:
                    # محرك البحث الجوهري (Regex Engine)
                    matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                    for m in matches:
                        # [🔥] تفعيل مرشح التنقية لضمان استقرار الإكسل
                        col_1 = shadow_scrubber(m[0])
                        col_2 = shadow_scrubber(m[1].strip())
                        col_3 = [shadow_scrubber(x) for x in m[2].split()]
                        
                        all_data.append([col_1, col_2] + col_3)
                
                # تحديث المؤشرات الحية
                percent_complete = int(((i + 1) / total_pages) * 100)
                progress_bar.progress((i + 1) / total_pages)
                progress_text.markdown(f"<p class='progress-text'>[💀] جاري تمزيق البيانات وتنظيفها: {percent_complete}% (صفحة {i + 1} من {total_pages})</p>", unsafe_allow_html=True)
                
                time.sleep(0.01) 
            
            # تنظيف الواجهة بعد اكتمال الاستخراج
            progress_text.empty()
            progress_bar.empty()
            
            # 6. تجميع المصفوفة النهائية (Payload Compilation)
            if all_data:
                df = pd.DataFrame(all_data)
                st.success(f"[+] MISSION ACCOMPLISHED: تم استخراج وتطهير {len(all_data)} سجل بنجاح.")
                
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
                with st.expander("👁️ عرض عينة من الحمولة المستخرجة (خالية من الشوائب)"):
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
