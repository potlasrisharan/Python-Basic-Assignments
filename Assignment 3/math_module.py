import math
num=int(input("enter a number :"))
def square_root(num):
    return math.sqrt(num)
def natural_log(num):
    return math.log(num)
def sin_value(num):
    return math.sin(num)
a=square_root(num)
b=natural_log(num)
c=sin_value(num)
print(f"Square root of {num} is {a}")
print(f"Natural logarithm of {num} is {b}")
print(f"Sine of the {num} is {c}")