# PYTHON FUNDAMENTALS

# 1. Write Python code that prints your name, student number and email address.

print("Nabil Shajahan")
print(27)
print("nabil.shajahan@gmail.com")

# 2. Write Python code that prints your name, student number and email address using escape sequences.

print("Nabil Shajahan\n\t27\n\bnabil.shajahan@gmail.com")

# 3. Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

n1 = 14
n2 = 7

print(n1,"+",n2,"=", n1+n2)
print(n1,"-",n2,"=", n1-n2)
print(n1,"*",n2,"=",n1*n2)
print(n1,"/",n2,"=",n1/n2)


# 4. Write Python code that displays the numbers from 1 to 5 as steps.

for i in range(1,6):
    print(i)

# 5. Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
# An example runs of the program:
# "SDK" stands for "Software Development Kit", whereas
# "IDE" stands for "Integrated Development Environment".

print('\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\"')

# 6. Practice and check the output
# print("python is an \"awesome\" language.")
# print("python\n\t2023")
# print('I\'m from Entri.\b')
# print("\65")
# print("\x65")
# print("Entri", "2023", sep="\n")
# print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# 7. Define the variables below. Print the types of each variable.
# What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
# num=23
# textnum="57"
# decimal=98.3

num = 23
textnum = "57"
decimal = 98.3

print(type(num),type(textnum),type(decimal))
print(num+int(textnum)+decimal)

# 8. calculate the number of minutes in a year using variables for each unit of time.
# print a statement that describes what your code does also. Create three variables to store no of days in a year,
# minute in a hour, hours in a day, then calculate the total minutes in a year and print the values
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

Daysofyear = 365
Hoursinday = 24
Mininhour = 60

print("Multiplying above three variables\nwill give total minutes in a year which is",Daysofyear*Hoursinday*Mininhour,"minutes")

# 9. Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program:
# Please enter you name: Tony
# Hi Tony, welcome to Python programming :)

name = input("Enter your name:")
print(f"Hi {name},welcome to Python programming :)")

