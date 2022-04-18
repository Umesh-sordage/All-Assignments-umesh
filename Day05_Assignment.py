# def nozero(fnc):
#     def helper(*args):
#         print(fnc(*args))
#     return helper
# @nozero
# def div(x, y):
#     return x / y
#
# @nozero
# def mul(x, y):
#     return x * y
#
# @nozero
# def add(x, y):
#     return x + y
#
# @nozero
# def sub(x, y):
#     return x - y
#
# div(10,5)
# mul(50,5)
# add(20,5)
# sub(30,5)
print("_" * 40)
print("Assignment 1")


def nozero(fnc):
    def helper(*args):
        #     print("logged into the service...")
        print(fnc(*args))  # callback

    #     print("logged out the service...")
    #     print("_"*40)
    #
    return helper


@nozero
def add(x, y):
    print("add function called")
    return x + y


@nozero
def sub(x, y):
    print("sub function called")
    return x - y


@nozero
def mul(x, y):
    print("mul function called")
    return x * y


@nozero
def div(x, y):
    print("div function called")
    return x / y


addlogger = nozero(add)
addlogger(10, 20)
add(123, 12)
sub(10, 7)
mul(3, 6)
div(100, 10)
print("-" * 40)
print("Assignment 2")

'''
Assignment 2

@drawborder('*','#',40)
def greet(msg):
    print("greet",msg)

@drawborder('=','_',30)
def RSVP(msg): 
    print("RSVP",msg)
'''


def drawborder(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)

    return helper


def drawborder2(fnc):
    def helper(*args):
        print("#" * 40)
        fnc(*args)
        print("=" * 40)

    return helper


@drawborder
@drawborder2
def greet(msg):
    print("greet", msg)


@drawborder
@drawborder2
def RSVP(msg):
    print("RSVP", msg)


greet("welcome to India")
RSVP("welcome to event")


"""
Assignment 3
@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args)

@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
"""
print("-" * 40)
print("Assignment 3")

def logBeforeAfter(func):
    def helper(*args, **kwargs):
        print("=" * 40)
        func(*args, **kwargs)
        print("#" * 40)
    return helper

@logBeforeAfter
def fun(x, y):
    print("fun", x+y)

@logBeforeAfter
def fun1(args):
    print("fun1", args)

@logBeforeAfter
def fun2(kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(args, kwargs):
    print("fun3", args, kwargs)

fun(5,6)
fun1(5)
fun2(6)
fun3(5, 6)