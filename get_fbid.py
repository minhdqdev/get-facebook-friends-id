'''
Script to get all fbid of your friends.

Author: minhdq99hp
'''
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium_utils.selenium_utils import scroll_until_exists
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.desktop-notification", 1)

driver = webdriver.Firefox(options=options, firefox_profile=profile)

user_data = None
with open('user_config.json', 'r') as f:
    user_data = json.load(f)


# Login into Facebook
driver.get('http://www.facebook.com')


email_input = driver.find_element_by_id('email')
password_input = driver.find_element_by_id('pass')
login_button = driver.find_element_by_id('loginbutton')

email_input.clear()
email_input.send_keys(user_data['email'])
password_input.clear()
password_input.send_keys(user_data['password'])

login_button.click()


# Go to /friends page
avatar_img = driver.find_element_by_xpath('//a[@class="_2s25 _606w"]')
friends_url = avatar_img.get_attribute('href') + '/friends'
driver.get(friends_url)

scroll_until_exists(driver, ['pagelet_timeline_medley_movies', 'pagelet_timeline_medley_books', 
                                'pagelet_timeline_medley_music', 'pagelet_timeline_medley_photos', 
                                'pagelet_timeline_medley_videos', 'pagelet_timeline_medley_map', 
                                'pagelet_timeline_medley_likes', 'pagelet_timeline_medley_review', 
                                'pagelet_timeline_medley_app_instapp'])



id_list = []

# read page source to get friend's id.
soup = BeautifulSoup(driver.page_source, 'html5lib')
for d in soup.find_all("div", class_="fsl fwb fcb"):
    try:
        link = list(d.children)[0]['data-gt']
        data_link = json.loads(link)
        id_list.append(data_link['engagement']['eng_tid'].rstrip())
    except KeyError:
        continue

with open('friendlist.txt', 'w', encoding='utf-8') as f:
    for fbid in id_list:
        f.write(fbid + '\n')

driver.close()
