import os
import psutil
from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()

def Alert(title, msg, duration=10):
        toaster.show_toast(title, msg, duration=duration)

while True:
    percent = psutil.sensors_battery().percent
    battery = psutil.sensors_battery().power_plugged

    if not battery:
        if percent <= 25:
            msg = "Please, Charge The Battery"
            Alert('Low Battery', msg)

    sleep(60)

