# hjemmelavet decorator
def touppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@touppercase
def hello():
    return "hello"


print(hello())
print(hello.__name__)
print("-----------Generator expression-----------")
# Generators
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

generator = (x**2 for x in nums)
b = (i for i in range(100))
for i in range(10):
    print(next(b))

for num in generator:
    print(num)


print("----------pipeline generator------------")
def firstgenrator(nums):
    for num in nums:
        if num % 2 == 0:
            yield num


def secondgenerator(nums):
    for num in nums:
        yield 'The Number: %s' % num


temp = secondgenerator(firstgenrator(nums))

for num in temp:
    print(num)


# context manager
class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# simpel context manager
with open('demo', 'w') as opened_file:
    opened_file.write('simpelt men virker')
# file = open('some_file', 'w')
# try:
#     file.write('simpelt men virker')
# finally:
#     file.close()

with File('demo', 'w') as opened_file:
    opened_file.write("denne gang som en klasse")

from contextlib import contextmanager


@contextmanager
def openfile(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()



    with openfile('demo') as f:
        f.write("lidt risky")
