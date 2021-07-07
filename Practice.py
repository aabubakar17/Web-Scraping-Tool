from selenium import webdriver
#allows you to use the enter and escape keys to search thing auto.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# -*- coding: utf-8 -*-

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.footasylum.com/")
#print(driver.title)
#search = driver.find_element_by_id("search-anime")
#search.send_keys("Attack on Titan")
#search.send_keys(Keys.RETURN)
link = driver.find_element_by_link_text("Shop Men's")
link.click()

#Waits for 10 seconds for the page to laod up, until it find the correct elements.
try:
    #element = WebDriverWait(driver, 10).until(
      #EC.presence_of_element_located((By.link_text , "Shop Men's"))
    #)
    #element.click()

    element = WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.link_text , "Tech 2.0 T-Shirt"))
    )
    element.click()

except:
    driver.quit()


import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
