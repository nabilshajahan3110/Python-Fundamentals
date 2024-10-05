# Python-Fundamentals
Python exercise covering the fundamental concepts 

Created by NABIL SHAJAHAN

This assignment consists of 10 questions covering the fundamental topics of Python

1. Write Python code that prints your name, student number and email address.

print("Nabil Shajahan")
print(27)
print("nabil.shajahan@gmail.com")
 

![PF 1](https://github.com/user-attachments/assets/f5927e61-5996-40f2-b395-e295592807d2)



2. Write Python code that prints your name, student number and email address using escape sequences.

print("Nabil Shajahan\n\t27\n\bnabil.shajahan@gmail.com")
 


![PF 2](https://github.com/user-attachments/assets/7a53cc73-1ccd-4d55-98c0-bcb4c5f79d1f)



3. Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

n1 = 14
n2 = 7

print(n1,"+",n2,"=", n1+n2)
print(n1,"-",n2,"=", n1-n2)
print(n1,"*",n2,"=",n1*n2)
print(n1,"/",n2,"=",n1/n2)
 


![PF 3](https://github.com/user-attachments/assets/a445f84e-b4d3-49f3-88c8-3a7261c9aefd)




4. Write Python code that displays the numbers from 1 to 5 as steps.

for i in range(1,6):
    print(i)
 


![PF 4](https://github.com/user-attachments/assets/4dd3dc30-c086-4236-9f7a-951cdc6ca95e)



5. Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen: An example runs of the program:
"SDK" stands for "Software Development Kit", whereas
"IDE" stands for "Integrated Development Environment".

print('\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\"')
 


![PF 5](https://github.com/user-attachments/assets/e216d220-7131-4704-a06e-fb3ef1d54f7c)




6. Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
 


![PF 6](https://github.com/user-attachments/assets/6869e7f8-735f-486c-8569-e15b772d315f)




7. Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
num=23, textnum="57", decimal=98.3

num = 23
textnum = "57"
decimal = 98.3

print(type(num),type(textnum),type(decimal))
print(num+int(textnum)+decimal)
 


![PF 7](https://github.com/user-attachments/assets/a3f05c58-d45f-48c6-b440-5e752d9a5e72)




8. calculate the number of minutes in a year using variables for each unit of time. Print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in an hour, hours in a day, then calculate the total minutes in a year and print the values. (hint) total number of minutes in a year =No.of days in a year * Hours in a day * Minutes in an hour

Daysofyear = 365
Hoursinday = 24
Mininhour = 60

print("Multiplying above three variables\nwill give total minutes in a year which is",Daysofyear*Hoursinday*Mininhour,"minutes")
 


![PF 8](https://github.com/user-attachments/assets/4e6d628e-9e1e-4921-b7ff-23ac47c138b3)



9. Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
An example runs of the program:
Please enter you name: Tony
Hi Tony, welcome to Python programming :)

name = input("Enter your name:")
print(f"Hi {name},welcome to Python programming :)")
 


![PF 9](https://github.com/user-attachments/assets/fcd752fd-2a9f-43dc-b214-dd01a88e789b)



10. Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)

Amount1 = int(input("Enter amount in GBP:"))
Amount2 = 1.33*Amount1

print(f"GBP {Amount1} in USD is {Amount2}")


 
![PF 10](https://github.com/user-attachments/assets/1fbeb017-b180-4a08-abf4-ef26fb952ac6)
