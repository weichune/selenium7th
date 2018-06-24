import csv

#把读取文件的代码封装成一个方法
class CsvFileManager2:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file=open(path,'r')
        #通过csv代码库读取打开的csv文件,获取到文件中的数据
        data_table=csv.reader(file)
        #表格中有几行数据就循环几次
        for item in data_table:
            print(item)

#如果想测试下这个方法:
if __name__ == '__main__':
    # csvr=CsvFileManager2()
    # csvr.read()
    #如果在方法上面加上classmethod,表示这个方法可以直接被调用,就不需要先实例化对象后才能调用
    CsvFileManager2.read()