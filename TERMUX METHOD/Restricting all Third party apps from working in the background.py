import subprocess

def run_termux_cmd(command):
    cmd = f"su -c '{command}'"
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def get_packages():
    # Get all packages
    raw = run_termux_cmd('pm list packages')
    all_pkgs = [line.replace('package:', '').strip() for line in raw.splitlines()]
    
    # Get system packages
    sys_raw = run_termux_cmd('pm list packages -s')
    sys_pkgs = set([line.replace('package:', '').strip() for line in sys_raw.splitlines()])
    
    third_party = [p for p in all_pkgs if p not in sys_pkgs]
    system = [p for p in all_pkgs if p in sys_pkgs]
    
    return sorted(third_party), sorted(system)

def main():
    tp_apps, sys_apps = get_packages()
    
    # 1. Handle Third-Party Apps
    print(f"--- Found {len(tp_apps)} Third-Party Apps ---")
    for p in tp_apps: 
        print(p)
    print("\nEnter package names to KEEP (skip restriction), comma-separated:")
    keep_input = input("> ").split(',')
    to_keep = {p.strip() for p in keep_input if p.strip()}
    
    # 2. Handle System Apps
    print(f"\n--- Found {len(sys_apps)} System Apps ---")
    print("WARNING: Only enter packages here if you are 100% sure they are non-essential.")
    print("Enter system package names to RESTRICT, comma-separated:")
    restrict_sys_input = input("> ").split(',')
    to_restrict_sys = {p.strip() for p in restrict_sys_input if p.strip()}
    
    # Restrict Third-Party
    for pkg in tp_apps:
        if pkg in to_keep:
            print(f"Keeping: {pkg}")
            continue
        print(f"Restricting 3P: {pkg}")
        subprocess.run(f"su -c 'cmd appops set {pkg} RUN_IN_BACKGROUND ignore'", shell=True)
        
    # Restrict Chosen System
    for pkg in to_restrict_sys:
        if pkg in sys_apps:
            print(f"Restricting SYS: {pkg}")
            subprocess.run(f"su -c 'cmd appops set {pkg} RUN_IN_BACKGROUND ignore'", shell=True)
        else:
            print(f"Package {pkg} not found in system list.")

    print("\nTask Complete.")

if __name__ == "__main__":
    main()