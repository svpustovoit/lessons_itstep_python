"""
def назва_функції(аргументи):
    код функції


назва_функції(значення)

# однорядковий коментар
print('''
однорядковий коментар
однорядковий коментар
однорядковий коментар
''')

def first_function():
    print('Hello students!')

first_function()
print(first_function)

def second_function():
    hello = "Hello students!"
    name = input("What is your name?")
    return hello, name

print(second_function)
print(second_function())
#print(hello, name) ---> print("Hello students!", "Serhii")

def hello(arg_1, arg_2):
    return arg_1 + arg_2

print(hello)
print(hello("Hello", "World!"))
print(hello(3, 5))
print(hello(input("arg_1-"), input("arg_2-")))
x = "IT"
y = " Step"
print(hello(x, y))
"""
def s_triangle(a, h):
    s = .5 * a * h
    return s

print(f"площа трикутника s = {s_triangle(5, 6)}")
print(f"площа трикутника s ="
      f" {s_triangle(int(input('a=')), int(input('h=')))}")



