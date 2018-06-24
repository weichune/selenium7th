import csv

#每个测试用例对应着不同的csv文件
# 每条测试用例都会打开一个csv文件,所以每次也应该关闭该文件

class CsvFileManager3:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file=open(path,'r')
        try:
            #通过csv代码库读取打开的csv文件,获取到文件中的数据
            data_table=csv.reader(file)
            #表格中有几行数据就循环几次
            for item in data_table:
                print(item)
            # 方法最后应该添加close方法
        finally: #不论是否报错都会执行以下代码
            file.close()

#如果想测试下这个方法:
if __name__ == '__main__':
    # csvr=CsvFileManager2()
    # csvr.read()
    #如果在方法上面加上classmethod,表示这个方法可以直接被调用,就不需要先实例化对象后才能调用
    CsvFileManager3.read()