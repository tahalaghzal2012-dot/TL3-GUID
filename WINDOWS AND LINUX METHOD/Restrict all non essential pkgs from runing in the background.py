import subprocess

# List of critical packages that must NEVER be restricted
# Includes system, Google services, Clock, and Calendar
PROTECTED_PACKAGES = {
    # Core System
    "com.android.systemui", "com.android.settings", "com.android.phone",
    "com.android.providers.telephony", "com.android.bluetooth",
    "com.android.networkstack",
    
    # Google Services
    "com.google.android.gms", "com.android.vending", "com.google.android.gsf",
    
    # Required Apps (as requested)
    "com.google.android.calendar", 
    "com.google.android.deskclock",
    
    # Samsung Specifics (Often required for basic device function)
    "com.samsung.android.incallui", "com.samsung.android.app.telephonyui"
}

def run_adb(command):
    try:
        return subprocess.run(f"adb shell {command}", shell=True, capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def optimize_device():
    print("Fetching third-party packages...")
    # List only 3rd party packages
    raw_pkgs = run_adb("pm list packages -3")
    pkgs = [p.replace("package:", "").strip() for p in raw_pkgs.splitlines()]
    
    for pkg in pkgs:
        if pkg in PROTECTED_PACKAGES:
            print(f"Skipping protected: {pkg}")
            continue
        
        print(f"Optimizing: {pkg}")
        # Restrict background execution (App Ops)
        run_adb(f"cmd appops set {pkg} RUN_ANY_IN_BACKGROUND ignore")
        
        # Force into 'rare' bucket (Most restrictive Standby Bucket)
        run_adb(f"am set-standby-bucket {pkg} rare")

if __name__ == "__main__":
    optimize_device()
    print("\nOptimization complete.")
    print("If an app misbehaves, revert it with:")
    print("adb shell am set-standby-bucket <package_name> active")