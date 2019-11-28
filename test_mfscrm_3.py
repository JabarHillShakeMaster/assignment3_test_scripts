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
        # Here in this script the code will make a products, update information, and delete the products
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        time.sleep(3)
        # Here the script will select the add product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a").click()
        time.sleep(3)
        # Here the script will fill out information about the product being ordered
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Barbara York")
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Pepsi")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("24 pack of soda cans")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("1")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("8.75")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(3)
        # Now the script will edit a service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[7]/td[7]/a").click()
        # The category name will be changed to Food Prep/Cater
        elem = driver.find_element_by_id("id_product").clear()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Coke-Colo")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click() # Click update
        time.sleep(3)
        # Now the script will delete the product from admin page
        driver.get("http://127.0.0.1:8000/admin")
        # On the admin page, select product change
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a").click()
        # On the edit selection page, the service will be selected and deleted
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td[1]/input").click()
        elem = driver.find_element_by_name("action")
        elem.send_keys("Delete selected products")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()  # Click Go
        time.sleep(3)
        # On the Are You Sure? page the script will click yes and delete the customer from the site
        elem = driver.find_element_by_css_selector("input[type='submit']").click()  # Click Yes
        time.sleep(3)
        # Here the script will delete the customer information we just created
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()