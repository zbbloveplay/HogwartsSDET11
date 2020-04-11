from hogwarts.sdet.Student import Student

# 打印字符串的几种方式
# 单引号双引号都是一样的，只是当使用双引号的时候语句内的双引号要转义，单引号一样
print('C:\\some\\name')  # 1)单引号需要转移符号

print(r'C:\some\name')  # 2）前面加r就不需要转义符号

x = 'abc'
print(f'C:\\some\\name\\{x}')  # 3）前面加f可以使用变量（花括号），但是要使用转义符号

print("C:\\some\\name\\{y}\\{x}".format(y=x, x=123))  # 4）普通的双引号模式需要.format

# 字符串的拼接
print('Py' 'thon')

y = 'efg'
print(x + y)

# 字符串的切片
print(y[1:2])

# Tuples 元祖
# 元祖的内容不可修改，内部可以嵌套元祖
t = 12345, 54321, 'hello!'

# Lists 列表
# 列表的内容可以修改
squares = list(map(lambda x: x ** 2, range(10)))
squares2 = [x ** 2 for x in range(10)]

# Set 集合
# 集合没有排列
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a = set('abracadabra')
b = set('alacazam')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# Dictionaries 词典
# 词典可以关系数据
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
print(list(tel))
print(sorted(tel))
print('guido' in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})

Student()
