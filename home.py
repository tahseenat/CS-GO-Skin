import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import autoit
import keyboard

# if __name__ == "__main__":
cs_go_home = "https://csgoempire.com/withdraw"

# specify waits in sec
soft_wait = 2
long_wait = 4

driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver_win32/chromedriver.exe')

driver.get(cs_go_home)

time.sleep(long_wait + soft_wait)
