'''
    id()
    __str__
    private
    protected
    public
'''

class Car:
    # 初始化方法
    def __init__(self,name,color="red",wheelNum=4):
        self.__name = name
        self.__color = color
        self.__wheelNum = wheelNum
    
    def __move(self):
        print("%s颜色的汽车在行驶~~~"%self.__color)

    def __str__(self):
        return "我是一辆%s汽车"%self.__name

    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color = color
    def get_move(self):
        self.__move()

    # 析构方法
    def __del__(self):
        print("我被删除了~~~")

    
BMW = Car(name="宝马",color="blue",wheelNum=4)
print(BMW.get_color())
BMW.get_move()

del BMW
    