from datetime import datetime
from time import sleep
from datetime import timedelta

max_time_s = input("数える時間を秒で指定 : ")

print(f"{max_time_s}秒カウントダウンします")

max_time = int(max_time_s)

for count in range(max_time, 0, -1):
    print(f"{count:02d}", end="\r")
    sleep(1)
print()