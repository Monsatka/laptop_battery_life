#batterylife_checker
#@author: Monika
#@date: 05.10.2020



import psutil
from plyer import notification
import time

battery=psutil.sensors_battery()
while True:
    percent=battery.percent
    if percent <= 20:
        notification.notify(
            title="Battery Percentage",
            message=f"{percent}% battery remaining",
            timeout=10
        )
        break

    time.sleep(60*5)
