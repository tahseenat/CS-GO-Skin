import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
from credentials import password, username, cs_go_home_url, steam_url
from skin_details import get_src


def buy(skin_name):
    try:
        driver.find_element(By.XPATH, """(//*[contains(text(), '{}')])[1]""".format(skin_name)).click()
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Withdraw')])[2]""").click()
        driver.find_element(By.XPATH, """//*[@id="trade-url"]""").send_keys(steam_url)
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Confirm')])[1]""").click()
    except:
        pass


# if __name__ == "__main__":

# specify waits in sec
soft_wait = 2
long_wait = 4
dota_wait = 1.2
refresh_wait = 1

driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver_win32/chromedriver.exe')

driver.get(cs_go_home_url)

time.sleep(long_wait + soft_wait)
driver.find_element(By.XPATH, """(//*[contains( text(), "Sign In")])[1]""").click()
time.sleep(long_wait)

driver.find_element(By.XPATH, """//*[@id = "steamAccountName"]""").send_keys(username)
driver.find_element(By.XPATH, """//*[@id="steamPassword"]""").send_keys(password)
driver.find_element(By.XPATH, """//*[@id="imageLogin"]""").click()

time.sleep(long_wait)

driver.find_element(By.XPATH, """//*[contains(text(), 'Continue')]""").click()
driver.find_element(By.XPATH, """(//*[contains(text(), 'Withdraw')])[1]""").click()

skin_name = "Golden Staff"

while True:
    driver.refresh()
    time.sleep(refresh_wait)
    try:
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Dota')])[1]""").click()
        # dataframe read and pass the name of skin in buy function
        for i in range (dataframe)
            buy(i)
    except:
        pass
    time.sleep(dota_wait)
