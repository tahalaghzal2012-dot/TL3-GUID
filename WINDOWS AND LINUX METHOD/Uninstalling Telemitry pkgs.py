import subprocess

# Optimized list excluding the apps you want to keep
TO_UNINSTALL = [
    "com.samsung.android.knox.analytics.uploader",
    "com.samsung.android.bixby.agent",
    "com.samsung.android.visionintelligence",
    "com.sec.android.diagmonagent",
    "com.samsung.android.networkdiagnostic",
    "com.samsung.android.app.watchmanagerstub"
]

def run_optimization():
    for pkg in TO_UNINSTALL:
        print(f"Uninstalling: {pkg}")
        # -k keeps the data, --user 0 is the current user
        result = subprocess.run(["adb", "shell", "pm", "uninstall", "-k", "--user", "0", pkg], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully removed {pkg}")
        else:
            print(f"Failed to remove {pkg} (it may already be gone)")

if __name__ == "__main__":
    run_optimization()
    print("\nOptimization complete.")