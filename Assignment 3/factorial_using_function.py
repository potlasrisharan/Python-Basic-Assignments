num=int(input("enter a number :-"))
def fact(num):
    if num==0:
        factorial=1
    elif num>0:
        factorial=num*fact(num-1)
    return factorial
factorial=fact(num)
print(f"the factorial of {num} is {factorial}")