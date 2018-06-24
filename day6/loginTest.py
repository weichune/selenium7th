from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from day5.myTestCase import MyTestCase

driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element(By.ID, "username").send_keys("weichune")
driver.find_element(By.ID, "password").send_keys("123qwe")
driver.find_element(By.CLASS_NAME, "login_btn").click()
#中间有个跳转页面,不能直接点击进入商城购物
#解决方法:time.sleep(),隐式等待,显式等待
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
#这句显示等待的代码,相当于time.sleep(20)的优化版代码

driver.find_element_by_link_text("进入商城购物").click()
