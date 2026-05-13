import os
import json
import shutil # مكتبة مخصصة للتعامل مع المجلدات وحذفها

# 1. تحديد المسارات بدقة
BASE_PATH = "/storage/emulated/0/SAEED_MARKET_SITE"
FILE_NAME = "saeed_databot_config.json"
FULL_PATH = os.path.join(BASE_PATH, FILE_NAME)

# 2. بيانات الإعدادات الخاصة بمشروعك
project_config = {
    "model": "gemini-1.5-flash",
    "project_name": "Saeed DataBot",
    "version": "1.0",
    "assets": os.path.join(BASE_PATH, "assets")
}

def force_save_config():
    print("--- بدء عملية الإصلاح والحفظ النهائي ---")
    
    # التأكد من وجود المجلد الرئيسي أولاً
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    # معالجة مشكلة "المجلد المعاند" الظاهرة في الصورة 1000188131.jpg
    if os.path.exists(FULL_PATH):
        if os.path.isdir(FULL_PATH): # إذا وجد مجلداً بهذا الاسم
            print("⚠️ تم اكتشاف مجلد خاطئ.. جاري الحذف الآن.")
            shutil.rmtree(FULL_PATH) # حذف المجلد تماماً
        else:
            print("ℹ️ الملف موجود كملف نصي، سيتم تحديثه.")

    # 3. كتابة البيانات في ملف JSON حقيقي
    try:
        with open(FULL_PATH, 'w', encoding='utf-8') as f:
            json.dump(project_config, f, indent=4, ensure_ascii=False)
        print(f"✅ مبروك يا سعيد! تم حفظ الملف بنجاح في: {FULL_PATH}")
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    force_save_config()
