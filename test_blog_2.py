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
        # In this section the test script will add information onto the post added in the previous script
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h2/a").click()
        time.sleep(5)
        # You are brought to the post review page. Here the pencil icon will be clicked
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a/span").click()
        time.sleep(5)
        # I will add some content on the text field. First, find the text field with the text ID
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("\n Here is some new content onto this post.")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(2)
        # Now the post has been changes with new content on the post

def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()