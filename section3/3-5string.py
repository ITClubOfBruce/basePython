'''
    myStr = "welcome to beijing!"
'''
myStr = "welcome to beijing!"

# find
num = myStr.find("bei",0,len(myStr))
print(num)
print(myStr.find("o"))

print(myStr.find("a"))

# index
# print(myStr.index("a"))

# count
print(myStr.count("o"))

# replace
new_str = myStr.replace("o","O",2)
print(new_str)

#split,  列表
new_str = myStr.split(" ")
print(new_str)

# strip()   红楼梦.txt,求十二金钗出现的次数，并且排序输入

#partition  元组
new_str2 = myStr.partition(" ")
print(new_str2)

# join  
myStr1 = "aaa"
str1 = "_"
print(str1.join(myStr1))