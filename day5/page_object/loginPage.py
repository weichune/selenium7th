#这种框架的设计思想叫做page-object设计模式,是一种高级的框架设计思想
#这种思想主旨是把业务逻辑和代码技术分离
#测试用例的类,专门负责业务逻辑
#元素定位和操作交给网页对象类
#在pageObject这个类中,把每个网页看成一个类
#网页中的每个元素看成类中的一个属性
#针对这个元素的操作,看成类中的一个方法
#元素的信息\定位是名词性,可以看成属性(成员变量)
#元素的操作是动词性的,可以看出方法

#这个类主要做的就是把元素定位改一个易于理解的名字
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #为这个网页创建一个构造函数
    #在python中构造函数固定名字__init__()
    def __init__(self,driver):
        #因为setUp方法中已经创建了一个浏览器,所以这里不需要新建浏览器,直接用setUp建好的浏览器
        self.driver=driver
        self.url="http://localhost/index.php?m=user&c=public&a=login"

#声明一个变量,保存元素定位需要的两个参数
    #python的元组,类似于数组
    # 声明了一个数组username_input_loc,数组中有两个元素
    username_input_loc=(By.ID,"username")
    password_input_loc=(By.ID,"password")
    login_button_loc=(By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    #给参数设置默认值,如果调用方法时,传入一个新的用户名就使用新的
    #如果调用方法时不传参,那就使用默认值
    def input_username(self,username="weichune"):
        #这类中涉及到三个元素定位,因为元素定位不太稳定经常需要修改,
        # 所以应该把定位方式声明成类中的一个属性
        # self.driver.find_element(By.ID,"username").send_keys(username)
        #星号表示给find_element()这个方法传入的不是一个元组,而是元组中的每个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password="123qwe"):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

