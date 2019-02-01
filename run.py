from functions import *
import time

def run():
    driver = setUpDriver()

    login(driver)
    time.sleep(4)

    sendTweet(driver, "My first automated tweet using #Python and #Selenium")
    time.sleep(6)

    deleteCreatedTweet(driver)
    time.sleep(5)

    #clickSearchFirstElement(driver, "#tesla")
    time.sleep(15)
    driver.quit()

# SCRIT EXECUTION
run()