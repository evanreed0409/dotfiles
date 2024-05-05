import sys
import subprocess

def main(action):
    if action == "poweroff":
        subprocess.call(["poweroff"])
    elif action == "reboot":
        subprocess.call(["reboot"])
    else:
        print("Invalid action:", action)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./hyprland_power.py [poweroff|reboot]")
        sys.exit(1)
    action = sys.argv[1]
    main(action)
