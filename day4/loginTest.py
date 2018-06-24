#用unittest写一个后台登录的测试用例
#1.导包
import unittest
#2.建类并继承父类
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #3.重写setUp和tearDown方法
    @classmethod
    def setUpClass(self):
        #做web自动化测试,所有测试用例都要打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化的代码,要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()
    @classmethod
    def tearDownClass(self):
        #为了保证可以看清测试结果,可以在tearDown方法中加一个30s的延时等待
        time.sleep(30)
        #每次执行完测试用例,应该把打开的浏览器关闭,释放内存,清除cookie和缓存,为下次测试用例做准备
        #这里调用的driver是声明在setUp方法中的局部变量
        #局部变量不允许被其他方法访问
        #所以应该把setUp方法中声明的driver改成一个全局变量
        #因为self表示类本身,所以只要在变量前加上self.就表示这个变量是属于类的
        self.driver.quit()

    def test_login(self):
        #因为每次使用driver变量时都需要前面加一个self.
        #为了简化代码,可以把成员变量self.driver赋值给局部变量driver
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")

        #有些常用的键也可以用转义字符代替,其中\t表示Tab键,\n表示Enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_adding(self):
        driver=self.driver
        #如果第二个方法重新打开一个浏览器,登录就无效了
        #可以将setUp改成setUpClass,tearDown改成tearDownClass
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        # 除了用name属性切换frame,也可通过8种元素定位方法定位元素,然后切换
        iframe=driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        # driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("name").send_keys("照相机")
        #变量名文件夹的起名规则:数字,大小写字母,下划线,一般要求以字母开头
        #如果id是纯数字,用#的方式不能定位,可以用[]的方式定位,所有的属性都可以用[]定位
        driver.find_element_by_xpath("//*[@id=\"1\"]").click()
        driver.find_element_by_link_text("手机通讯").click()
        driver.find_element_by_link_text("手机").click()
        link = driver.find_element_by_link_text("苹果 (Apple)")
        actions = ActionChains(driver)
        actions.move_to_element(link).double_click().perform()
        options = driver.find_element_by_name("brand_id")
        select1 = Select(options)
        select1.select_by_value("1")
        # 7.点击提交按钮
        driver.find_element_by_class_name("button_search").click()

if __name__ == '__main__':
    unittest.main()

