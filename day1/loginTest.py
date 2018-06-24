#这个文件用来实现一个登录功能的自动化操作
#1.打开浏览器
import time
from selenium import webdriver
#从 谷歌公司的一个项目名导入网络驱动,来操作浏览器
driver=webdriver.Ie()
#设置隐式等待:一旦找到页面元素,马上执行后面的语句
#如果超过20s仍然找不到页面元素,程序会报超市错误
driver.implicitly_wait(20)
#2.打开海盗商城网站
driver.get("http://localhost/")
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名密码
driver.find_element_by_id("username").send_keys("weichune")
driver.find_element_by_id("password").send_keys("123qwe")
#5.点击登录按钮
#所有调用方法都会有提示信息,没有提示信息就说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功
#Alt+Enter导包快捷键
#time.sleep()这个方法提供了一种固定的时间等待,点击登录按钮,等5s后,再检查用户名是否正常显示
#弊端是因为网络延迟,不知是每次等1s合适还是5s合适
#解决办法:智能等待
#time.sleep(5)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#通过if语句判断页面显示的文本和预期的文本是否一致
if username_text=="您好 weichune":
    print("测试执行通过")
else:
    print("测试执行失败")
#selenium主要做回归测试,所以测试脚本都是pass的,只有开发做了代码变更,测试用例才有可能失败
#一般工作中不用if...else语句做判断,后面详细讨论
#7.点击"进入商城购物"按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#xpath有一个缺点,定位元素的可读性比较差
driver.find_element_by_link_text("进入商城购物").click()
#在商城主页输入搜索条件iphone
time.sleep(2)
driver.find_element_by_name("keyword").send_keys("iphone")
#点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#点击第一个商品
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
#窗口切换
driver.close() #关闭原来的窗口-selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])
#点击加入购物车
time.sleep(5)

driver.find_element_by_id("joinCarButton").click()