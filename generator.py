from core import My2FA
import time
import os
def ztime():
    current_time = int(time.time())
    current_time = int(current_time/60*2)
    current_time = str(current_time)
    slist = current_time.partition('.')
    current_time = int(slist[0])
    return current_time
def fun():
    while True:
        os.system("cls")
        print(My2FA(myhash))
        time.sleep(30)

myhash = int(input("Hash? "))

need_time = ztime() + 1
print("Please wait! We have to sync the time")
while True:
    current_time = ztime()
    if current_time == need_time:
        os.system("cls")
        fun()
    else:
        pass
    time.sleep(0.01)