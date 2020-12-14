'''
    统计三国演义中name.txt中各个英雄出现的次数,和weapon.txt中武器出现的次数
'''
import re

f = open('./name.txt','r+')
names = f.read().split('|')

f1 = open('./sanguo_utf8.txt','r+',encoding="utf-8")
data = f1.read().strip()

times = []
for name in names:
    t = data.count(name)
    times.append(t)
result = sorted(times)

print(times)
print(result)

# re.findall()
re.findall(name,data)

# 使用pyecharts绘制柱状图