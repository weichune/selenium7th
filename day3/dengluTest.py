import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.implicitly_wait(20)
#点击登录链接
#用javascript的方法找登录链接
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium找登录链接
#driver.find_element_by_link_text("登录")
#selenium不支持removeAttribute的javaxcript方法
#但是selenium找到的链接和javascript找到的是同一个元素
login_link=driver.find_element_by_link_text("登录")
#把selenium找到的这个元素,传入到javascript方法里,代替原来的javascript定位元素
#arguments参数数组,[0]表示第一个参数,指的就是js后面的login_link
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#用户名
driver.find_element_by_id("username").send_keys("weichune")
#密码
driver.find_element_by_id("password").send_keys("123qwe")
#提交
driver.find_element_by_id("username").submit()
#回到商城首页
driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/span/a").click()
#输入iphone搜索
driver.find_element_by_name("keyword").send_keys("iphone")
#提交
driver.find_element_by_name("keyword").submit()

#点击第一个商品
product_link_xpath="/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a"
#关闭新打开的页面,img没有target属性,所以复制他的父节点a的xpath
iphone=driver.find_element_by_xpath(product_link_xpath)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#加入购物车
driver.find_element_by_id("joinCarButton").click()
#去购物车结算
driver.find_element_by_class_name("shopCar_T_span3 ").click()
#结算
#css_selector定位时在class前面加一个小数点就可以定位
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
#添加收货人
driver.find_element_by_class_name("add-address").click()
#收件人
driver.find_element_by_name("address[address_name]").send_keys("weichune")
#联系方式
driver.find_element_by_name("address[mobile]").send_keys("18613802587")
#地址
dropdown1=driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素,对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类Select
#dropdown1的类型是一个普通的网页 元素,下面这句代码是把普通的网页元素转换成下拉框的类型
print(type(dropdown1)) #WebElement类型
#WebElement这个类中只有click和send_keys这样的方法,没有选择下拉选项的方法
select1=Select(dropdown1)
print(type(select1)) #Select类型
#转换成select类型之后,网页元素还是那个元素,但是Select类中有选择下拉选项的方法
select1.select_by_value("110000") #通过选项值来定位
time.sleep(2)
select1.select_by_visible_text("甘肃省") #也可以通过选项的文本信息来定位
#选择市区时因为是动态id,所以不能通过id定位
#因为class不唯一所以也不能用class定位
#但是我们可以用find_elements的方法先找到页面上所有class=add-new-area-select的元素
#然后再通过下标的方式选择第n个页面元素
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
select2=Select(dropdown2)
select2.select_by_visible_text("兰州市")
#select标签因为只有三个,可以用tag_name定位
#tag_name大多数情况都能找到一堆元素,所以find_element_by_tag_name()很少用,但是find_elements_by_tag_name
dropdown3=driver.find_elements_by_tag_name("select")[2]
#dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]
select3=Select(dropdown3)
select3.select_by_visible_text("城关区")
driver.find_element_by_name("address[address]").send_keys("城关区北沙滩")
driver.find_element_by_name("address[zipcode]").send_keys("730206")
driver.find_element_by_class_name("aui_state_highlight").click()





