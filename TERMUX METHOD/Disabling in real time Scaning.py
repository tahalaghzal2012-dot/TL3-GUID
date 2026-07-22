import subprocess

def run_termux_cmd(command):
    # Runs system shell commands using su
    try:
        cmd = f"su -c '{command}'"
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def apply_global_optimizations():
    print("Applying system-level battery optimizations via Termux...")

    # Disable Wi-Fi Scanning
    run_termux_cmd("settings put global wifi_scan_always_enabled 0")
    print("Wi-Fi scanning disabled.")

    # Disable Bluetooth Scanning
    run_termux_cmd("settings put global ble_scan_always_enabled 0")
    print("Bluetooth scanning disabled.")

    # Restrict Location Scanning overhead
    run_termux_cmd("settings put global location_mode 0") 
    print("Location scanning restricted.")

    print("\nOptimizations applied successfully!")

if __name__ == "__main__":
    apply_global_optimizations()