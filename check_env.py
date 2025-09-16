import importlib
import sys

REQUIRED_PACKAGES = [
    "numpy",
    "scipy",
    "sklearn",
    "torch",
    "torchvision",
    "matplotlib"
]

def check_package(pkg):
    try:
        importlib.import_module(pkg)
        print(f"✅ {pkg} is installed")
        return True
    except ImportError:
        print(f"❌ {pkg} is NOT installed")
        return False

def main():
    print("🔍 Checking environment...\n")
    all_ok = True
    for pkg in REQUIRED_PACKAGES:
        if not check_package(pkg):
            all_ok = False

    if all_ok:
        print("\n🎉 Environment is ready!")
        sys.exit(0)
    else:
        print("\n⚠ Some packages are missing. Run: bash scripts/setup_env.sh")
        sys.exit(1)

if __name__ == "__main__":
    main()
