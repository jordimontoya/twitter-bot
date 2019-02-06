from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import special keyboard keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from driver import *
from config import *
from time import sleep

driver = None

def createUserAgent():
    ua = UserAgent(cache=False).chrome
    ua = UserAgent(cache=False)
    print(ua)
    return ua

def firefoxInstance():
    global driver

    # Create a Firefox instance
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", createUserAgent())
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=PATH_FIREFOX_DRIVER)
    driver.maximize_window()

def chromeInstance():
    global driver

    # Create a Chrome instance
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={createUserAgent()}')
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    #profile.set_preference("general.useragent.override", "whateveryouwant")
    driver = webdriver.Chrome(options=options, executable_path=PATH_CHROME_DRIVER) 

def setUpDriver():
    global driver
    
    if "FIREFOX" == BROWSER: 
        firefoxInstance()
    elif "CHROME" == BROWSER: 
        chromeInstance()
    
    # Navigate to this url
    driver.base_url = BASE_URL
    driver.get(BASE_URL)

def browserClose():
    driver.quit()

def login():
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

def sendTweet(text):
    # fill textarea
    textarea = driver.find_element_by_id("tweet-box-home-timeline")
    textarea.click()
    textarea.send_keys(text)

    sleep(DELAY)

    # send Tweet
    button = driver.find_element_by_xpath("//div[@id='timeline']//button[contains(@class,'tweet-action')]")
    button.click()

def deleteCreatedTweet():
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

def searchTwitter(text):
    # Twitter search input
    searchInput = driver.find_element_by_id("search-query")
    searchInput.click()
    searchInput.clear()
    searchInput.send_keys(text)
    searchInput.submit()

def dismissVisiblePopup():
    dissmissableButton = driver.find_element_by_css_selector(".Icon.Icon--close.dismiss")
    if dissmissableButton.is_displayed() and dissmissableButton.is_enabled():
        print(dissmissableButton)
        dissmissableButton.click()