from selenium import webdriver
#1.打开主页
driver=webdriver.Chrome()
driver.get("http://localhost/")
#2.点击登录按钮
driver.find_element_by_link_text("登录").click()
#3.输入iphone
driver.find_element_by_name("keyword").send_keys("iphone")
#如果想在新的标签页上操作页面元素,需要窗口切换
#driver.switch_to.window(第二个窗口名字)
#selenium提供了浏览器中所有窗口的名字
#driver.window_handles可以理解为一个数组
#取组数的第二个元素
#所以第二个窗口名字 driver.window_handles[1]
#窗口切换:
driver.switch_to.window(driver.window_handles[1])
#再试一下iphone会被输入到哪个搜索框中
driver.find_element_by_name("keyword").send_keys("iphone")

#[1]表示第二个元素,[-1]表示最后一个元素

#在python中,元组和列表可以正着数,也可以负着数,倒数第一个-1,倒数第二个-2
#所以上边的代码可以改成:
driver.switch_to.window(driver.window_handles[-1])