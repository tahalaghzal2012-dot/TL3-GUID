import subprocess

PROTECTED_PACKAGES = {
    # Core System
    "com.android.systemui", "com.android.settings", "com.android.phone",
    "com.android.providers.telephony", "com.android.bluetooth",
    "com.android.networkstack",
    
    # Google Services
    "com.google.android.gms", "com.android.vending", "com.google.android.gsf",
    
    # Required Apps
    "com.google.android.calendar", 
    "com.google.android.deskclock",
    
    # Samsung Specifics
    "com.samsung.android.incallui", "com.samsung.android.app.telephonyui"
}

def run_termux_cmd(command):
    try:
        cmd = f"su -c '{command}'"
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def optimize_device():
    print("Fetching third-party packages...")
    raw_pkgs = run_termux_cmd("pm list packages -3")
    pkgs = [p.replace("package:", "").strip() for p in raw_pkgs.splitlines()]
    
    for pkg in pkgs:
        if pkg in PROTECTED_PACKAGES:
            print(f"Skipping protected: {pkg}")
            continue
        
        print(f"Optimizing: {pkg}")
        # Restrict background execution
        run_termux_cmd(f"cmd appops set {pkg} RUN_ANY_IN_BACKGROUND ignore")
        
        # Force into 'rare' bucket
        run_termux_cmd(f"am set-standby-bucket {pkg} rare")

if __name__ == "__main__":
    optimize_device()
    print("\nOptimization complete.")
    print("If an app misbehaves, revert it with:")
    print("su -c 'am set-standby-bucket <package_name> active'")