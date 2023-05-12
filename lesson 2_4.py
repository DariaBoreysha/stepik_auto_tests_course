from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'



try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("Ana")

    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Kov")

    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("2@as.com")

    current_file = os.path.abspath(os.path.dirname(__file__))
    path_file = os.path.join(current_file, 'file\lesson2_4.txt')
    print(path_file)
    choose = browser.find_element_by_xpath('//input[@id="file"]')
    choose.send_keys(path_file)

    browser.find_element_by_xpath('//button').click()

finally:
    time.sleep(8)
    browser.quit()    



