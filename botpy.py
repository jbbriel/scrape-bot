import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from USCities import popularCities

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.abspath('/Users/ryniguez/Selenium Browsers')
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chromeOptions, executable_path=DRIVER_BIN)
baseURL = "http://www.google.com"
driver.get(baseURL)

# grabs the current browser tab window id
current_window = driver.current_window_handle

class scrape_advenfunture_flights:

    # creating this method makes this bit of code reusable
    def __init__(self, numOfPlaces=None):
        self.places = popularCities().inUS(numOfPlaces)

    def wait_for_browser(self):
        browserReady = driver.execute_script('return document.readyState')
        while browserReady not in 'complete':
            browserReady = driver.execute_script('return document.readyState')
            print(browserReady)


    def siteTraversal(self):

        for Arilines in self.places:
            self.wait_for_browser()
            elem = driver.find_element_by_name('destination_name')
            time.sleep(2)
            elem.clear()
            elem.click()
            self.wait_for_browser()
            elem.send_keys(Arilines)
            time.sleep(1)
            elem.send_keys(Keys.DOWN)
            time.sleep(1)
            elem.send_keys(Keys.ENTER)
            time.sleep(1)

            elem.submit()
            self.wait_for_browser()

            # Get new window/tab ID
            second_window = [window for window in driver.window_handles if window != current_window][0]

            # Switch to new window/ second tab
            driver.switch_to.window(second_window)
            url = driver.current_url
            print(url)
            time.sleep(2)
            # Save's a screen shot of second Window

            #driver.save_screenshot('city_' + str(Arilines) +'flights.png')

            self.wait_for_browser()
            time.sleep(5)
            # Click Book Button on second Tab
            driver.execute_script("document.getElementsByClassName('ticket-action-button-deeplink ticket-action-button-deeplink--')[1].click()")
            self.wait_for_browser()

            # Switch to new window/ third tab
            third_window = [window for window in driver.window_handles if window != current_window and window != second_window ][0]

            driver.switch_to.window(third_window)
            self.wait_for_browser()
            # Save's a screen shot of second Window
            time.sleep(3)
            driver.save_screenshot('city_' + str(Arilines) + 'book_clicked.png')
            time.sleep(3)

            driver.close()
            # Switch to new window/ second tab
            driver.switch_to.window(second_window)
            time.sleep(1)
            driver.close()
            # Switch to new window/ first tab
            driver.switch_to.window(current_window)
            time.sleep(1)

        driver.delete_all_cookies()
        driver.close()
        driver.quit()

scrape_advenfunture_flights(30).siteTraversal()