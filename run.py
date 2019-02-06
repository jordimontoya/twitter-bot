from functions import *
from time import sleep

def run():
    setUpDriver()

    login()
    sleep(4)

    sendTweet("My first automated tweet using #Python and #Selenium")
    sleep(DELAY)

    dismissVisiblePopup()
    sleep(DELAY)

    deleteCreatedTweet()
    sleep(DELAY)

    searchTwitter("#tesla")
    sleep(4)

    browserClose()

# SCRIT EXECUTION
run()