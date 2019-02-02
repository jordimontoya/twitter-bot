from functions import *
from time import sleep

def run():
    driver = setUpDriver()

    login(driver)
    sleep(4)

    sendTweet(driver, "My first automated tweet using #Python and #Selenium")
    sleep(DELAY)

    deleteCreatedTweet(driver)
    sleep(DELAY)

    searchTwitter(driver, "#tesla")
    sleep(4)
    driver.quit()

# SCRIT EXECUTION
run()