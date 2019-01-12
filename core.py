import time

def My2FA(myhash):
    current_time = int(time.time())
    current_time = int(current_time/60*2)
    current_time = str(current_time)
    slist = current_time.partition('.')
    current_time = int(slist[0])
    to_print = str(current_time*myhash)
    to_print = int(to_print[-6:])
    return to_print

