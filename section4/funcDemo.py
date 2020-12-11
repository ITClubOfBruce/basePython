'''
    接收用户输入的月日，判断用户的星座
    ("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
    ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''
zodiac = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

month = int(input("请输入您的出生月份:"))
day = int(input("请输入您的出生日期:"))

# for循环解决
# index = 0
# for zodiac_day in zodiac_days:
#     if month==12 and day>22:
#         index = 0
#     elif (month,day) > zodiac_day:
#         index += 1

# print(zodiac[index])


# while 循环解决
# n = 0
# while (month,day) > zodiac_days[n]:
#     if month==12 and day>22:
#         break
#     n += 1

# print(zodiac[n])


# 使用lambda表达式
def add(arg1,arg2):
    return arg1+arg2

lambda arg1,arg2:arg1+arg2

sum = lambda arg1, arg2: arg1 + arg2

def judezodiac(month,day):
    n = 0
    while (month,day) > zodiac_days[n]:
        if month==12 and day>22:
            break
        n += 1
    return zodiac[n]

# 使用内置函数 filter
result = filter(lambda x:x<(month,day),zodiac_days)
print(zodiac[len(list(result))])

stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]

stus.sort(key=lambda x:x["age"])
print(stus)