from core import My2FA
import time

myhash = int(input("Hash? "))
while True:
    code = int(input("Code? "))
    need = My2FA(myhash)
    
    if need == code:
        print("Code Validated!")

    else:
        print("Code Rejected!")

    