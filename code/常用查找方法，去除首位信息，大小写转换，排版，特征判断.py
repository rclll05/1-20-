a = '''我是容程朗，
就读于广东工业大学计算机学院人工智能创新班。
努力学习更多有关python的知识内容，
希望有朝一日成为兼具能力与学识的国家栋梁。'''
print(a.find("朗"))
print(len(a))
print(a.startswith("我是容程朗"))
print(a.endswith("栋梁。"))
print(a.find("容"))
print(a.rfind("容"))
print(a.count("我"))
print(a.isalnum())


b = ("rcl love porgramming,LOVE.")
print(b.capitalize())
print(b.title())
print(b.upper())
print(b.lower())
print(b.swapcase())

print("##love#you##".strip("#"))
print("##love#you##".rstrip("#"))
print("##love#you##".lstrip("#"))

c = "python"
print(c.center(10,"*"))
print(c.ljust(10,"*"))
print(c.rjust(10,"*"))

x = "rc100".isalnum()
y = "rcl容程朗".isalpha()
z = "050311".isdigit()
print(x,y,z)