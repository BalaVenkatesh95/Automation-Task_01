"""
File contains automation methods / functions which can be
used in test case file
"""
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class SauceDemoClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False


   #  fetches the title of the web application
   def fetch_title(self):
       if self.initiation_function() == True:
           return self.driver.title
       else:
           return False


   # fetches the URL of the web application
   def fetch_url(self):
       if self.initiation_function():
           return self.driver.current_url
       else:
           return False


   #  fetches the entire source-code
   def fetch_webpage(self):
       if self.initiation_function():
           return self.driver.page_source
       else:
           return False

   # Emulates login process of user
   def login_user(self):


       if self.initiation_function():
           username_field = self.driver.find_element('id', 'user-name')
           password_field = self.driver.find_element('id', 'password')
           login_button = self.driver.find_element('id', 'login-button')
           username_field.send_keys("standard_user")
           password_field.send_keys("secret_sauce")
           login_button.click()
           time.sleep(5)
       else:
           return False


