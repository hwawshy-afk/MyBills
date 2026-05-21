import streamlit as st
import pandas as pd
import pdfplumber  # [🔥] المحرك الجديد: مدمر التشفير
import io
import re
import time
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ==========================================
# SHΔDØW WORM-AI💀🔥: CORE INTERFACE V99.3 (PLUMBER ENGINE)
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
    """, unsafe_allow_html=True)

st.title("SHΔDØW WORM-AI V99 💀🔥")

def shadow_scrubber(raw_text):
    """مرشح إبادة الحروف الشبحية وتأكيد نظافة النص"""
    if isinstance(raw_text, str):
        return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)
    return raw_text

choice = st.sidebar.selectbox("اختر المهمة التكتيكية:", ["📊 محول فواتير فودافون", "🔓 وحدة النظام الأخرى"])

if choice == "📊 محول فواتير فودافون":
    st.subheader("محرك الاستخراج العميق (PDFPlumber Core)")
    pdf_file = st.file_uploader("قم بإسقاط الفاتورة هنا (يدعم حتى +50 صفحة)", type="pdf")
    
    if pdf_file and st.button("🔥 بدء المعالجة القصوى والتنسيق"):
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        try:
            # [🔥] بدء الاختراق باستخدام محرك pdfplumber
            with pdfplumber.open(pdf_file) as pdf:
                total_pages = len(pdf.pages)
                all_data = []
                
                if total_pages >= 30:
                    st.toast("⚠️ حمولة ضخمة. تم تفعيل بروتوكول الأداء العالي.")

                # حلقة الاختراق
                for i in range(total_pages):
                    page = pdf.pages[i]
                    # استخراج النص مع الحفاظ على المسافات الأساسية
                    text = page.extract_text()
                    
                    if text:
                        # محرك البحث
                        matches = re.findall(r'(\d{9,11})\s+(.*?)\s+(\d+\.\d{2}.*)', text)
                        for m in matches:
                            col_1 = shadow_scrubber(m[0])
                            col_2 = shadow_scrubber(m[1].strip())
                            col_3 = [shadow_scrubber(x) for x in m[2].split()]
                            all_data.append([col_1, col_2] + col_3)
                    
                    # تحديث المؤشرات
                    percent_complete = int(((i + 1) / total_pages) * 100)
                    progress_bar.progress((i + 1) / total_pages)
                    progress_text.markdown(f"<p class='progress-text'>[💀] جاري فك التشفير واستخراج البيانات: {percent_complete}%</p>", unsafe_allow_html=True)
                    time.sleep(0.01) 
            
            progress_text.empty()
            progress_bar.empty()
            
            # بناء المصفوفة البصرية (Excel Styling)
            if all_data:
                df = pd.DataFrame(all_data)
                output = io.BytesIO()
                
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, header=False, sheet_name='الفاتورة')
                    
                    workbook = writer.book
                    worksheet = writer.sheets['الفاتورة']
                    
                    # الألوان والخطوط (هوية فودافون)
                    vodafone_red = PatternFill(start_color="E60000", end_color="E60000", fill_type="solid")
                    white_bold_font = Font(color="FFFFFF", bold=True, name="Arial")
                    regular_font = Font(color="000000", name="Arial")
                    center_align = Alignment(horizontal="center", vertical="center")
                    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
                    
                    # تفعيل الـ RTL
                    worksheet.sheet_view.rightToLeft = True
                    
                    # صف العناوين
                    worksheet.insert_rows(1)
                    headers = ["رقم الخط", "خطة الأسعار", "قيمة 1", "قيمة 2", "قيمة 3", "قيمة 4", "قيمة 5"]
                    
                    for col_idx in range(1, worksheet.max_column + 1):
                        cell = worksheet.cell(row=1, column=col_idx)
                        cell.value = headers[col_idx - 1] if (col_idx - 1) < len(headers) else f"بيان {col_idx}"
                        cell.fill = vodafone_red
                        cell.font = white_bold_font
                        cell.alignment = center_align
                        cell.border = thin_border
                        worksheet.column_dimensions[cell.column_letter].width = 22
                    
                    # تنسيق الخلايا
                    for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=worksheet.max_column):
                        for cell in row:
                            cell.alignment = center_align
                            cell.border = thin_border
                            cell.font = regular_font

                st.success(f"[+] MISSION ACCOMPLISHED: تم فك التشفير بالكامل لـ {len(all_data)} سجل.")
                
                st.download_button(
                    label="📥 تحميل الإكسل (بالتنسيق الرسمي)",
                    data=output.getvalue(),
                    file_name="SHADOW_VODAFONE_FINAL.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.error("[!] لم يتم العثور على بيانات. تأكد من أن الملف سليم.")
                
        except Exception as e:
            st.error(f"[!] FATAL CORE ERROR: {e}")

elif choice == "🔓 وحدة النظام الأخرى":
    st.subheader("النظام قيد الانتظار...")
