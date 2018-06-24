#这个文件是用来批量执行unittest测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unittest,因为批量执行测试用例的功能是unittest提供的
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    #1.通过path打开新生成的测试报告文件
    #html格式不是文本格式,需要指定以二进制的方式打开
    file=open(path,'rb')
    #2.读取文件的内容作为邮件正文
    msg=file.read()
    #3.把读取出来的内容转换成MIMEText的格式
    #邮件类型一般分为三种:纯文本plain,html,富文本
    mime=MIMEText(msg, _subtype='html', _charset="utf-8")
    #4.除了正文,还要设置主题,发件人,收件人
    mime['Subject']='自动化测试报告'
    #发件人需要登录密码,这里的密码不是登录密码,而是客户端授权码
    #第三方登录不能直接用密码,必须用授权码
    mime['From']='w.c.e.1228@163.com'
    mime['To']='w.c.e.1228@163.com'

    #实现SMTP()构造方法
    smtp=smtplib.SMTP()
    #连接126邮箱
    smtp.connect("smtp.163.com")
    #登录126邮箱
    smtp.login("w.c.e.1228@163.com","5863453wce")
    #发送邮件
    smtp.send_message(mime,from_addr="w.c.e.1228@163.com",to_addrs='w.c.e.1228@163.com')
    #退出
    smtp.quit()




if __name__ == '__main__':
    #2.要想批量执行,首先要明确要执行哪些测试用例
    #只能执行继承了unittest.TestCase的类
    #比如执行这个项目中所有的unittest的测试用例
    #defaultTestLoader是默认的测试用例加载器,可以用来找所有测试用例
    suite=unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #3.找到测试用例后,执行这些测试用例
    #TextTestRunner()文本的测试用例运行器
    #unittest.TextTestRunner().run(suite)
    #4.生成测试报告
    #HTMLTestRunner类似于TextTestRunner,都是批量执行测试用例
    #区别在于,他们执行完所有测试用例的输出结果
    #一个是Text,另一个是HTML
    #Text会被打印到控制台中,HTML会单独生成一个文件
    #相比于Text,HTML结构更清晰
    #所有二者选其一,用HTMLTestRunner代替unittest原生的TextTestRunner
    #需要把生成的html格式的测试报告保存到一个固定位置,方便查看
    #在项目根节点下,创建一个文件夹叫report,以后所有的测试报告都保存在report下
    #5.定义测试报告的保存目录
    base_path=os.path.dirname(__file__)
    path=base_path+'/report/test_report.html'
    #6.创建测试文件
    file=open(path,'wb')

    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境:Server 2008;浏览器:'Chrome'").run(suite)

    #7.把测试报告作为邮件发送
    #前提条件:准备两个邮箱
    #版本控制的前提条件,申请一个git账号

    send_mail(path)