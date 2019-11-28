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
        # After the login section, you will be brought to the store page
        # For this test we will create a customer then delete the customer. First we need to select customer
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(3)
        # You will be brought to the customer page. Here we will click the add customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a").click()
        time.sleep(3)
        # After clicking the add customer button, you need to fill out information about the customer
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Shakeb Majid")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("UNOmaha College of IS&T")
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Student")
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI Room 158")
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("123456")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("1110 S 67th St.")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("NE")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68135")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("shakebmajid@unomaha.edu")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("(402) 555-2222")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        # After information for the customer is filled, the sciprts will click the edit button to edit some information for the customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a").click()
        time.sleep(2)
        # Here we will edit the customer's name but clearing the field and adding a new name
        elem = driver.find_element_by_id("id_cust_name").clear()
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Shakeb Majid Jabarkhail")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        # After editing the customer information and saving it, the scripts will hit the summary button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[14]/a").click()
        time.sleep(2)
        # After that you are brought to the summary page and there will be no information here because the customer didn't add and services or products
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(2)
        # After viewing the summary page, the script will click the customer banner at the top and be bourght back to the customer page
        # For curtain reasons, we will delete the customer from the admin page
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(2)
        # On the admin page the script will click on the customer change button
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a").click()
        time.sleep(2)
        # Here we will select the customer we just created and delete the customer's information
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[3]/td[1]/input").click()
        elem = driver.find_element_by_name("action")
        elem.send_keys("Delete selected products")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()  # Click Go
        time.sleep(2)
        # On the Are You Sure? page the script will click yes and delete the customer from the site
        elem = driver.find_element_by_css_selector("input[type='submit']").click()  # Click Yes
        time.sleep(2)
        # Here the script will delete the customer information we just created
        time.sleep(2)




def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()