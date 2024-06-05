import PyPDF2
from translate import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk

translator = Translator(to_lang="fa")
reader = PyPDF2.PdfReader("HTTP.The.Definitive.Guide.pdf")
page = reader.pages[22]
text = page.extract_text()
STRINg = ""
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()
x = width - 100
y = 750
list1 = []
# ایجاد یک فایل PDF جدید
pdf_file = "HTTP.The.Definitive.Guide(farsi).pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter
# اضافه کردن فونت "IranNastaliq"
font_path = "A-Sade/A-Sade.ttf"  # مسیر فایل فونت
pdfmetrics.registerFont(TTFont('A-Sade', font_path))
# تنظیم فونت برای متن فارسی
c.setFont("A-Sade", 15)

for i in text:
    STRINg += i
    if i == ".":
        text = STRINg.replace("""This is the Title of the Book, eMatter Edition
Copyright © 2008 O’Reilly & Associates, Inc.""", "").replace("All rights reserved.", "").replace("4 | Chapter 1: Overview of HTTP", "").replace("3Chapter 1This is the Title of the BookCHAPTER 1", "")
        translated_text = translator.translate(text)
        # print(translated_text)
        reshaped_text = arabic_reshaper.reshape(translated_text)
        bidi_text = get_display(reshaped_text)
        list1.append(bidi_text)
        # print(list1)
for list2 in list1:
        if list2 != "":
                print(list2)
        # c.drawString(x, y, list2)
        # y -= 20
    
c.save()
