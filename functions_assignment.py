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


# calculator()

# The Temperature Converter

'''
Create a program that converts temperatures between fahrenheit and Celsius

Task 1: Code a funciton that converts celsius to fahrenheit 
Task 2: Code a function that converts fahrenheit to celsius
task 3: Implement a user interface that asks the user which conversion they want to perform and calls the appropriate function
'''

def cel_fah():
    print()
    celsius = input("Enter the temperature in Celsius: ")
    celsius = int(celsius)
    result_F = celsius * 1.8 + 32
    result_F = round(result_F, 2)
    print(f"{celsius} degrees celsius is equal to {result_F} degrees fahrenheit")

# cel_fah()
    
def fah_cel():
    print()
    fahrenheit = input("Enter the temperature in Fahrenheit: ")
    fahrenheit = int(fahrenheit)
    result_C = (fahrenheit - 32) * 0.556
    result_C = round(result_C, 2)
    print(f"{fahrenheit} degrees fahrenheit is equal to {result_C} degrees celsius")

def temperature_converter():
    while True:
        print()
        f_or_c = input("Welcome to Kai's Temperature converter!\n Would you like to convert Fahrenheit to Celsius or Celsius to Fahrenheit?\n Type Celsius for C-F or Fahrenheit for F-C. type x to exit: ")
        if f_or_c == 'celsius' or f_or_c == 'Celsius':
            cel_fah()
            continue
        elif f_or_c == 'fahrenheit' or f_or_c == 'Fahrenheit':
            fah_cel()
            continue
        else:
            print("Have a great day!")
            break

# temperature_converter()
        
# The Shopping List Maker
        
'''
Create a program that helps the user make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way
'''

def shopping_list():
    shop_list = []
    while True:
        print()
        add_list = input("Type the items you need to add to your shopping list or 'done' to exit: ")
        if add_list == 'done':
            break
        else:
            shop_list.append(add_list)
            continue
    print(shop_list)
    while True:
        rem_list = input("Would you like to remove items from your list? type r to remove or x to exit and see your list: ")
        if rem_list == 'r':
            item_removed = input("Choose an item to remove: ")
            if item_removed in shop_list:
                shop_list.remove(item_removed)
                print(f"This is your updated shopping list\n {shop_list}")
                continue
            else:
                print("Sorry that item isn't in your list")
                continue
        else:
            print(f"This is your shopping list:\n {shop_list}")
            break

# shopping_list()
        
# Grade Analyzer
        
'''
Task 1: Code a function to calculate the average grade
Task 2: Implement a function to find the highest and lowest grade
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc)
'''

def assign_letter_grade(grade):
    if grade <= 69:
        return 'F'
    elif grade <= 79:
        return 'C'
    elif grade <= 89:
        return 'B'
    elif grade <= 99:
        return 'A'
    else:
        return 'A+'

def grades():
    import math
    import statistics

    grade_list = []
    letter_grades = []

    while True:
        print()
        add_grade = input("Enter grade percent out of 100 here or x to exit: ")
        if add_grade == 'x':
            break
        else:
            add_grade = float(add_grade)
            grade_list.append(add_grade)
            letter_grades.append(assign_letter_grade(add_grade))


    av_grade = statistics.mean(grade_list)
    av_grade = round(av_grade, 2)
    max_grade = max(grade_list)
    min_grade = min(grade_list)

    av_letter_grade = assign_letter_grade(av_grade)
    max_letter_grade = assign_letter_grade(max_grade)
    min_letter_grade = assign_letter_grade(min_grade)

    print(f"Grades in your list are\n {grade_list}\n {letter_grades}")
    print(f"The average grade is {av_grade}, {av_letter_grade}")
    print(f"The highest grade is {max_grade}, {max_letter_grade}")
    print(f"The smallest grade is {min_grade}, {min_letter_grade}")

# grades()    
    
# Daily Planner
    
'''
Create a simple daily planner that can add, remove, and display tasks.

Task 1: Write a function to add a task with a time slot
task 2: Code a function to remove a task
Task 3: Implement a display function that shows all tasks in order of time
'''

def add_task(tasks, time, task):
    tasks[time] = task

def remove_task(tasks, time):
    if time in tasks:
        del tasks[time]
        print("Task removed successfully.")
    else:
        print("Task not found at the given time.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks scheduled for today.")
    else:
        print("Tasks for today:")
        for time, task in sorted(tasks.items()):
            print(f"{time}: {task}")

def run_planner():
    print()
    tasks = {}

    while True:
        print("\nKai's Daily Planner Menu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice (by number): ")

        if choice == '1':
            time = input("Enter time for the task (e.g., 9:00 AM): ")
            task = input("Enter task: ")
            add_task(tasks, time, task)
            print("Task added successfully.")
        elif choice == '2':
            time = input("Enter time for the task to remove: ")
            remove_task(tasks, time)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting Daily Planner.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



# run_planner()

# The journey Planner
    
'''
Create a program that plans a journey, calclulating travel times and stops.

Task 1: Code a function that calculates travel time based on distance and speed.
Task 2: Create a feature that suggests stops based on the length of the journey
Task 3: Implement user input for starting point, destination, and preffered travel speed.
'''

def get_user_input():
    import random
    print()

    start_point = input("Enter starting point: ")
    destination = input("Enter Destination: ")
    speed = float(input("Enter preffered travel speed (mph): "))
    distance = random.randint(10, 1000) # Just going to assume a random distance for this case
    return start_point, destination, speed, distance 

