#1.要想读取csv文件,首先要导入csv代码库
#csv不用下载,是python内置的代码库
#如果要读取Excel需要下载相应的代码库:xlrd
#下载方式:1.通过命令下载 在dos窗口中输入pip install -U xlrd
#selenium的离线包,也可通过命令行在线安装pip install -U xlrd或pip3 install xlrd
#-U是升级到最新版的意思
#pip是python语言最常用的项目管理工具,和java代码中的maven类似
#如果python2和python3同时安装,可能需要把pip改成pip3
#         2.点击File-Settings-project下面的interpreter-点击+号,搜索需要的代码库并可直接安装
import csv


#2.指定要读取的文件路径
path='C:\\Users\\51Testing\\PycharmProjects\\selenium7th\\data\\test_data.csv'
# 因为字符串中包含转义字符\t等
#  1.每个反斜线前面加一个反斜线
#  2.把每个反斜线改成正斜线
# 相比,第二种方法更好一点,因为java,python都是跨平台的语言
# 在字符串中两个反斜线会自动根据转义字符的规则转成一个反斜线
# 在windows操作系统中,用反斜线表示目录结构
# 但是linux操作系统中,只有正斜线/才能表示目录
# 如果用双反斜线,代码就不能跨平台
#  3.在字符串外面加上r,认为中间所有代码都不存在转义字符

#3.打开路径所对应的文件
file=open(path,'r')

#4.读取文件的内容
#reader()方法是专门用来读取文件的
data_table=csv.reader(file)
#打印data_table中的每一行数据,循环for-each语句
#item代表每一行,每循环一次,item就代表最新的一行数据
#data_table表示整个文件中的所有数据行
for item in data_table:
    print(item)

#很多的测试用例可能都需要从excel中读取数据,所有我们应该对这些代码做封装
#建一个文件叫scvFileManager2,把以上代码封装到一个方法中
#并且再建一个文件来读取封装好的方法


