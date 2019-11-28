import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Customer_Purchase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_customer(self):
        user = "shakebmajid"
        pwd = "Shakeb12"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # In this section I will create a new post and write an introduction onto it then delete the post through the admin
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a Selenium test")
        elem = driver.find_element_by_id("id_text")
        # The information on the post
        elem.send_keys("This is a test post to see if I can finish this assignment by the due date")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        # The post is saved and added to the main page
        # Now we will delete the post we made through the admin panel
        driver.get("http://127.0.0.1:8000/admin") # The get drive function will bring us to the admin webpage
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/a").click()
        time.sleep(5)
        # We will select change to delete the post we made, which will be the at the bottom
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td").click()
        # The script here will select the from the drop down box the delete function
        elem = driver.find_element_by_name("action")
        elem.send_keys("Delete selected products")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()  # Click Go
        time.sleep(5)
        # On the Are You Sure? page the script will click yes and the post will be deleted
        elem = driver.find_element_by_css_selector("input[type='submit']").click()  # Click Yes
        time.sleep(6)


def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()