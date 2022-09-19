import time

from win10toast import ToastNotifier
noti = ToastNotifier()

while True:
    noti.show_toast("look at you! you did a lot of work today!", "take a break for 10 minutes, you need it!", duration=2700)
    time.sleep(600)