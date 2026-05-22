from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

STUDENT_ID = "12004672"
TEACHER_ID = "1221715"

# صفحة تسجيل الدخول
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>تسجيل الدخول - بوابة البطانة</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f5f5f5; }
            form { background: white; padding: 30px; max-width: 400px; margin: auto; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            input, select, button { width: 100%; padding: 12px; margin: 10px 0; box-sizing: border-box; }
            button { background: #2c5aa0; color: white; border: none; cursor: pointer; font-size: 16px; }
        </style>
    </head>
    <body>
        <h2>بوابة محاضرات كلية البطانة</h2>
        <form method="post" action="/login">
            <input type="email" name="email" placeholder="الايميل" required>
            <select name="role" required>
                <option value="">اختر الدور</option>
                <option value="student">طالب</option>
                <option value="teacher">أستاذ</option>
            </select>
            <input type="text" name="user_id" placeholder="الرقم الجامعي/المرجعي" required>
            <button type="submit">دخول</button>
        </form>
    </body>
    </html>
    """

# التحقق وتحويل حسب الدور
@app.post("/login", response_class=HTMLResponse)
def login(role: str = Form(...), user_id: str = Form(...)):
    if role == "student" and user_id == STUDENT_ID:
        return student_page()
    elif role == "teacher" and user_id == TEACHER_ID:
        return teacher_page()
    else:
        return HTMLResponse("""
            <h2 style='text-align:center;padding:50px;color:red;'>البيانات غير صحيحة</h2>
            <div style='text-align:center;'><a href='/'>العودة لتسجيل الدخول</a></div>
        """)

# صفحة الطالب
def student_page():
    return HTMLResponse("""
    <div dir="rtl" style="font-family:Arial;padding:30px;">
        <h2>مرحباً بك في صفحة الطالب</h2>
        <p>هنا حتظهر قائمة المحاضرات للتحميل والمشاهدة</p>
        <div style="background:#f0f0f0;padding:20px;border-radius:8px;margin-top:20px;">
            <h3>المحاضرات المتاحة</h3>
            <p>لسه مافي محاضرات مرفوعة</p>
        </div>
        <br><a href="/">تسجيل خروج</a>
    </div>
    """)

# صفحة الأستاذ
def teacher_page():
    return HTMLResponse("""
    <div dir="rtl" style="font-family:Arial;padding:30px;">
        <h2>مرحباً بك في صفحة الأستاذ</h2>
        <p>هنا حتقدر ترفع المحاضرات وتحدد الزمن والمكان</p>
        <div style="background:#f0f0f0;padding:20px;border-radius:8px;margin-top:20px;">
            <h3>رفع محاضرة جديدة</h3>
            <p>خاصية الرفع جاية في الخطوة الجاية</p>
        </div>
        <br><a href="/">تسجيل خروج</a>
    </div>
    """)
