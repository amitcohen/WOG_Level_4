from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

website = "http://127.0.0.1:30000/score"

# Open a webpage
def open_website():
    while True:
        driver.get(website)


open_website()


# Find an element and interact with it
element = driver.find_element_by_id('element_id')
element.click()
# test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
def test_scores_service():
    pass


# call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.
def main_function():
    pass