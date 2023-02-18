def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
def substract(a,b):
    return a-b

a =int(input("Enter the First Number :"))
b= int(input("Enter the Second Number :"))
sum =sum(a,b)
print(f"The sum of two number is {sum}")
substract=substract(a,b)
print(f"The difference of a-b is {substract}")
mul = mul(a,b)
print(f"The mul of the number : {mul}")
divide=divide(a,b)
print(f"The divide between two number is {divide}")
