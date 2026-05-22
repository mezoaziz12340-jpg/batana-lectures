from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

STUDENT_ID = "12004672"
TEACHER_ID = "1221715"

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
            button:hover { background: #1e3f73; }
            .error { color: red; margin-top: 10px; }
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

@app.post("/login", response_class=HTMLResponse)
def login(role: str = Form(...), user_id: str = Form(...)):
    if role == "student" and user_id == STUDENT_ID:
        return HTMLResponse("<h2 style='text-align:center;padding:50px;'>مرحباً بالطالب<br>صفحة المحاضرات قادمة</h2>")
    elif role == "teacher" and user_id == TEACHER_ID:
        return HTMLResponse("<h2 style='text-align:center;padding:50px;'>مرحباً بالأستاذ<br>صفحة رفع المحاضرات قادمة</h2>")
    else:
        return HTMLResponse("""
            <h2 style='text-align:center;padding:50px;color:red;'>البيانات غير صحيحة</h2>
            <div style='text-align:center;'><a href='/'>العودة لتسجيل الدخول</a></div>
        """)
