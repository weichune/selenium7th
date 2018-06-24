#实现注册功能的自动化
from selenium import webdriver
#打开浏览器
driver=webdriver.Chrome()
#打开商城首页
driver.get("http://localhost/")
#打开注册页
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("weichune1")
driver.find_element_by_name("password").send_keys("123qwe")
driver.find_element_by_name("userpassword2").send_keys("123qwe")
driver.find_element_by_name("mobile_phone").send_keys("18613802222")
driver.find_element_by_name("email").send_keys("www@126.com")
driver.find_element_by_class_name("reg_btn").click()
