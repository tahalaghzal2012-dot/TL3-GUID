import subprocess

def run_adb(command):
    # Runs adb shell commands
    try:
        return subprocess.run(f"adb shell {command}", shell=True, capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def apply_global_optimizations():
    print("Applying system-level battery optimizations...")

    # Disable Wi-Fi Scanning (Always available)
    # Value 0 = disabled, 1 = enabled
    run_adb("settings put global wifi_scan_always_enabled 0")
    print("Wi-Fi scanning disabled.")

    # Disable Bluetooth Scanning (Always available)
    run_adb("settings put global ble_scan_always_enabled 0")
    print("Bluetooth scanning disabled.")

    # Reduce Location Accuracy/Scanning overhead
    # This disables the "Improve Location Accuracy" feature
    run_adb("settings put global location_mode 0") 
    print("Location scanning restricted.")

    print("\nOptimizations applied successfully!")

if __name__ == "__main__":
    apply_global_optimizations()