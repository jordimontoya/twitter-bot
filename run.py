from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import special keyboard keys
from driver import *
from config import *
import time

def setUpDriver():
    # Create a Firefox instance
    driver = webdriver.Firefox(executable_path=PATH_FIREFOX_DRIVER)
    # Navigate to this url
    driver.get(BASE_URL)
    return driver

def login(driver):
    # email input
    input = driver.find_element_by_xpath("//form/fieldset/div[1]/input[@type='text']")
    input.click()
    input.clear()
    input.send_keys(USERNAME)

    time.sleep(2)

    # pwd input
    inputPwd = driver.find_element_by_xpath("//form/fieldset/div[2]/input[@type='password']")
    inputPwd.click()
    inputPwd.clear()
    inputPwd.send_keys(PASSWORD)

    inputPwd.send_keys(Keys.RETURN)

def clickSearchFirstElement(driver, text):
    # search input
    searchInput = driver.find_element_by_id("search-query")
    searchInput.click()
    searchInput.clear()
    searchInput.send_keys(text)

    time.sleep(2)
    
    # click first item
    firstSearchedElement = driver.find_element_by_id("typeahead-item-1")
    firstSearchedElement.click()
    print(firstSearchedElement.text)

def sendTweet(driver, text):
    # fill textarea
    textarea = driver.find_element_by_id("tweet-box-home-timeline")
    textarea.click()
    textarea.send_keys(text)

    # send Tweet
    time.sleep(3)
    button = driver.find_element_by_xpath("//div[@id='timeline']//button[contains(@class,'tweet-action')]")
    print(button.text)
    button.click()

# SCRIT EXECUTION
driver = setUpDriver()

login(driver)
time.sleep(4)

#clickSearchFirstElement(driver, "#tesla")
sendTweet(driver, "My first automated tweet using #Python and #Selenium")
time.sleep(15)


#driver.quit()