print (f"prework | python programing basic | program flow control")
"""
print (f"e-01")
i = 0
mx = 10
while i < mx:
    print(f"I am a Python programmer. {i}/{mx}")
    i += 1

print (f"e-02")
a = 2
i = 0
mx = 10
while i <= mx:
    print(f"{a} to the power of {i} is {pow(a,i)}")
    i += 1

print (f"e-03")
while True:
    f_name = input("first name:")
    s_name = input("second name:")
    if f_name == s_name:
        print(f"same")
    else:
        print(f"different")

    if f_name == "end":
        print(f"break")
        break

print (f"e-04")
a = float(input("a:"))
b = float(input("b:"))
l = "x"
if a > b:
    l = "a"
elif:
    a > b
else:
    l = "b"
print(f"{l} is greater!")

print (f"e-05")
print(f"Equation a*x**2 + b*x + c == 0")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
delta = a-b
if delta > 0:
    x_1 = (-b - delta**0.5) / (2 * a)
    x_2 = (-b + delta**0.5) / (2 * a)
    print(f"x_1: {x_1}")
    print(f"x_1: {x_2}")
elif delta == 0:
    val=0
    print ("Primes of the quadratic equation:")
    print (f"x_1 = x_2 = {val}")
else:
    print(f"no solution")

print (f"e-06")
n = int(input("n:"))
s=0
for i in range(0,n):
    s = s+i
print(f"suma: {s}")

print (f"e-07")
numbers = []
n = int(input("How many numbers do you want to enter? "))
for i in range(0,n):
    # num =
    numbers.append(float(input("Enter a number: ")))
total = sum(numbers)
if n>0:
    average = total/n
else:
    average = 0
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
if total > average:
    print("Sum is greater than average.")
else:
    print("Sum is NOT greater than average.")
numbers = []

counter = int(input("How many numbers do you want to add? "))
for i in range(counter):
    numbers.append(float(input("Number: ")))

result = sum(numbers)
average = result / len(numbers)

print(f"The result is: {result}")
print(f"The average is: {average}")
if result < average:
    print(f"average is greater")
else:
    print(f"result is greater than average")
    
print (f"e-08")
n = 8

for i in range(1,n+1):
    print(f"number: {i} ")
    
print (f"e-09")
n = int(input("Enter number: "))
for i in range(1,10+1):
    print(f"number: {i}*{n}={i*n}")

while True:
    n = int(input("Enter a number: "))
    if 0 < n < 11:
        break

for number in range(1, 11):
    print(f"{number} * {n} = {n * number}")

print (f"e-10")
for i in range(1,30+1):
    c=""
    if i%3==0:
        c = c + "Fizz"
    if i%5==0:
        c = c + "Buzz"
    if c == "":
        c = str(i)
    print(f"{c}")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")
        
    else:
        print(number)

int = 1
if int > 3:

    print("vetsi nez ... ")

elif int < 1:

    print("mensi nez ... ")

else:

    print("je ... ")

# if
print(f"value: {int}")

# ===========================

a = 23

if a < 12:
    print(f"si dieta")
elif a < 20:
    print(f"si teeneger")
else:
    print("si dospely")

print("KONIEC")


while True:
    print(a)
    a -= 1
    user_choice = input("KONIEC?")

    if a > 20:
        print("nastal continue")
        continue

    if user_choice == "yes":
        break

    print(f"si dieta")

print(f"si teeneger")

# ============================

user_num = 3 #int(input("Enter a number: "))
for i in range(0, user_num):
    print(i)

print()

n = 0
while n < 4:
    print(n)
    n += 1

print()
for i in range(2, 5):
    print(i)

print()
for i in range(8, 3, -1):
    print(i)

print()
word = "SLOVO"
names = ["Adam", "Eva", "karol"]
for name in names:
    for letter in name:
        print(letter)

for row in range(5):
    for col in range(5):
        print(row, col, end=" ")
    print()


nums = [pow(i, 2) for i in range(10) if i % 2 == 0]
print(nums)


numbers = [1, 2, 5]

for i in numbers:
    if i % 2 == 0:
        print("Even number found!")
        break

else:
    print("There are no even numbers on the list!")


if a:= pow(2, 3):
    print(a)

print(a)
"""