def calculate_travel_time(distance, speed):
    time_hours = distance / speed
    time_hours = round(time_hours)
    return time_hours

def suggest_stops(distance):
    if distance <= 50:
        return ["Scenic viewpoint at Mile 25"]
    elif distance <= 200:
        return ["Rest stop at Mile 50", "Point of interest at Mile 100"]
    elif distance <= 400:
        return ["Rest stop at Mile 100", "Point of interest at Mile 200", "Scenic overlook at Mile 300"]
    elif distance <= 600:
        return ["Rest stop at Mile 150", "Point of interest at Mile 300", "Scenic overlook at Mile 450"]
    elif distance <= 800:
        return ["Rest stop at Mile 200", "Point of interest at Mile 400", "Scenic overlook at Mile 600", "Historical site at Mile 700"]
    else:
        return ["Rest stop at Mile 250", "Point of interest at Mile 500", "Scenic overlook at Mile 750", "Historical site at Mile 900", "Nature trail at Mile 950", "Picnic area at Mile 975"]


def journey_planner():
    print()
    print("Welcome to Kai's Journey Planner!")
    
    while True:
        start_point, destination, speed, distance = get_user_input()
        
        travel_time = calculate_travel_time(distance, speed)
        print(f"Estimated travel time from {start_point} to {destination}: {travel_time:.2f} hours")
        
        stops = suggest_stops(distance)
        if stops:
            print("Suggested stops:")
            for stop in stops:
                print("- " + stop)
        else:
            print("No suggested stops for this journey.")
        
        choice = input("Do you want to plan another journey? (yes/no): ")
        if choice != 'yes':
            print("Exiting Journey Planner.")
            break

# journey_planner()
        
# Personal Library organizer
        
'''
Create a system that organizes a personal library of books

Task 1: Write a function to add books with title, author, and genre
Task 2: Code a search function to find books by title or author
Task 3: Implement a way to display books sorted by genre or author
'''

def add_book(title, author, genre, library):
    book = {'title': title, 'author': author, 'genre': genre}
    library.append(book)
    print("Book added to your library.")

def search_book(query, library):
    search_results = []
    for book in library:
        if query in book['title'] or query in book['author'] or query in book['genre']:
            search_results.append(book)
    return search_results

def display_books(books, sort_key):
    sorted_books = sorted(books, key=lambda x: x[sort_key])
    for book in sorted_books:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

def remove_book(title, library):
    removed = False
    for book in library:
        if book['title'] == title:
            library.remove(book)
            print(f"Book '{title}' removed successfully.")
            removed = True
            break
    
    if not removed:
        print(f"Book '{title}' not found in the library.")

def library_organizer():
    library = [   # Just wanted to pre populate some of my favorite books in to the library
        {'title': 'Harry Potter and the Sorcerer\'s Stone', 'author': 'J.K. Rowling', 'genre': 'Fantasy'},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Classic'},
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Classic'},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Literary Fiction'},
        {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy'},
        {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance'},
        {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'genre': 'Young Adult'},
        {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'genre': 'Mystery'},
        {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Adventure'}
    ]
    
    while True:
        print("\nLibrary Organizer Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books sorted by genre")
        print("5. Display all books sorted by author")
        print("6. Exit")
        
        choice = input("Enter your choice (number): ")
        
        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            add_book(title, author, genre, library)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            remove_book(title, library)
        elif choice == '3':
            query = input("Enter the title or author to search: ")
            results = search_book(query, library)
            if results:
                print("Search results:")
                for book in results:
                    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
            else:
                print("No matching books found.")
        elif choice == '4':
            print("\nBooks sorted by genre:")
            display_books(library, 'genre')
        elif choice == '5':
            print("\nBooks sorted by author:")
            display_books(library, 'author')
        elif choice == '6':
            print("Exiting Library Organizer.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
# library_organizer()
            
# The Fitness Tracker

'''
Create a program that tracks fitness activities and calories burned.

Task 1: Develop a funciton to log different fitness activities and their duration
Task 2: Write a funciton that estimates calories burned based on teh activity and duration
Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
'''

import random

def log_activity(activity, duration, log):
    log.append({'activity': activity, 'duration': duration})

def estimate_calories(activity, duration):
    return random.randint(100, 200)


def generate_summary_report(log):
    total_calories = 0
    max_activity_length = max(len(entry['activity']) for entry in log)
    max_activity_length += 15  
    
    print("Summary Report:")
    print(f"Activity{' '*(max_activity_length - 8)}Duration (min)\tCalories Burned")
    print("-" * (40 + max_activity_length))
    
    for entry in log:
        activity = entry['activity']
        duration = entry['duration']
        calories_burned = estimate_calories(activity, duration)
        total_calories += calories_burned
        print(f"{activity:<{max_activity_length}}\t{duration}\t\t{calories_burned}")
        
    print("-" * (40 + max_activity_length))
    print(f"Total Calories Burned: {total_calories}")

def user_input_for_activities():
    log = []
    print()
    print("Welcome to Kai's Fitness Tracker!")
    while True:
        print()
        activity = input("Enter the activity (or 'done' to finish): ")
        if activity.lower() == 'done':
            break
        duration_str = input("Enter the duration (in minutes): ")
        try:
            duration = int(duration_str)
        except ValueError:
            print("Invalid input. Duration must be a valid integer.")
            continue
        log_activity(activity, duration, log)
    return log


log = user_input_for_activities()
generate_summary_report(log)

