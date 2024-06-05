import PyPDF2
from translate import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk

# مترجم را مقداردهی اولیه کنید
translator = Translator(to_lang="fa")

# PDF را بخوانید
reader = PyPDF2.PdfReader("HTTP.The.Definitive.Guide.pdf")
page = reader.pages[22]
text = page.extract_text()

# متن استخراج شده را پاکسازی کنید
text = text.replace("""This is the Title of the Book, eMatter Edition
Copyright © 2008 O’Reilly & Associates, Inc.""", "").replace("All rights reserved.", "").replace("4 | Chapter 1: Overview of HTTP", "").replace("3Chapter 1This is the Title of the BookCHAPTER 1", "")

# PDF خروجی را آماده کنید
pdf_file = "HTTP.The.Definitive.Guide(farsi).pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# فونت فارسی را اضافه کنید
font_path = "A-Sade/A-Sade.ttf"  # اطمینان حاصل کنید که این مسیر به فونت فارسی صحیح است
pdfmetrics.registerFont(TTFont('A-Sade', font_path))
c.setFont("A-Sade", 15)

# مقداردهی اولیه Tkinter برای دریافت ابعاد صفحه
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

# ترجمه و نوشتن در PDF
y = height - 100  # ارتفاع شروع را به دلخواه تنظیم کنید
paragraphs = text.split('.')  # متن را به جملات یا پاراگراف‌ها تقسیم کنید

for paragraph in paragraphs:
    if paragraph.strip():  # پردازش پاراگراف‌های غیر خالی
        translated_text = translator.translate(paragraph.strip())
        reshaped_text = arabic_reshaper.reshape(translated_text)
        bidi_text = get_display(reshaped_text)
        if y < 50:  # بررسی کنید که آیا صفحه پر شده است
            c.showPage()
            c.setFont("A-Sade", 15)
            y = height - 100  # موقعیت y را بازنشانی کنید

        c.drawString(100, y, bidi_text)
        y -= 20  # برای خط بعدی به پایین حرکت کنید

# PDF را ذخیره کنید
c.save()
