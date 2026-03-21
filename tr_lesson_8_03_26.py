s = "itstep"
s_1 = '012302'
for elem in s:
    print(f"elem = {elem}")

for elem in s_1:
    print(f"elem = {elem}")

lst = [12, "-25", True, (0, 12), ["one"], {"two": "three"}]
for elem in lst:
    print(f"elem = {elem}")

lst = [1, 2, 3, 4, 5]
iterator = iter(lst)
'''
print(f"next(iterator) = {next(iterator)}")
print(f"next(iterator) = {next(iterator)}")
print(f"next(iterator) = {next(iterator)}")
print(f"next(iterator) = {next(iterator)}")
print(f"next(iterator) = {next(iterator)}")
#print(f"next(iterator) = {next(iterator)}")
'''
print(f"type(iterator) = {type(iterator)}")

for elem in iterator:
    print(f"elem = {elem}")

print("повторне використання ітератора")

for elem in iterator:
    print(f"elem = {elem}")

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1      # self.i = self.i + 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)
for elem in count:
    print(f"elem = {elem}")


def raise_to_the_degress(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

result = raise_to_the_degress(122345, 500)
print(f"result = {result}")
for _ in result:
    print(f"_ --> {_}")

print("повторне використання генератора")

print(f"result = {result}")
for _ in result:
    print(f"_ --> {_}")

def raise_to_the_degres(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1
res = raise_to_the_degres(122345)
print(f"result = {res}")
for _ in res:
    print(f"elem = {_}")

class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return (f"I will help you with your {self.work}."
                f"\nAfterwards I will help you with your {work}.")

helper = Helper("homework")
print(helper("cleaning"))

def helper(work):
    work_in_memory = work

    def helper(work):
        return (f"Iwill help you with your {work_in_memory}."
                f"\nAfterwards I will help you with your {work}.")
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))

def cheker(function):
    def cheker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"Problems - {exc}")
        else:
            print(f"Not problems. Result: {result}")

    return cheker
'''
def calculate(expression):
    return eval(expression)

calculate = cheker(calculate)
calculate("2+3**3")
calculate("2+3**a")
'''
@cheker
def calculate(expression):
    return eval(expression)

calculate("2+3**3")

# логування
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="log.txt",
                    filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
















