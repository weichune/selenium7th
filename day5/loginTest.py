import unittest

from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这个类不需要再写setUp和tearDown方法,只需要写测试用例方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.ID,"username").send_keys("weichune")
        driver.find_element(By.ID,"password").send_keys("123qwe")
        driver.find_element(By.CLASS_NAME,"login_btn").click()
        check_tip=driver.find_element(By.LINK_TEXT,"您好 weichune").text
        self.assertEqual("您好 weichune",check_tip)

if __name__ == '__main__':
    unittest.main()
