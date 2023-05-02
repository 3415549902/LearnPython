# 文件的写入操作

# 案例演示
'''
f = open("python.txt","w")
f.write("hello world")
f.flush()
'''
#注意：
#直接调用wirte，并未真正写入文件，而是积攒到程序的内存中，称之为缓冲区
#调用flush函数是才会真正写入
#是为了避免频繁的操作硬盘，导致效率下降
