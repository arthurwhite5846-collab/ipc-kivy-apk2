# IPC Calculator (Kivy) — APK Build Template

هذا المشروع يحتوي على كود تطبيق Kivy الذي أرسلته **جاهز كقالب** لبناء ملف APK باستخدام Buildozer (Android).

> **ملاحظة مهمة:** أنا لا أستطيع تشغيل Android SDK/NDK وبناء ملف APK فعليًا داخل هذه المحادثة، لكن أرسلت لك المشروع كاملًا (main.py + buildozer.spec + Workflow جاهز لـ GitHub Actions) بحيث تستطيع استخراج الـ APK بسهولة على جهازك أو من GitHub.

---

## 1) طريقة البناء على لينكس / WSL (الموصى بها)

### المتطلبات
- Ubuntu 20.04/22.04 أو WSL2 Ubuntu على ويندوز
- Python 3 + pip
- Java (OpenJDK)

### الأوامر
داخل نفس مجلد المشروع:

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk   python3-pip autoconf libtool pkg-config   zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5   cmake libffi-dev libssl-dev liblzma-dev libsqlite3-dev

python3 -m pip install --upgrade pip
python3 -m pip install --user buildozer cython virtualenv

# أول مرة قد يقوم Buildozer بتنزيل Android SDK/NDK تلقائياً
~/.local/bin/buildozer -v android debug
```

بعد النجاح ستجد الـ APK هنا:
- `bin/`  (مثال: `bin/ipccalculator-0.1.0-arm64-v8a_armeabi-v7a-debug.apk`)

---

## 2) بناء APK تلقائيًا عبر GitHub Actions (بدون إعدادات محلية)

هذا المشروع يحتوي على Workflow جاهز:
- `.github/workflows/android.yml`

الخطوات:
1. ارفع هذا المشروع إلى GitHub Repo جديد.
2. ادخل على تبويب **Actions**.
3. شغّل Workflow باسم **Build APK (Kivy/Buildozer)** (workflow_dispatch).
4. بعد انتهاء البناء ستجد الـ APK كـ Artifact وتقوم بتحميله.

---

## 3) إصدار Release (اختياري)

- Debug APK مناسب للاختبار.
- لو تريد Release APK موقّع (Signing) تحتاج إنشاء keystore وتوقيع التطبيق.  
يمكنك لاحقًا تشغيل:

```bash
buildozer android release
```

ثم توقيع الناتج باستخدام jarsigner / apksigner (حسب بيئة أندرويد لديك).

---

## تعديل اسم الحزمة/الأيقونة

- اسم التطبيق: `buildozer.spec` → `title`
- package name/domain:  
  - `package.name`  
  - `package.domain`
- أيقونة التطبيق: ضع أيقونة 512×512 في `assets/icon.png`

---

## الملفات المهمة
- `main.py` : كود التطبيق
- `buildozer.spec` : إعدادات بناء APK
- `.github/workflows/android.yml` : بناء APK على GitHub Actions
