print("Task1.********") #Create a dictionary with your name, age, and city, then print the dictionary.
person = {
    "name": "Ravi",
    "age": 18,
    "city": "Lucknow"
}
print(person)


print("Task2.********") #Create a dictionary of a student with keys: name, roll_no, and marks. Print only the marks.
student = {
    "name": "Ravi",
    "roll_no": 101,
    "marks": 85
}
print(student["marks"])


print("Task3.********")# Create a dictionary with 3 fruits and their prices. Print the price of banana.
fruits = {
    "apple": 120,
    "banana": 50,
    "mango": 80
}
print(fruits["banana"])


print("Task4.********")# Create a dictionary with 2 subjects and their marks. Add one more subject with its marks and print the dictionary.
subjects = {
    "Math": 90,
    "English": 85
}
subjects["Science"] = 88
print(subjects)


print("Task5.********") #Create a dictionary with keys id and name. Add a new key department and print the updated dictionary.
emp = {
    "id": 1,
    "name": "Ravi"
}
emp["department"] = "CSE"
print(emp)


print("Task6.********") #Write a program to print numbers from 0 to 9 using range().
for i in range(10):
    print(i)


print("Task7.********") #Write a program to print numbers from 15 to 25 using range().
for i in range(15, 26):
    print(i)


print("Task8.********") #Write a program to print numbers from 5 to 30 by increasing 5 each time.
for i in range(5, 31, 5):
    print(i)


print("Task9.********") #Write a program to print numbers from 20 to 0 by decreasing 2 each time.
for i in range(20, -1, -2):
    print(i)


print("Task10.********")# Write a program to print all odd numbers from 1 to 19 using range().
for i in range(1, 20, 2):
    print(i)


print("Task11.********")# Take a number n as input and print numbers from 1 to n using range().
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)


print("Task12.********")#Use a for loop to print numbers from 1 to 5.
for i in range(1, 6):
    print(i)


print("Task13.********")# Use a for loop to print the word "Python" 5 times.
for i in range(5):
    print("Python")


print("Task14.********")# Use a for loop to print all numbers from 1 to 20.
for i in range(1, 21):
    print(i)


print("Task15.********")# Print each character of the string "WELCOME" using a for loop.
for ch in "WELCOME":
    print(ch)


print("Task16.********")# Use a for loop to print all odd numbers from 1 to 15.
for i in range(1, 16, 2):
    print(i)


print("Task17.********")#  Use a while loop to print numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1


print("Task18.********")# Use a while loop to print numbers from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i -= 1


print("Task19.********")# Use a while loop to print even numbers from 2 to 10.
i = 2
while i <= 10:
    print(i)
    i += 2


print("Task20.********")#Write a program using a while loop to print the word "Hello" 5 times.
i = 1
while i <= 5:
    print("Hello")
    i += 1