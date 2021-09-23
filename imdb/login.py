import csv
import re

import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys

def config_driver():
    data_dir = 'data'
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument(f"--user-data-dir={data_dir}")
    options.add_argument("--start-maximized")
    options.add_argument('—no-sandbox')
    options.add_argument('—disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    d[
        'phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options,
                              desired_capabilities=d)

    return driver


def start(url):
    driver = config_driver()
    driver.get(url)

    time.sleep(200)
    driver.close()


if __name__ == '__main__':
    start_url = 'https://pro.imdb.com/discover/title?type=movie&status=production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_prod'
    start(start_url)
