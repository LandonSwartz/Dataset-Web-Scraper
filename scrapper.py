#12.25.2020
#First attempt at web scrapper

import selenium
from selenium import webdriver
import PIL

#Path to driver
DRIVER_PATH = r'C:\Users\Landon\Documents\Programming\Web_image_scrapper\chromedriver.exe'

#setting up web driver
wd = selenium.webdriver.Chrome(executable_path = DRIVER_PATH)

#goes to google.com
wd.get('https://google.com')

#entering search query
search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')

#quitting search driver
wd.quit()