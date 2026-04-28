# Library version checker
libraries = ["tensorflow", "keras", "numpy","streamlit" ,"matplotlib", "pandas", "torch", "sklearn","groq"]

print("Checking installed libraries:\n")

for lib in libraries:
    try:
        module = __import__(lib)
        version = getattr(module, "__version__", "Unknown")
        print(f"{lib:<15} ✅ Installed (version: {version})")
    except ImportError:
        print(f"{lib:<15} ❌ Not installed")