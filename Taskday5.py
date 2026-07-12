# =========================
# Task 1
# =========================
if 'a' in "apple":
    print("Task 1: Present")
else:
    print("Task 1: Not Present")

# =========================
# Task 2
# =========================
if "Python" in "I am learning Python":
    print("Task 2: Present")
else:
    print("Task 2: Not Present")

# =========================
# Task 3
# =========================
if 'z' not in "banana":
    print("Task 3: z is not present")
else:
    print("Task 3: z is present")

# =========================
# Task 4
# =========================
if "cat" in "The cat is sleeping":
    print("Task 4: Present")
else:
    print("Task 4: Not Present")

# =========================
# Task 5
# =========================
num = int(input("Task 5 - Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Not Positive")

# =========================
# Task 6
# =========================
num = int(input("Task 6 - Enter a number: "))
if num == 0:
    print("Zero")
else:
    print("Not Zero")

# =========================
# Task 7
# =========================
num = int(input("Task 7 - Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# =========================
# Task 8
# =========================
a = int(input("Task 8 - Enter first number: "))
b = int(input("Task 8 - Enter second number: "))
if a > b:
    print("Greater:", a)
else:
    print("Greater:", b)

# =========================
# Task 9
# =========================
age = int(input("Task 9 - Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# =========================
# Task 10
# =========================
num = int(input("Task 10 - Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# =========================
# Task 11
# =========================
marks = int(input("Task 11 - Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# =========================
# Task 12
# =========================
ch = input("Task 12 - Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

# =========================
# Task 13
# =========================
ch = input("Task 13 - Enter a character: ")
if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

# =========================
# Task 14
# =========================
num = int(input("Task 14 - Enter a number: "))
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")

# =========================
# Task 15
# =========================
a = int(input("Task 15 - Enter first number: "))
b = int(input("Task 15 - Enter second number: "))
c = int(input("Task 15 - Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# =========================
# Task 16
# =========================
marks = int(input("Task 16 - Enter marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 75 <= marks <= 89:
    print("Grade B")
elif 60 <= marks <= 74:
    print("Grade C")
elif 40 <= marks <= 59:
    print("Grade D")
else:
    print("Grade F")

# =========================
# Task 17
# =========================
day = int(input("Task 17 - Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")

# =========================
# Task 18
# =========================
month = int(input("Task 18 - Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid")

# =========================
# Task 19
# =========================
a = int(input("Task 19 - Enter first number: "))
b = int(input("Task 19 - Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid Operator")

# =========================
# Task 20
# =========================
year = int(input("Task 20 - Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# =========================
# Task 21
# =========================
password = input("Task 21 - Enter password: ")

if password == "admin123":
    print("Correct Password")
else:
    print("Wrong Password")

print("\nPattern:")
for i in range(5, 0, -1):
    print("*" * i)

# =========================
# Task 22
# =========================
print("\nUsing for loop:")
for i in range(1, 11):
    print(i)

print("\nUsing while loop:")
i = 1
while i <= 10:
    print(i)
    i += 1