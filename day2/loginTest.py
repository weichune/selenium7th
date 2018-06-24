#如何把这个文件封装成一个登录方法
#python中类的关键字是class,方法也有一个关键字def,是difine的缩写,表示定义方法

#1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#python中使用冒号代替java中的大括号
#在冒号后面敲回车自动缩进四个空格
class Login:
    #def是方法的关键字,loginWithDefaultUser是方法名
    #方法后面必须有括号,用来声明参数,默认有一个参数(self),self表示类本身,类似于java中的this
    #方法声明后面也有冒号,方法下面所有语句都必须缩进四个空格
    #登录功能的代码都被封装到loginWithDefaultUser()方法中了
    #以后只要写一句话,调用这个方法,就可实现登录
    def loginWithDefaultUser(self,driver):
        #driver=webdriver.Chrome()
        #2.打开海盗网站
        driver.get("http://localhost")
        #3.删除登录链接的target属性
        #python中字符串可以用单引号也可以双引号,如果字符串本身包含双引号,两边用单引号
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")'
                              '[0].childNodes[1].removeAttribute("target")')
        #4.点击登录按钮,跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        #5.输入用户名
        driver.find_element_by_id("username").send_keys("weichune")
        #6.输入密码
        #ActionChains是一组动作和行为的意思
        #实例化一个ActionChains这个类的对象,对象用来执行一组动作和行为
        #和java的区别:python语言实例化不需要声明变量的类型,实例化去掉了new关键字
        actions=ActionChains(driver)
        #如果想使用键盘上的任意按键,去Keys类中找
        #所有Actions中的方法都必须以perform()结尾才会被执行
        actions.send_keys(Keys.TAB).send_keys("123qwe").perform()
        #7.点击登录按钮
        #actions.send_keys(Keys.ENTER).perform()
        #如果不支持回车键登录,可以直接定位点击登录按钮
        #如果很难定位登录按钮,还可以用submit()方法,用于提交表单
        #开发通过form表单把这些信息同时提交到服务器
        #可以用任何一个元素执行submit()方法,来提交表单中的所有数据
        driver.find_element_by_id("username").submit()


