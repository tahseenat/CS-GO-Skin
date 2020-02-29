import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from credentials import cs_go_home_url, steam_url, withdraw_url, exe_path
from skin_details import get_src


def add_skin(skin_name):
    print(skin_name)
    item = "(//*[contains(text(), '{}')])[1]".format(skin_name)
    try:
        driver.find_element(By.XPATH, item).click()
    except Exception as e:
        print(e)


def login():
    pass
    # driver.find_element(By.XPATH, """(//*[contains( text(), "Sign In")])[1]""").click()
    # time.sleep(long_wait)
    #
    # driver.find_element(By.XPATH, """//*[@id = "steamAccountName"]""").send_keys(username)
    # driver.find_element(By.XPATH, """//*[@id="steamPassword"]""").send_keys(password)
    # driver.find_element(By.XPATH, """//*[@id="imageLogin"]""").click()
    #
    # time.sleep(long_wait)
    #
    # driver.find_element(By.XPATH, """//*[contains(text(), 'Continue')]""").click()
    # driver.find_element(By.XPATH, """(//*[contains(text(), 'Withdraw')])[1]""").click()


def buy():
    try:
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Withdraw')])[2]""").click()
        driver.find_element(By.XPATH, """//*[@id="trade-url"]""").send_keys(steam_url)
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Confirm')])[1]""").click()
    except Exception as e:
        print(e)


if __name__ == "__main__":

    # specify waits in sec
    soft_wait = 2
    long_wait = 4
    dota_wait = 2.5
    refresh_wait = 1.4
    hold_page = 0.3
    login_wait = 40

    driver = webdriver.Chrome(executable_path=exe_path)

    driver.get(cs_go_home_url)

    #  manual login will be done under a minute
    time.sleep(login_wait)

    # skin_name = "Golden Staff"
    data = pd.read_csv("Skins.csv")
    print(data)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(withdraw_url)

    while True:
        driver.refresh()
        time.sleep(refresh_wait)
        try:
            driver.find_element(By.XPATH, """(//*[contains(text(), 'Dota')])[1]""").click()
            time.sleep(dota_wait)
            # data frame read and pass the name of skin in buy function
            for i in data.index:
                if data['Flag'][i] == "Not Sent":
                    add_skin(data['Skin_name'][i])

        except Exception as e:
            print(e)
        # buy()
        time.sleep(dota_wait)
