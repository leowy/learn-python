# 导入模块
import random

# 布尔值
print(True)
print(False)
# 比较操作符（==、!=、<、>、<=、>=）
print(1 == 1)
print(2 <= 1)
# 布尔操作符（and、or、not）
print(True and False)
print(True or False)
print(not True)

# if语句
print('please input your name:')
name = input()
if name == 'zhangw':
    print('yes,it\'s me')
elif name == 'damon':
    print('no,it\'s my son')
else:
    print('no')

# while语句，循环语句包含 continue、break使用、sys.exit()结束程序
print('please input your age:')
age = int(input())
while age <= 18:
    print('it\'s adult')
    age += 1

# for语句
total = 0
for i in range(1, 101):
    total += i
print(total)

for i in range(5):
    print(random.randint(1, 10))
