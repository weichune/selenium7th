
from selenium import webdriver
#1.登录海盗商城后台
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/admin.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("username").submit()

#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
#操作子框架中的元素,首先要进行frame切换
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphoneX")
#5.选择商品分类(双击或点击选择当前分类)
driver.find_element_by_xpath("//*[@id=\"1\"]").click()
driver.find_element_by_link_text("手机通讯").click()
driver.find_element_by_link_text("手机").click()
link=driver.find_element_by_link_text("苹果 (Apple)")
actions=ActionChains(driver)
actions.move_to_element(link).double_click().perform()
#driver.find_element_by_link_text("苹果 ").click()
#driver.find_element_by_link_text("选择当前分类").click()
#6.下拉框中选择商品品牌
options=driver.find_element_by_name("brand_id")
select1=Select(options)
select1.select_by_value("1")
#7.点击提交按钮
driver.find_element_by_class_name("button_search").click()



