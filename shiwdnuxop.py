Shiwdnux op.py
import os
import shutil
import subprocess
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def run(cmd):
    if not shutil.which("adb"):
        print(RED + "ADB install nahi hai!" + RESET)
        input("Enter dabao...")
        return
    try:
        subprocess.run(cmd, timeout=20)
    except Exception as e:
        print("Error:", e)
    input("\nEnter dabao...")

def menu():
    os.system("clear")
    print(CYAN + r"""
  ███████╗██╗  ██╗██████╗
  ██╔════╝██║  ██║██╔══██╗
  ███████╗███████║██████╔╝
  ╚════██║██╔══██║██╔══██╗
  ███████║██║  ██║██║  ██║
  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

       S H R Y A N S H
            T O O L
    """ + RESET)
    print(GREEN + "===== ADB CONTROL CENTER =====" + RESET)
    print("1. Check ADB devices")
    print("2. Phone information")
    print("3. Battery information")
    print("4. List installed packages")
    print("5. Show Android version")
    print("6. Take screenshot")
    print("7. View connected device logs")
    print("8. Open Android settings")
    print("9. Reboot device")
    print("0. Exit")
    return input("\nSHRYANSH > ")

while True:
    choice = menu()

    if choice == "1":
        run(["adb", "devices", "-l"])

    elif choice == "2":
        run(["adb", "shell", "getprop"])

    elif choice == "3":
        run(["adb", "shell", "dumpsys", "battery"])

    elif choice == "4":
        run(["adb", "shell", "pm", "list", "packages", "-3"])

    elif choice == "5":
        run(["adb", "shell", "getprop", "ro.build.version.release"])

    elif choice == "6":
        if shutil.which("adb"):
            result = subprocess.run(
                ["adb", "shell", "screencap", "-p",
                 "/sdcard/shryansh.png"],
                capture_output=True
            )
            if result.returncode == 0:
                subprocess.run([
                    "adb", "pull", "/sdcard/shryansh.png", "."
                ])
            else:
                print("Screenshot failed.")
            input("Enter dabao...")

    elif choice == "7":
        run(["adb", "logcat", "-d", "-t", "100"])

    elif choice == "8":
        run(["adb", "shell", "am", "start",
             "-a", "android.settings.SETTINGS"])

    elif choice == "9":
        confirm = input("Connected device reboot karein? (yes/no): ")
        if confirm.lower() == "yes":
            run(["adb", "reboot"])

    elif choice == "0":
        print("SHRYANSH TOOL band ho raha hai...")
        break

    else:
        print("Invalid option!")
        tshiwdnux op.py
import os
import shutil
import subprocess
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def run(cmd):
    if not shutil.which("adb"):
        print(RED + "ADB install nahi hai!" + RESET)
        input("Enter dabao...")
        return
    try:
        subprocess.run(cmd, timeout=20)
    except Exception as e:
        print("Error:", e)
    input("\nEnter dabao...")

def menu():
    os.system("clear")
    print(CYAN + r"""
  ███████╗██╗  ██╗██████╗
  ██╔════╝██║  ██║██╔══██╗
  ███████╗███████║██████╔╝
  ╚════██║██╔══██║██╔══██╗
  ███████║██║  ██║██║  ██║
  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

       S H R Y A N S H
            T O O L
    """ + RESET)
    print(GREEN + "===== ADB CONTROL CENTER =====" + RESET)
    print("1. Check ADB devices")
    print("2. Phone information")
    print("3. Battery information")
    print("4. List installed packages")
    print("5. Show Android version")
    print("6. Take screenshot")
    print("7. View connected device logs")
    print("8. Open Android settings")
    print("9. Reboot device")
    print("0. Exit")
    return input("\nSHRYANSH > ")

while True:
    choice = menu()

    if choice == "1":
        run(["adb", "devices", "-l"])

    elif choice == "2":
        run(["adb", "shell", "getprop"])

    elif choice == "3":
        run(["adb", "shell", "dumpsys", "battery"])

    elif choice == "4":
        run(["adb", "shell", "pm", "list", "packages", "-3"])

    elif choice == "5":
        run(["adb", "shell", "getprop", "ro.build.version.release"])

    elif choice == "6":
        if shutil.which("adb"):
            result = subprocess.run(
                ["adb", "shell", "screencap", "-p",
                 "/sdcard/shryansh.png"],
                capture_output=True
            )
            if result.returncode == 0:
                subprocess.run([
                    "adb", "pull", "/sdcard/shryansh.png", "."
                ])
            else:
                print("Screenshot failed.")
            input("Enter dabao...")

    elif choice == "7":
        run(["adb", "logcat", "-d", "-t", "100"])

    elif choice == "8":
        run(["adb", "shell", "am", "start",
             "-a", "android.settings.SETTINGS"])

    elif choice == "9":
        confirm = input("Connected device reboot karein? (yes/no): ")
        if confirm.lower() == "yes":
            run(["adb", "reboot"])

    elif choice == "0":
        print("SHRYANSH TOOL band ho raha hai...")
        break

    else:
        print("Invalid option!")
        time.sleep(1)
