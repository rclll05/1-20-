a = "名字是：{0}，年龄是：{1}，{0}是个精神小伙"
b = a.format("容程朗",18)
c = a.format("容程刚",6)
print(b)
print(c)

d = "名字是：{name},年龄：{age}"
e = d.format(age=18,name="容程朗")
print(e)