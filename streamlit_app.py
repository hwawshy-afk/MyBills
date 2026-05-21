import streamlit as st
import pandas as pd
import pdfplumber
import io
import re
import time
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ==========================================
# SHΔDØW WORM-AI💀🔥: THE ABSOLUTE GRID V99.5
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
    val = int(match.group(1))
    if 19 <= val <= 28:
        return str(val - 19)
    elif val == 3:
        return ' '
    return ''

def shadow_scrubber(raw_text):
    """تطهير، فك تشفير، ومعالجة الخلايا الفارغة"""
    if raw_text is None or str(raw_text).strip() == "":
        return "0.00" # ملء الفراغات لمنع الانزياح
    
    raw_text = str(raw_text)
    raw_text = re.sub(r'\(cid:(\d+)\)', decrypt_vodafone_cipher, raw_text)
    raw_text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)
    return raw_text.strip()

choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون (النسخة المطابقة)", "🔓 وحدة النظام الأخرى"])

if choice == "📊 محول فواتير فودافون (النسخة المطابقة)":
    st.subheader("محرك الاستخراج الهيكلي (Structural Cloning)")
    pdf_file = st.file_uploader("قم بإسقاط الفاتورة هنا", type="pdf")
    
    if pdf_file and st.button("🔥 استنساخ الفاتورة المطابقة"):
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        try:
            with pdfplumber.open(pdf_file) as pdf:
                total_pages = len(pdf.pages)
                all_data = []
                
                # العناوين الـ 11 الثابتة بناءً على الصورة
                headers = [
                    "رقم الخط", "خطة الأسعار", "رسوم شهرية", "رسوم محلية", 
                    "رسوم دولية", "رسوم تجوال", "رسوم خدمات", "رسوم و خصومات أخرى", 
                    "القيمة الإجمالية قبل الضرائب", "رسوم خدمات معفاة من الضرائب", "القيمة الإجمالية بعد الضرائب"
                ]
                
                if total_pages >= 30:
                    st.toast("⚠️ جاري تفعيل بروتوكول الشبكة الصارمة (Strict Grid).")

                # حلقة الاختراق الهيكلي
                for i in range(total_pages):
                    page = pdf.pages[i]
                    # [🔥] التغيير الجوهري: استخراج الجداول كشبكة هندسية وليس كنص
                    tables = page.extract_tables()
                    
                    for table in tables:
                        for row in table:
                            # تجاهل الصفوف الفارغة أو صفوف العناوين المكررة
                            if not row or row[0] is None or "رقم الخط" in str(row):
                                continue
                                
                            # تنظيف وتجهيز الصف
                            cleaned_row = [shadow_scrubber(cell) for cell in row]
                            
                            # إجبار الصف على أن يكون 11 عموداً بالضبط
                            if len(cleaned_row) > 1: # التأكد من أنه صف بيانات فعلي
                                # عكس ترتيب المصفوفة إذا كانت مقلوبة من الـ PDF (من اليسار لليمين)
                                # إذا كان أول عمود ليس رقماً، نقوم بعكسه
                                if not re.match(r'\d+', cleaned_row[0]):
                                    cleaned_row.reverse()
                                    
                                # ضبط العدد لـ 11 عمود
                                if len(cleaned_row) < 11:
                                    cleaned_row.extend(["0.00"] * (11 - len(cleaned_row)))
                                elif len(cleaned_row) > 11:
                                    cleaned_row = cleaned_row[:11]
                                    
                                all_data.append(cleaned_row)
                    
                    percent_complete = int(((i + 1) / total_pages) * 100)
                    progress_bar.progress((i + 1) / total_pages)
                    progress_text.markdown(f"<p class='progress-text'>[💀] جاري بناء الشبكة المطابقة: {percent_complete}%</p>", unsafe_allow_html=True)
                    time.sleep(0.01) 
            
            progress_text.empty()
            progress_bar.empty()
            
            if all_data:
                df = pd.DataFrame(all_data, columns=headers)
                output = io.BytesIO()
                
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='البيانات_المالية')
                    
                    workbook = writer.book
                    worksheet = writer.sheets['البيانات_المالية']
                    
                    # التصميم البصري المطابق للصورة (Visual Clone)
                    red_fill = PatternFill(start_color="E60000", end_color="E60000", fill_type="solid")
                    gray_fill = PatternFill(start_color="E0E0E0", end_color="E0E0E0", fill_type="solid")
                    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
                    
                    white_bold = Font(color="FFFFFF", bold=True, name="Arial")
                    regular_font = Font(color="000000", name="Arial")
                    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
                    border_style = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
                    
                    # توجيه الملف ليقرأ من اليمين لليسار (RTL)
                    worksheet.sheet_view.rightToLeft = True
                    
                    # تثبيت العناوين (Headers)
                    worksheet.insert_rows(1)
                    
                    for col_idx in range(1, len(headers) + 1):
                        cell = worksheet.cell(row=1, column=col_idx)
                        cell.value = headers[col_idx - 1]
                        cell.fill = red_fill
                        cell.font = white_bold
                        cell.alignment = center_align
                        cell.border = border_style
                        # ضبط اتساع الأعمدة
                        worksheet.column_dimensions[cell.column_letter].width = 18 if col_idx > 2 else 22
                    
                    # تنسيق الخلايا وتلوين الصفوف (Zebra Striping المطابق للصورة)
                    for row_idx, row in enumerate(worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=11), start=2):
                        # تلوين رمادي وأبيض بالتبادل
                        current_fill = gray_fill if row_idx % 2 == 0 else white_fill
                        for cell in row:
                            cell.alignment = center_align
                            cell.border = border_style
                            cell.font = regular_font
                            cell.fill = current_fill

                st.success(f"[+] MISSION ACCOMPLISHED: تم استنساخ {len(all_data)} سجل بالهيكل البصري المطابق (11 عمود).")
                
                st.download_button(
                    label="📥 تحميل الإكسل (النسخة المطابقة)",
                    data=output.getvalue(),
                    file_name="SHADOW_VODAFONE_CLONE.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.error("[!] لم يتم العثور على جداول هيكلية قابلة للفك.")
                
        except Exception as e:
            st.error(f"[!] FATAL CORE ERROR: {e}")

elif choice == "🔓 وحدة النظام الأخرى":
    st.subheader("النظام قيد الانتظار...")
