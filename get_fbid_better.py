'''
Script to get all fbid of your friends.

Author: minhdq99hp
'''
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium_utils.selenium_utils import scroll_until_exists
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
# options.add_argument("--disable-infobars")
# options.add_argument("start-maximized")
# options.add_argument("--disable-extensions")

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.desktop-notification", 1)

driver = webdriver.Firefox(options=options, firefox_profile=profile)

user_data = None
with open('user_config.json', 'r') as f:
    user_data = json.load(f)


# Login into Facebook Mobile
driver.get('https://m.facebook.com')


email_input = driver.find_element_by_name('email')
password_input = driver.find_element_by_name('pass')
login_button = driver.find_element_by_name('login')

email_input.clear()
email_input.send_keys(user_data['email'])
password_input.clear()
password_input.send_keys(user_data['password'])

login_button.click()

not_now_button = driver.find_element_by_xpath('//a[@class="bl bn bo bp br bm"]')
not_now_button.click()

# Go to /friends page
friends_url = 'https://m.facebook.com/' + user_data['fbid'] + '/friends'
driver.get(friends_url)

# read page source to get friend's id.
id_list = []
while True:
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    for d in soup.find_all("a"):
        try:
            if '?fref=fr_tab' in d['href']:
                id_list.append(d['href'][1:len(d['href'])-12])
        except KeyError:
            continue

    try:
        see_more_button = driver.find_element_by_id('m_more_friends').find_element_by_tag_name('a')
        see_more_button.click()
        # print('click')
    except NoSuchElementException:
        break

with open('friendlist_better.txt', 'w', encoding='utf-8') as f:
    for fbid in id_list:
        f.write(fbid + '\n')

driver.close()
