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

def s_triangle(a, h):
    s = .5 * a * h
    return s

print(f"площа трикутника s = {s_triangle(5, 6)}")
print(f"площа трикутника s ="
      f" {s_triangle(int(input('a=')), int(input('h=')))}")

def calc(var_1, var_2, var_3):
    return var_1 * 3 + var_2 / 4 + var_3 ** 1.5

result_1 = calc(1, 2, 3)
print(f"result_1 = {calc(1, 2, 3)}")

result_2 = calc(var_2=2, var_3=3, var_1=1)
print(f"result_2 = {calc(var_2=2, var_3=3, var_1=1)}")

result_3 = calc(1, 2, var_3=3)
print(f"result_3 = {calc(1, 2, var_3=3)}")

print(f"result_4 = {calc(1, 2, var_3=3)}")

import random

def coin_simulator():
    coin = random.randint(0, 1)
    if coin == 0:
        print("Решка")
    else:
        print("Орел")

for i in range(5):
    coin_simulator()

var_1 = 5

def function_1():
    global var_2
    var_1 = 10
    print(f"function_1 --> var_1 = {var_1}")
    var_2 = 4

function_1()
print(f"global var_1 --> var_1 = {var_1}")
print(f"var_2 = {var_2}")

var_1 = 5

def first():
    var_1 = 10

    def second():
        print(f"nonlocal --> var_1 = {var_1}")

    second()

first()
print(f" global --> var_1 = {var_1}")

var_2 = 15
def first():
    var_1 = 10

    def second():
        nonlocal var_1
        var_1 = 1
        global var_2
        var_2 = 2

    second()
    print(f"local --> var_1 = {var_1}")

first()
print(f"global --> var_2 = {var_2}")
"""
# C++ --> const int number = 9.81
# Python констант немає, але домовились якщо --> NAME - то це константа

import config

name = config.NAME
print(name)











