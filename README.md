# ترجمه و تبدیل متن PDF به فارسی

این اسکریپت برای استخراج متن از فایل PDF، ترجمه آن به فارسی و سپس ایجاد یک فایل PDF جدید با متن ترجمه شده طراحی شده است.

## پیش‌نیازها

برای اجرای این اسکریپت، به کتابخانه‌های زیر نیاز دارید:
- PyPDF2
- translate
- reportlab
- arabic_reshaper
- python-bidi
- tkinter

شما می‌توانید این کتابخانه‌ها را با استفاده از pip نصب کنید:
```bash
pip install PyPDF2 translate reportlab arabic_reshaper python-bidi tk
