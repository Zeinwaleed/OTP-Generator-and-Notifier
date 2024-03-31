import random
import string
from win10toast import ToastNotifier
otp = 'w'
def random_numbers():
    nums = string.digits
    numsls = []
    for i in range(0,4):
        numsls.append(nums[random.randint(0,9)])
    global otp
    otp = "".join(numsls)
random_numbers()
notification = ToastNotifier()
notification.show_toast("otp number",f"your otp number is {otp}",icon_path="eif")

