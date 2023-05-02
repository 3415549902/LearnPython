# 打开文件 "File/1.txt"，采用只读模式，编码方式为 UTF-8
f = open("File/1.txt", 'r', encoding="UTF-8")

# 方式1：将整个文件内容读入到一个字符串中，然后使用字符串 count() 方法统计单词出现次数

# content = f.read()
# count = content.count("itheima")
# print(f"itheima出现:{count}")

# 方式2：逐行读取文件内容，去掉每行开头和结尾的空格符，然后使用空格符分割字符串成一个单词列表
# 再遍历单词列表，统计出现 "itheima" 单词的次数

count = 0
for i in f:
    i = i.strip(" ")    # 去掉字符串开头和结尾的空格符
    words = i.split(" ")   # 使用空格符分割字符串成一个单词列表
    for word in words:      # 遍历单词列表
        if word == "itheima":   # 如果单词是 "itheima"，次数加 1
            count += 1
print(f"itheima出现{count}次")

# 关闭文件
f.close()