# 1 The Welcoming Program

'''
Create a simple program that greets users and responds based on their input

Task 1: Code a program  that asks for the user's name and prints a personalized greeting.
Task 2: Modify the program to ask the user how they are feeling today and respond with a comforting message if they're feeling down, 
or a cheerful one if they're feeling happy.
Task 3: Add error handling to ensure that the user inputs a string for the name and not anumber or special character.
'''

# make a function that asks for the user's name and greets them
# use if statements to make responses to user input
# for the name block respond with an 'error' message if they enter a wrong answer or data type.

def greeting():
    print()
    while True:
        greet = input("Hello, my name is Kai, what is your name? ")

        if greet.isalpha():
            print(f"Hello {greet}! Nice to meet you!")
        else:
            print("I'm sorry please enter a valid name.\n Use letters only")
            continue

        feeling = input("How are you feeling today?\n (common responses are happy, sad, confused, tired, upset) ")

        if feeling == 'happy':
            print("I'm glad you're feeling happy! I hope that your day continues to go well!")
            break
        if feeling == 'sad':
            print("I'm sorry that you're feeling sad, I hope that your day gets better!")
            break
        if feeling == 'confused':
            print("Sometimes I get confused too,\n usually that means I need to take a break and have some coffee")
            break
        if feeling == 'tired':
            print("When I'm tired I take a nap! That always helps me!")
            break
        if feeling == 'upset': 
            print("When I get upset or frusterated I know it's time to take a break from whatever I'm doing.\n Maybe you need to go outside and take a walk?")
            break
        else:
            print("I'm not really used to that feeling, but I'm here for you if you need someone to talk to.")
            break

# greeting()

# The Calculator App

'''
Create a basic calculator that can perform addition, subtraction, multiplication, and division.

task 1: Create functions for each arithmetic operation
task 2: implement user input to receive numbers and an operation choice
task 3: Ensure your program can handle division by ero and other potential errors.
'''

# Create functions for addition, subtraction, multiplication, and division
# Create a function that runs one of the other 4 functions based on user input "What kind of problem would you like to solve today?"
# Make sure to check for errors 

import math

def adds (add_nums):
    add_result = add_nums[0]
    for add in add_nums[1:]:
        add_result += add
    return add_result

def addition():
    print()
    add_nums = []
    while True:
        add_input = input("Enter a number to add or 'done' when finished: ")
        if add_input == 'done':
            break
        try:
            add = float(add_input)
            add_nums.append(add)
        except ValueError:
            print("Sorry, please enter a number or done to finish")

    if len(add_nums) < 2:
        print("You need at least two numbers for addition")
    else:
        add_result = adds(add_nums)
        print(f"After adding\n {add_nums}\n your answer is {add_result}")

def subtraction(sub_nums):
    sub_result = sub_nums[0]
    for sub in sub_nums[1:]:
        sub_result -= sub
    return sub_result

def subtract():
    print()
    sub_nums = []
    while True:
        sub_input = input("Enter a number to subtract or 'done' when finished: ")
        if sub_input == 'done':
            break
        try:
            sub = float(sub_input)
            sub_nums.append(sub)
        except ValueError:
            print("Sorry, please enter a number or done to finish")

    if len(sub_nums) < 2:
        print("You need at least two numbers for subtraction")
    else:
        sub_result = subtraction(sub_nums)
        print(f"After subtracting\n {sub_nums}\n your answer is {sub_result}")

def multiplication_fun(mult_nums):
    mult_result = mult_nums[0]
    for mult in mult_nums[1:]:
        mult_result *= mult
    return mult_result

def multiplication():
    print()
    mult_nums = []
    while True:
        mult_input = input("Enter a number to multiply or done when finished: ")
        if mult_input == 'done':
            break
        try:
            mult = float(mult_input)
            mult_nums.append(mult)
        except ValueError:
            print("Sorry please enter a number or done to finish")

    if len(mult_nums) < 2:
        print("You need at least two numbers for multiplication")
    else:
        mult_result = multiplication_fun(mult_nums)
        print(f"After multiplying\n {mult_nums}\n your answer is {mult_result}")

def division_fun(div_nums):
    div_result = div_nums[0]
    for div in div_nums[1:]:
        div_result /= div
    return div_result

def division():
    div_nums = []
    while True:
        div_input = input("Enter a number to divide or done when finished: ")
        if div_input == 'done':
            break
        try:
            div = float(div_input)
            div_nums.append(div)
        except ValueError:
            print("Sorry please enter a number or done to finish")

    if len(div_nums) < 2:
        print("You need at least two numbers for division")
    else:
        div_result = division_fun(div_nums)
        print(f"After dividing\n {div_nums}\n your answer is {div_result}")

def calculator():
    print()
    while True:
        use = input("Would you like to use the calculator? y or n ")
        if use == 'y':
            print("What would you like to do?")
            options = input("Options are, addition, subtraction, multiplication, or division\n type your answer: ")
            if options == 'addition':
                addition()
                continue
            if options == 'subtraction':
                subtract()
                continue
            if options == 'multiplication':
                multiplication()
                continue
            if options == 'division':
                division()
                continue
            else:
                print("Sorry that's not an option at this time")
                continue
        else:
            break


calculator()

# The Temperature Converter

'''
Create a program that converts temperatures between fahrenheit and Celsius

Task 1: Code a funciton that converts celsius to fahrenheit 
Task 2: Code a function that converts fahrenheit to celsius
task 3: Implement a user interface that asks the user which conversion they want to perform and calls the appropriate function
'''