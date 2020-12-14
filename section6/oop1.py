'''
    类的定义
'''
# class Car:
#     pass

# class Car(object):
#     # 方法
#     def getCarInfo(self):
#         print("这是一辆红色的smart")
#     # 移动
#     def move(self):
#         print("车在行驶~~~")
#     # 鸣笛
#     def toot(self):
#         print("车在鸣笛...嘟嘟..")


# BMW = Car()
# BMW.color = "红色"
# BMW.wheelNum = 4
# BMW.move()
# BMW.toot()
# print(BMW.color)
# print(BMW.wheelNum)



# audio = Car()




class Car:
    def __init__(self,color,wheelNum):
        self.color = color
        self.wheelNum = wheelNum
    def move(self):
        print("车在行驶~~~")


BMW = Car("red",4)
print(BMW.color)
print(BMW.wheelNum)
Audio = Car("blue",40)
print(Audio.color)
print(Audio.wheelNum)