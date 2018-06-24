import unittest

import time
from selenium import webdriver


#继承unittest.TestCase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    #重写setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    #编写一个测试用例方法(以test开头的方法)
    def test_register(self):
        for row in CsvFileManager4().read("test_data.csv"):

            driver=self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            #find_element_by_name等于find_element(By.NAME,"name")
            driver.find_element(By.NAME,"username").send_keys(row[0])
            driver.find_element(By.NAME,"password").send_keys(row[1])
            driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
            driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME,"email").send_keys(row[4])
            # 在for循环中执行测试用例,虽然解决批量执行的问题

            #输入完邮箱后按tab键,检查提示信息是否都是"通过信息验证"
            #如果页面上提示的信息是"通过信息验证",那么测试通过,否则测试失败
            check_tip=driver.find_element(By.CSS_SELECTOR,"form > ul > li:nth-child(1) > div > span").text
            print(check_tip)
            # check_tip是执行用例时从网页上抓取的信息
            #"通过信息验证"是期望结果
            # if check_tip=="通过信息验证":
            #     print("测试通过")
            # else:
            #     print("测试失败")
            #断言的写法
            self.assertEqual("通过信息验证",check_tip)
            #不应该用for循环的方式执行不同的测试数据
            #因为在方法中写了for循环虽然执行了多次,但是unittest仍然认为它是一条测试用例,一旦断言失败,就会终止            这条测试用例,所以应该采用ddt框架实现数据驱动
            

            driver.find_element(By.CLASS_NAME,"reg_btn").click()



if __name__ == '__main__':
    unittest.main()