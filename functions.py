from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import special keyboard keys
from driver import *
from config import *
from time import sleep

def setUpDriver():
    # Create a Firefox instance
    driver = webdriver.Firefox(executable_path=PATH_FIREFOX_DRIVER)
    # Navigate to this url
    driver.base_url = BASE_URL
    driver.get(BASE_URL)
    return driver

def login(driver):
    # email input
    input = driver.find_element_by_class_name("js-username-field")
    input.click()
    input.clear()
    input.send_keys(USERNAME)

    sleep(DELAY)

    # pwd input
    inputPwd = driver.find_element_by_class_name("js-password-field")
    inputPwd.click()
    inputPwd.clear()
    inputPwd.send_keys(PASSWORD)

    inputPwd.send_keys(Keys.RETURN)

def sendTweet(driver, text):
    # fill textarea
    textarea = driver.find_element_by_id("tweet-box-home-timeline")
    textarea.click()
    textarea.send_keys(text)

    sleep(DELAY)

    # send Tweet
    button = driver.find_element_by_xpath("//div[@id='timeline']//button[contains(@class,'tweet-action')]")
    button.click()

def deleteCreatedTweet(driver):
    # click dropdown button
    button = driver.find_element_by_xpath("//div[@id='timeline']//button[contains(@class,'ProfileTweet-actionButton')]")
    button.click()

    sleep(DELAY)

    # click delete button
    delButton = driver.find_element_by_xpath("//div[@id='timeline']//li[contains(@class,'js-actionDelete')]")
    if delButton.is_displayed():
        delButton.click()

    sleep(DELAY)

    # click pop-up's delete button
    delButton = driver.find_element_by_css_selector(".EdgeButton--danger.delete-action")
    if delButton.is_displayed():
        delButton.click()

def searchTwitter(driver, text):
    # Twitter search input
    searchInput = driver.find_element_by_id("search-query")
    searchInput.click()
    searchInput.clear()
    searchInput.send_keys(text)
    searchInput.submit()