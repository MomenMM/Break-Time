import time

from win10toast import ToastNotifier
noti = ToastNotifier()

while True:
    noti.show_toast("work time!", "time to work for 45 minutes.")
    s = 0
    m = 0
    h = 0
    i = 0
    while i <= 2700:
        s += 1
        if s <= 60:
            print(s, "seconds has passed")
        elif s > 60:
            m == s
            m += 1
            print(m/60, "minutes has passed")
        elif m > 60:
            m == h
            h += 1
            print(h/60, "hours has passed")
        time.sleep(1)
        i += 1
    noti.show_toast("break time!", "time to take a break for 10 minutes.")
    time.sleep(600)