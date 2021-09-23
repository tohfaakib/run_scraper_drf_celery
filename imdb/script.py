import csv
import re

import regex as regex
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys

def config_driver():
    data_dir = 'imdb/data'
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
    driver = webdriver.Chrome(executable_path="imdb/chromedriver", options=options,
                              desired_capabilities=d)

    return driver

def regex_text(pattern, text):
    text = str(text)
    try:
        pattern = re.compile(r'{}'.format(pattern))
        matches = re.search(pattern, text)
        return matches.group(1)
    except Exception as e:
        print(e)
        return ''

def regex_find_all(pattern, text):
    text = str(text)

    try:
        matches = regex.findall(r'{}'.format(pattern), text)
        return matches
    except Exception as e:
        print(e)
        return ''


def convertTuple(tup):

    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str


save_csv_call_counter = 0
output_file_name = 'output.csv'

def save_csv(movie_title, movie_url, people_url, name, title, known_for, phones, emails, websites, contact_block, about_block):
    global save_csv_call_counter
    fields = [movie_title, movie_url, people_url, name, title, known_for, phones, emails, websites, contact_block, about_block]

    header = ['movie_title', 'movie_url', 'people_url', 'name', 'title', 'known_for', 'phones', 'emails', 'websites', 'contact_block', 'about_block']
    with open(output_file_name, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if save_csv_call_counter == 0:
            writer.writerow(header)
        writer.writerow(fields)
    save_csv_call_counter += 1


def scrape_people(people_urls, movie_title, movie_url, driver):
    for people_url in people_urls:
        name, title, known_for, phones, emails, websites, contact_block, about_block = [''] * 8
        people_url = str(people_url).split('?')[0] + '/about'
        print(movie_title)
        driver.get(people_url)
        time.sleep(1)

        name = driver.find_element_by_xpath('//*[@id="name_heading"]/div/div/div[2]/div[1]/h1/span').text
        print(name)
        title = driver.find_element_by_xpath('//*[@id="name_page_primary_professions"]').text
        print(title)
        known_for = driver.find_element_by_xpath('//*[@id="const_page_summary_section"]/div[2]').text
        print(known_for)

        contact_block = driver.find_element_by_xpath('//*[@id="tabs_row"]/div/div/div/div/div[1]').text
        # print(contact_block)
        about_block = driver.find_element_by_xpath('//*[@id="const_tabs"]/div[2]').text
        # print(about_block)

        phones = regex_find_all("(\+?[0-9]+([0-9]|\/|\(|\)|\-| ){10,})", contact_block + ' ' + about_block)
        phones = [convertTuple(x).strip() for x in phones]
        phones = list(set(phones))
        phones = ', '.join(phones)

        emails = regex_find_all("([A-Za-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", contact_block + ' ' + about_block)
        emails = [convertTuple(x).strip() for x in emails]
        emails = list(set(emails))
        emails = ', '.join(emails)


        websites = regex_find_all("((http(s)?://)?([\w-]+\.)+[\w-]+(/[\w\- ;,./?%&=]*)?)", contact_block + ' ' + about_block)
        # print(websites)
        websites = [x[0] for x in websites]
        websites = [x for x in websites if len(x.split('.')[-1]) >= 2]
        websites = list(set(websites))
        if 'bing.com' in websites:
            websites.remove('bing.com')
        websites = ', '.join(websites)

        print(phones)
        print(emails)
        print(websites)

        save_csv(movie_title, movie_url, people_url, name, title, known_for, phones, emails, websites, contact_block, about_block)


def scrape_details(movie_urls, driver):
    for movie_url in movie_urls:
        movie_url = str(movie_url).split('?')[0] + '/filmmakers'
        driver.get(movie_url)
        time.sleep(1)
        title = str(driver.find_element_by_id("title_heading").find_element_by_tag_name('span').text).strip()
        table = None
        try:
            table = driver.find_element_by_id("title_filmmakers_music_department_sortable_table")
        except Exception as e:
            # print(e)
            pass

        if table:
            trs = table.find_elements_by_tag_name('tr')
            trs.pop(0)
            # print(trs[0].text)
            people_urls = []
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                people_url = tds[0].find_element_by_tag_name('a').get_attribute('href')
                # print(people_url)
                people_urls.append(people_url)
            scrape_people(people_urls, title, movie_url, driver)



        # break


def start(driver):
    cards = driver.find_elements_by_class_name("search-results__display-card")
    movie_urls = []
    for card in cards:
        movie_url = card.find_element_by_tag_name('a').get_attribute("href")
        # print(movie_url)
        movie_urls.append(movie_url)

    scrape_details(movie_urls, driver)

    time.sleep(20)
    # driver.close()


# if __name__ == '__main__':
def main(start_url, start_page_number):
    driver = config_driver()
    # start_url = 'https://pro.imdb.com/discover/title?type=movie&status=production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_prod'
    print(start_url)
    print(start_page_number)
    for i in range(int(start_page_number), 9999999):
        start_url_page = f'{start_url}&pageNumber={i}'
        driver.get(start_url_page)
        time.sleep(3)
        no_match_flag = '''<span>
            


No matches found for your search
        </span>'''
        if no_match_flag in str(driver.page_source):
            driver.close()
            break

        start(driver)

        break
    driver.close()
