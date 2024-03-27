"""
 Test case file with all required test cases to execute
"""
from SauceDemo_Functions import SauceDemoClass
import pytest



url = "https://www.saucedemo.com/"
#Creating Instance of SauceDemoClass to utilise its methods / functions
saucedemo = SauceDemoClass(url)

# Test case to navigate to URL
def test_navigate_url():
   testing_url = "https://www.saucedemo.com/"
   assert saucedemo.fetch_url() == testing_url
print("Landed on login page")

#Test Case for login
def test_login():
   saucedemo.login_user()

#Test Case to get title
def test_get_title():
   page_title = saucedemo.fetch_title()
   print(page_title)

#Test Case to get url
def test_get_url():
   page_url = saucedemo.fetch_url()
   print(page_url)

#Test Case to get webpage source and store in a text file
def test_scrap_and_store_webpage_details():
   scrap_details = saucedemo.fetch_webpage()
   file = open("Webpage_task_11.txt", "w")
   file.write(scrap_details)

#Test Case to quit / shutdown browser
def test_shutdown():
   saucedemo.shutdown()
