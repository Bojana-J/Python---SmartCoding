
entered_number = int(input('Enter any number:'))

def mult(number):
    newNumber = number * 3
    return newNumber

print (mult (entered_number))



number1 = int(input('Enter number 1:'))
number2 = int(input('Enter number 2:'))

def add(a,b):
    number = a + b
    return number

print (add(number1, number2))


numbers = [1,2,3,6]

num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])
num4 = int(numbers[3])

def sumOfListNumbers (a, b, c, d):
    some = a + b + c + d
    return some

print(sumOfListNumbers(num1, num2, num3, num4))
