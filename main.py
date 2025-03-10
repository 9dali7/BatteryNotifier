import os
import psutil
import sys
import shutil
import winshell
from time import sleep
from win10toast import ToastNotifier
from win32com.client import Dispatch

toaster = ToastNotifier()

def Alert(title, msg, duration=10):
    toaster.show_toast(title, msg, duration=duration)

def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, "BatteryNotifier.lnk")

    if not os.path.exists(shortcut_path):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.Description = "Battery Monitor"
        shortcut.Save()
        print("Added To Autostart!")

add_to_startup()

while True:
    battery_info = psutil.sensors_battery()
    if battery_info:
        percent = battery_info.percent
        plugged = battery_info.power_plugged

        if not plugged and percent <= 25:
            Alert('Low Battery', "Please, Charge The Battery")

    sleep(60)

