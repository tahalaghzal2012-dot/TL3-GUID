⚠️ Disclaimer: All tweaks and scripts included in this guide are safe and tested across the Galaxy S22, S23, S24, and S25 series. However, you are responsible for your own device. Make sure to back up your important files before proceeding.

📌 Repository Link & Credits
All automated execution scripts and package lists referenced in this guide are open-source and hosted in my GitHub repository:

👉 TL3-GUIDE GitHub Repository

Special Acknowledgments:

Shino’s Ultimate Battery Guide: Inspiration for baseline device configuration and system settings tweaks.

🛠️ Phase 1: On-Device Settings Optimization
Before running any scripts, prepare your phone with these baseline system settings.  

Step 1: Factory Reset Your Phone (Optional, but Highly Recommended)  
Why it helps: Clearing out old residual files, leftover cache from system updates, and conflicting app configurations gives you a completely clean slate for maximum battery efficiency.  

How to do it: Settings ➔ General management ➔ Reset ➔   Factory data reset

Step 2: Set Up as New (Don't Restore Old Settings)  
Why it helps: Restoring backups from Smart Switch or Google Cloud often reinstalls corrupted cache files, hidden background daemons, and old battery-draining app configurations.  

How to do it: During initial device setup, select "Don't copy" / "Set up as new device" and manually download only the apps you actively use.

Step 3: Turn Off Always On Display (AOD)
Why it helps: Keeps the screen controller completely asleep when the device is idle, saving roughly 1% to 1.5% battery per hour throughout the day.

How to do it: Settings ➔ Lock screen and AOD ➔ Toggle Always On Display OFF

Step 4: Turn On Power Saving Mode (With Adaptive Refresh Rate Keep-Alive)
Why it helps: Power Saving mode restricts background network sync, location checks, and background tasks. Leaving Adaptive Refresh Rate active gives you full 120Hz display smoothness while targeting background resource consumption.

How to do it: Settings ➔ Device care ➔ Battery ➔ Power saving ➔ Uncheck Limit motion smoothness to Standard (keep Adaptive Hz enabled), then toggle Power saving ON.

Step 5: Enable Light Performance Mode
Why it helps: Light mode optimizes processing speeds and thermals to prioritize battery life and cooling without causing noticeable lag in daily use or gaming.

How to do it: Settings ➔ Device care ➔ Performance profile ➔ Select Light

Step 6: Disable Battery Optimization for Critical Apps
Why it helps: Standard One UI battery optimization can interfere with essential background synchronization, leading to delayed push notifications or erratic app behavior.

How to do it: Settings ➔ Apps ➔ Select your desired app ➔ Battery ➔ Set to Unrestricted

Step 7: Put Unused Apps into Deep Sleep
Why it helps: Prevents apps you rarely open from starting background services, tracking location, or draining battery when you aren't using them.

How to do it: Settings ➔ Device care ➔ Battery ➔ Background usage limits ➔ Toggle Put unused apps to sleep ON

Step 8: Disable Nearby Device Scanning
Why it helps: Stops your phone's Bluetooth and Wi-Fi modems from continuously scanning for surrounding devices in the background 24/7.  

How to do it: Settings ➔ Connections ➔ More connection settings ➔ Toggle Nearby device scanning OFF  

💻 Phase 2: Debloating Methods
Choose Method A (PC Scripts), Method B (Termux on Phone), or Method C (Canta + Shizuku GUI) depending on your setup.

Method A: For Windows & Linux Users
Requirements:  
Python 3 installed on your PC.  

Android SDK Platform Tools (ADB) installed and added to your system PATH.  

USB Debugging enabled on your phone (Settings ➔ Developer options ➔ USB debugging).  

Instructions:  
Step 1: Download or clone the ZIP from the TL3-GUIDE GitHub Repo.  

Step 2: Connect your phone to your PC via USB and authorize the ADB prompt on your phone screen.  

Step 3: Open a command prompt or terminal inside the WINDOWS AND LINUX METHOD directory.  

Step 4: Execute all 4 Python files sequentially:  

Bash
python "disabling real time scaning.py"
python "Uninstalling Telemitry pkgs.py"
python "Restrict all non essential pkgs from runing in the background.py"
python "Restricting all third party apps from runing in the background.py"
Step 5: Restart your phone.  

Method B: For Termux Users (No PC Needed)  
Instructions:  
Step 1: Install and open Termux.  

Step 2: Copy and paste the following commands to clone the repo and run the scripts:

Bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/tahalaghzal2012-dot/TL3-GUIDE.git
cd TL3-GUIDE/"TERMUX METHOD"
python "Disabling in real time Scaning.py"
python "Uninstailing Telemetry Apps.py"
python "Restricting all PKGS from working in the background.py"
python "Restricting all Third party apps from working in the background.py"
Step 3: Restart your phone.

Method C: For Canta + Shizuku Users (GUI / No PC Needed)
Requirements:
Shizuku (Activated and permissions granted).

Canta (Installed and authorized via Shizuku).

JSON Viewer/Editor app (Recommended: JSON Forge on Google Play).

Instructions:
Step 1: Download the repository from Ruvomain-Protocol GitHub Repository.

Step 2: Open the directory matching your phone series (e.g., Ruvomain-Protocole/Configs/S22+/, S23+/, S24+/, or S25+/).

Step 3: Select one of the JSON files (Recommended: Stable version).

Step 4: Open the file using your JSON viewer/editor app and copy all the text inside it.

Step 5: Open Canta (ensure it is activated via Shizuku with required permissions granted), then tap the 3 dots menu ➔ Presets ➔ Import presets ➔ Import presets from clipboard ➔ Apply.

Step 6: Restart your phone.

⚡ Phase 3: Advanced ADB System Tweaks
Note: Run these commands via Command Prompt / Terminal on your PC (or via Termux/Shizuku local shell) ONLY AFTER you have restarted your phone from Phase 2.

1. Aggressive Doze Timing Tweaks  
Bash
adb shell settings put global device_idle_constants "inactive_to=30000,sensing_to=0,locating_to=0,location_accuracy=20,motion_inactive_to=0,idle_after_inactive_to=0,idle_pending_to=30000,max_idle_pending_to=60000,idle_pending_factor=2.0,idle_to=3600000,max_idle_to=21600000,idle_factor=2.0,min_time_to_alarm=60000"
What it does: Forces Android to enter Deep Doze mode almost immediately after the screen turns off, significantly reducing overnight standby battery drain.  

2. Limit Battery Saver Background Execution Duration  
Bash
adb shell settings put global battery_saver_constants "background_max_duration=30000"
What it does: Restricts background tasks from running longer than 30 seconds continuously when power saver features are active.  

3. Optimize RAM Usage by Limiting Cached Processes  
Bash
adb shell device_config put activity_manager max_cached_processes 24
What it does: Caps system RAM cache to 24 active background processes, reducing CPU overhead and keeping thermals cool.

4. Enforce Strict App Background Execution Limits
Bash
adb shell settings put global app_restriction_enabled true
What it does: Enforces strict system-level background execution rules on non-essential apps trying to wake up the CPU.

5. Enable Android Standby Buckets
Bash
adb shell settings put global app_standby_enabled 1
What it does: Enables Android's built-in intelligent power management to categorize apps based on usage frequency and restrict inactive ones automatically.




🟢 After TL3 Optimization (100% to 0% Drain Test):
Screen-On Time (SOT): [Add your after SOT hours here]

Battery Drain Profile: Ice cold thermals, zero background drain, and maximum screen-on duration.

