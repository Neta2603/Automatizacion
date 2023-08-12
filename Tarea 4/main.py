from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import HtmlTestRunner
import os


class TestSelenium(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://plataformavirtual.itla.edu.do/login/index.php')

        # Ingresa las credenciales
        user = driver.find_element(By.XPATH, "(//input[contains(@name,'username')])")
        user.send_keys("20220437")

        passw = driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        passw.send_keys("0437#Itla")

        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        time.sleep(5)

        self.take_screenshot('test.png')


    def tearDown(self):
        self.driver.quit()


    def take_screenshot(self, filename):
        screenshot_dir = 'screenshots'

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report'))

