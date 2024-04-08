# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and 
# print out the largest number among the three.

#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))
#third_number = int(input("Enter thrid number: "))

#if first_number > second_number and first_number > third_number:
#    print(f"Largest number is {first_number}")
#elif second_number > first_number and second_number > third_number:
#    print(f"Largest number is {second_number}")
#elif third_number > first_number and third_number > second_number:
#    print(f"Largest number is {third_number}")

#Task 2, Identify the smallest
#Extend your program from Task 1 to also determine the smallest number among the three and print it out.

#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))
#third_number = int(input("Enter thrid number: "))

#if first_number > second_number and first_number > third_number:
#    print(f"Largest number is {first_number}")
#elif second_number > first_number and second_number > third_number:
 #   print(f"Largest number is {second_number}")
#elif third_number > first_number and third_number > second_number:
#    print(f"Largest number is {third_number}")
#if first_number < second_number and first_number < third_number:
#    print(f"Smallest number is {first_number}")
#elif second_number < first_number and second_number < third_number:
#    print(f"Smallest number is {second_number}")
#elif third_number < first_number and third_number < second_number:
#    print(f"Smallest number is {third_number}")

#Task 3: Equality Check
#Enhance your program to handle cases where two or all of the 
#numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" 
#or "All numbers are equal".


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter thrid number: "))

if first_number > second_number and first_number > third_number:
    print(f"Largest number is {first_number}")
elif second_number > first_number and second_number > third_number:
    print(f"Largest number is {second_number}")
elif third_number > first_number and third_number > second_number:
    print(f"Largest number is {third_number}")
if first_number < second_number and first_number < third_number:
    print(f"Smallest number is {first_number}")
elif second_number < first_number and second_number < third_number:
    print(f"Smallest number is {second_number}")
elif third_number < first_number and third_number < second_number:
    print(f"Smallest number is {third_number}")
if first_number == second_number and first_number > third_number:
    print(f"Your first and second numbers are largest and equal: {first_number}")
elif first_number == second_number and first_number < third_number:
    print(f"Your first and second numbers are smallest and equal: {first_number}")
elif second_number == third_number and second_number > first_number:
    print(f"Your second and third numbers are largest and equal: {second_number}")
elif second_number == third_number and second_number < first_number:
    print(f"Your second and third numbers are smallest and equal: {second_number}")
elif first_number == third_number and first_number > second_number:
    print(f"Your first and third numbers are largest and equal: {first_number}")
elif first_number == third_number and first_number < second_number:
    print(f"Your first and third numbers are smallest and equal: {first_number}")
if first_number == second_number and second_number == third_number:
    print(f"All numbers are equal: {first_number}")