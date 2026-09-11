import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
from dotenv import load_dotenv
## set_up 

load_dotenv()
browser = webdriver.Chrome(options=Options())
browser.maximize_window()
browser.get(os.getenv("WEBSITE_ADDRESS"))
time.sleep(1.5)

# get data
def get_data():
    df = pd.read_csv(os.getenv("CSV_TO_UPLOAD"))
    return(df)


### Login ###
def login():
    time.sleep(1)
    #button = browser.find_element(By.XPATH, "//button[contains(@class,'ant-btn css-6e21uj ant-btn-text ant-btn-sm')]")
    #button.click()
    browser.find_elements(By.XPATH, "//button[contains(@class,'ant-btn')]")[0].click()
    time.sleep(1)

    email = browser.find_element(By.ID, "email")
    password = browser.find_element(By.ID, "password")
    email.send_keys(os.getenv("EMAIL_ADDRESS"))
    password.send_keys(os.getenv("PASSWORD"))
    browser.find_elements(By.XPATH, "//button[contains(@class,'ant-btn')]")[3].click()
    time.sleep(2)

### enter data 
def main_loop(df):
    for index in range(len(df)):
        print(df.iloc[index])
        browser.find_elements(By.XPATH, "//button[contains(@class,'ant-btn')]")[1].click()
        
        first_name = browser.find_element(By.ID, "firstName")
        first_name.send_keys(df.iloc[index]["name"])

        team = browser.find_element(By.ID, "lastName")
        team.send_keys( "-" + df.iloc[index]["team"])

        value = browser.find_element(By.ID, "value")
        value.send_keys("1")
        position = browser.find_element(By.ID, "positionName")
        position.click()
        time.sleep(0.5)
        if df.iloc[index]["position"] == "goalkeeper" or df.iloc[index]["position"] == "goalkeeper ":
            position.send_keys(Keys.ENTER)
        elif df.iloc[index]["position"] == "defender" or df.iloc[index]["position"] == "defender ":
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.ENTER)
        elif df.iloc[index]["position"] == "midfielder" or df.iloc[index]["position"] == "midfielder ":
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.ENTER)
        else:  
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.DOWN)
            time.sleep(0.2)
            position.send_keys(Keys.ENTER)  
        browser.find_elements(By.XPATH, "//button[contains(@class,'ant-btn css-v8s1rb ant-btn-primary')]")[3].click()
        time.sleep(2)

if __name__ == "__main__":
    login()
    main_loop(get_data())

    