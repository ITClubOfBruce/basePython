'''
    接收用户输入的年份，判断用户的生肖
    鼠牛虎兔龙蛇马羊猴鸡狗猪
'''
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
str_year = input("请输入您的出生年份:")
int_year = int(str_year)

zodiac_num = int_year%12

print("您的生肖是%s"%chinese_zodiac[zodiac_num])


