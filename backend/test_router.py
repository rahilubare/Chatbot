# backend/test_router.py
print("🔍 Testing import of routers.chat...")

try:
    from routers import chat
    print("✅ Imported chat module successfully")
    print("📁 Module file:", chat.__file__)
    print("🧩 Has 'router'?", hasattr(chat, 'router'))
    if hasattr(chat, 'router'):
        print("🎯 Router object:", chat.router)
        print("🔢 Number of routes:", len(chat.router.routes))
    else:
        print("❌ Missing 'router' attribute!")
except Exception as e:
    print("💥 Import failed:", str(e))