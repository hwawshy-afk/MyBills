import streamlit as st
import pandas as pd
import pdfplumber
import io
import re
import time
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ==========================================
# SHΔDØW WORM-AI💀🔥: THE TITANIUM MATRIX V99.4
# ==========================================

st.set_page_config(page_title="WORM-AI: Vodafone Pro", page_icon="💀", layout="wide")

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

def decrypt_vodafone_cipher(match):
    """خوارزمية فك تشفير CID الخاصة بفودافون"""
    val = int(match.group(1))
    if 19 <= val <= 28:
        return str(val - 19)  # مفتاح الإزاحة السري
    elif val == 3:
        return ' ' # مسافة
    return ''

def shadow_scrubber(raw_text):
    """تطهير وفك تشفير البيانات"""
    if isinstance(raw_text, str):
        # فك تشفير الـ CID
        raw_text = re.sub(r'\(cid:(\d+)\)', decrypt_vodafone_cipher, raw_text)
        # إبادة الحروف الشبحية
        raw_text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)
        return raw_text.strip()
    return raw_text

choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون", "🔓 وحدة النظام الأخرى"])

if choice == "📊 محول فواتير فودافون":
    st.subheader("محرك الاستخراج (كاسر التشفير وشبكة التيتانيوم)")
    pdf_file = st.file_uploader("قم بإسقاط الفاتورة هنا", type="pdf")
    
    if pdf_file and st.button("🔥 اختراق، فك تشفير، وتنسيق"):
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        try:
            with pdfplumber.open(pdf_file) as pdf:
                total_pages = len(pdf.pages)
                all_data = []
                
                if total_pages >= 30:
                    st.toast("⚠️ تم تفعيل بروتوكول الأداء العالي.")

                for i in range(total_pages):
                    page = pdf.pages[i]
                    text = page.extract_text()
                    
                    if text:
                        # محرك البحث الجوهري
                        matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                        for m in matches:
                            col_1 = shadow_scrubber(m[0])
                            col_2 = shadow_scrubber(m[1])
                            
                            # استخراج القيم المالية
                            financials = m[2].split()
                            financials = [shadow_scrubber(x) for x in financials]
                            
                            # [🔥] شبكة التيتانيوم: إجبار البيانات على 5 أعمدة مالية لمنع الترحيل
                            financials = (financials + ['0', '0', '0', '0', '0'])[:5]
                            
                            all_data.append([col_1, col_2] + financials)
                    
                    percent_complete = int(((i + 1) / total_pages) * 100)
                    progress_bar.progress((i + 1) / total_pages)
                    progress_text.markdown(f"<p class='progress-text'>[💀] جاري فك التشفير وتثبيت المصفوفة: {percent_complete}%</p>", unsafe_allow_html=True)
                    time.sleep(0.01) 
            
            progress_text.empty()
            progress_bar.empty()
            
            if all_data:
                df = pd.DataFrame(all_data)
                output = io.BytesIO()
                
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='البيانات_المالية')
                    
                    workbook = writer.book
                    worksheet = writer.sheets['البيانات_المالية']
                    
                    # التصميم البصري (هوية فودافون)
                    red_fill = PatternFill(start_color="E60000", end_color="E60000", fill_type="solid")
                    white_bold = Font(color="FFFFFF", bold=True, name="Arial")
                    regular_font = Font(color="000000", name="Arial")
                    center_align = Alignment(horizontal="center", vertical="center")
                    border_style = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
                    
                    # توجيه الملف ليقرأ من اليمين لليسار (RTL)
                    worksheet.sheet_view.rightToLeft = True
                    
                    # تثبيت العناوين (Headers)
                    worksheet.insert_rows(1)
                    headers = ["رقم الخط", "خطة الأسعار", "الرسوم الشهرية", "رسوم أخرى", "القيمة قبل الضرائب", "الضرائب", "القيمة الإجمالية"]
                    
                    for col_idx in range(1, len(headers) + 1):
                        cell = worksheet.cell(row=1, column=col_idx)
                        cell.value = headers[col_idx - 1]
                        cell.fill = red_fill
                        cell.font = white_bold
                        cell.alignment = center_align
                        cell.border = border_style
                        # ضبط اتساع الأعمدة
                        worksheet.column_dimensions[cell.column_letter].width = 22 if col_idx <= 2 else 18
                    
                    # تنسيق الخلايا وتوسيطها
                    for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=7):
                        for cell in row:
                            cell.alignment = center_align
                            cell.border = border_style
                            cell.font = regular_font

                st.success(f"[+] MISSION ACCOMPLISHED: تم كسر التشفير وتثبيت {len(all_data)} سجل دون انزياح.")
                
                st.download_button(
                    label="📥 تحميل الإكسل (جاهز للاستخدام)",
                    data=output.getvalue(),
                    file_name="SHADOW_VODAFONE_PERFECTED.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.error("[!] لم يتم العثور على بيانات قابلة للفك.")
                
        except Exception as e:
            st.error(f"[!] FATAL CORE ERROR: {e}")

elif choice == "🔓 وحدة النظام الأخرى":
    st.subheader("النظام قيد الانتظار...")
