File = open("Files/Files.txt", 'r', encoding='UTF-8')  # File是Open的对象
# encoding 不是第三位故用关键字

# read 方法 文件对象.read(num)
# num 表示从文件读取的数据长度(单位字节） 若未传入num则全部读取
# !!! 两个read()方法 会继续读取文件(不会从新读取)

# print(File.read())


print("-----------------------------------------------------------------------------------") # 分割线


#readlines()方法
# 按照行的方式把整个文件中的内容进行一次性读写，返回列表，每一行为一个元素

print(File.readlines())


File.close()