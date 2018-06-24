import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#1.登录海盗商城
from day2.loginTest import Login

#我们已经创建好一个空白的浏览器,后续的所有操作都应该在这个浏览器上执行
driver=webdriver.Chrome()
#每次创建浏览器时implicitly_wait固定写一次,对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要监测页面的加载时间,什么时候页面加载完,什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存,pycharm会自动帮我们释放内存
#代码运行完,检测到Login()这个对象不再被使用,系统自动释放内存
#把driver浏览器传入到登录方法中,让登录方法和下面的点击账号设置使用同一个浏览器

Login().loginWithDefaultUser(driver)
# driver=webdriver.Chrome()
# driver.get("http://localhost/")
# driver.find_element_by_link_text("登录").click()
# driver.close()
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_id("username").send_keys("weichune")
# driver.find_element_by_id("password").send_keys("123qwe")
# driver.find_element_by_class_name("login_btn ").click()
#2.点击"账号设置"

driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/ul/li[1]/a").click()
#3.点击"个人资料"
#partial_link_text可以使用链接的一部分进行元素定位
#当链接文本过长时,推荐使用partial_link_text
driver.find_element_by_partial_link_text("个人资料").click()
#xpath方法比较通用,可以用工具自动生成,但是不推荐使用,因为可读性差
#driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
#4.修改真实姓名
#如果输入框中原本有内容,先调用clear()方法清空原有值
#一个良好的编程习惯是每次sendKeys之前都应该先做clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("魏春娥")
#5.修改性别--3种方法
#要通过value属性定位有两种方法:xpath和css_selector
#通过css_selector定位元素,只需要在唯一属性的两边加上中括号
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中,//表示采用相对路径定位元素,一般通过元素的特殊属性查找
# /表示绝对路径,一般通过元素的位置,层级关系查找元素,一般都是从/html开始定位元素
#绝对路径比较长,涉及到的节点多,代码的稳定性比较差,当页面布局发生变化,受到影响的可能性大
#相对路径,查询速度比较慢,可能要遍历更多的节点
#工作中推荐用css_selector,因为查询速度比xpath快
#xpath在某些浏览器上支持不太好
# css_selector所有前端开发都会用,易于交流

# *星号表示任意节点  [@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()

#javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
#通过下标选取其中的第N个元素,也可以用于定位
driver.find_elements_by_id("xb")[2].click()

#6.修改生日
#一下一下点年月日可以实现,但是稳定性差,容易出错,并且很难修改日期
#右键检查,日历控件其实是个文本输入框,但是有readonly属性,不能输入
#写一个javascript脚本,删除readonly属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1986-12-28")

#7.修改qq
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("277869323")
#8.点击确定
time.sleep(3)
driver.switch_to.alert.accept()