# backend/test_commit.py
print("🔍 Testing import of routers.commit...")

try:
    from routers import commit
    print("✅ Imported commit module successfully")
    print("📁 Module file:", commit.__file__)
    print("🧩 Has 'router'?", hasattr(commit, 'router'))
    if hasattr(commit, 'router'):
        print("🎯 Router object:", commit.router)
        print("🔢 Number of routes:", len(commit.router.routes))
    else:
        print("❌ Missing 'router' attribute!")
except Exception as e:
    print("💥 Import failed:", str(e))