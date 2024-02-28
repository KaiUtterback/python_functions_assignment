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

greeting()