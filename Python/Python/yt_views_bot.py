from selenium import webdriver
import time

time.sleep(3)

no_of_drivers = 2
url = "https://youtu.be/kB5mJHjHW0M"
refresh_time = 4
drivers = []

for i in range(no_of_drivers):
    drivers.append(webdriver.Chrome(
        executable_path="123456890-[80-=-=i5967854"))
    drivers[i].get(url)
while True:
    time.sleep(refresh_time)
    for i in range(no_of_drivers):
        drivers[i].refresh()
