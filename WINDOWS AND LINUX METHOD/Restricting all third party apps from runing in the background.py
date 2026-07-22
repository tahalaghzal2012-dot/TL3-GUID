import subprocess

def get_packages():
    # Get all packages
    raw = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages']).decode('utf-8')
    all_pkgs = [line.replace('package:', '').strip() for line in raw.splitlines()]
    
    # Get system packages
    sys_raw = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages', '-s']).decode('utf-8')
    sys_pkgs = set([line.replace('package:', '').strip() for line in sys_raw.splitlines()])
    
    third_party = [p for p in all_pkgs if p not in sys_pkgs]
    system = [p for p in all_pkgs if p in sys_pkgs]
    
    return sorted(third_party), sorted(system)

def main():
    tp_apps, sys_apps = get_packages()
    
    # 1. Handle Third-Party Apps
    print(f"--- Found {len(tp_apps)} Third-Party Apps ---")
    for p in tp_apps: print(p)
    print("\nEnter package names to KEEP (skip restriction), comma-separated:")
    keep_input = input("> ").split(',')
    to_keep = {p.strip() for p in keep_input if p.strip()}
    
    # 2. Handle System Apps (Manual Opt-in)
    print(f"\n--- Found {len(sys_apps)} System Apps ---")
    print("WARNING: Only enter packages here if you are 100% sure they are non-essential.")
    print("Enter system package names to RESTRICT, comma-separated:")
    restrict_sys_input = input("> ").split(',')
    to_restrict_sys = {p.strip() for p in restrict_sys_input if p.strip()}
    
    # Execution
    # Restrict Third-Party
    for pkg in tp_apps:
        if pkg in to_keep:
            print(f"Keeping: {pkg}")
            continue
        print(f"Restricting 3P: {pkg}")
        subprocess.run(['adb', 'shell', 'cmd', 'appops', 'set', pkg, 'RUN_IN_BACKGROUND', 'ignore'])
        
    # Restrict Chosen System
    for pkg in to_restrict_sys:
        if pkg in sys_apps:
            print(f"Restricting SYS: {pkg}")
            subprocess.run(['adb', 'shell', 'cmd', 'appops', 'set', pkg, 'RUN_IN_BACKGROUND', 'ignore'])
        else:
            print(f"Package {pkg} not found in system list.")

    print("\nTask Complete.")

if __name__ == "__main__":
    main()