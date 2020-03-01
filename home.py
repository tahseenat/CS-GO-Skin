import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from credentials import cs_go_home_url, steam_url, withdraw_url, exe_path
from skin_details import get_src


def add_skin(i):
    item = "(//*[contains(text(), '{}')])[1]".format(data['skin_name'][i])
    try:
        driver.find_element(By.XPATH, item).click()
        data['no_of_skin'][i] -= 1

    except Exception as e:
        print("Exception adding skin")
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
        try:
            driver.find_element(By.XPATH, """//*[@id="trade-url"]""").send_keys(steam_url)
        except:
            pass
        driver.find_element(By.XPATH, """(//*[contains(text(), 'Confirm')])[1]""").click()
    except Exception as e:
        print("Exception in Buy functionality", e)


if __name__ == "__main__":

    # specify waits in sec
    soft_wait = 2
    long_wait = 4
    dota_wait = 2.5
    refresh_wait = 1.4
    hold_page = 0.3
    login_wait = 4

    file_name = "Skins.csv"

    driver = webdriver.Chrome(executable_path=exe_path)

    driver.get(cs_go_home_url)

    #  manual login will be done under a minute
    time.sleep(login_wait)

    # skin_name = "Golden Staff"
    data = pd.read_csv(file_name)
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
            for page in range(2):
                # data frame read and pass the name of skin in buy function
                for i in data.index:
                    if data['no_of_skin'][i] > 0:
                        add_skin(i)
                try:
                    driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]").click()
                    time.sleep(1.5)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
        buy()
        data.to_csv(file_name, index=False)
        time.sleep(dota_wait)
