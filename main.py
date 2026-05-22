from fastapi import FastAPI, Form, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

STUDENT_ID = "12004672"
TEACHER_ID = "1221715"

# ملف manifest
@app.get("/manifest.json")
def manifest():
    return {
        "name": "بوابة البطانة",
        "short_name": "البطانة",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#f5f5f5",
        "theme_color": "#2c5aa0",
        "icons": [{"src": "https://i.ibb.co/4ZQm9Qk/book-icon.png", "sizes": "192x192", "type": "image/png"}]
    }

# ملف Service Worker
@app.get("/sw.js")
def service_worker():
    js = """
    self.addEventListener('install', e => {
        e.waitUntil(caches.open('batana-v1').then(cache => {
            return cache.addAll(['/']);
        }));
    });
    self.addEventListener('fetch', e => {
        e.respondWith(caches.match(e.request).then(response => {
            return response || fetch(e.request);
        }));
    });
    """
    return Response(content=js, media_type="application/javascript")

# صفحة تسجيل الدخول - دي اللي عدلناها
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>تسجيل الدخول - بوابة البطانة</title>
        <link rel="manifest" href="/manifest.json">
        <meta name="theme-color" content="#2c5aa0">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script>
        if ('serviceWorker' in navigator) {
          navigator.serviceWorker.register('/sw.js');
        }
        </script>
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

@app.post("/login", response_class=HTMLResponse)
def login(role: str = Form(...), user_id: str = Form(...)):
    if role == "student" and user_id == STUDENT_ID:
        return student_page()
    elif role == "teacher" and user_id == TEACHER_ID:
        return teacher_page()
    else:
        return HTMLResponse("<h2 style='text-align:center;padding:50px;color:red;'>البيانات غير صحيحة</h2><div style='text-align:center;'><a href='/'>العودة لتسجيل الدخول</a></div>")

def student_page():
    return HTMLResponse("<div dir='rtl' style='font-family:Arial;padding:30px;'><h2>مرحباً بك في صفحة الطالب</h2><p>هنا حتظهر قائمة المحاضرات</p><br><a href='/'>تسجيل خروج</a></div>")

def teacher_page():
    return HTMLResponse("<div dir='rtl' style='font-family:Arial;padding:30px;'><h2>مرحباً بك في صفحة الأستاذ</h2><p>هنا حتقدر ترفع المحاضرات</p><br><a href='/'>تسجيل خروج</a></div>")
