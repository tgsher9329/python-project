from checks import monthLengthCheck
from dataManip import *
from color import *
from checks import *
import json

while True:

    # opens the two files we will be using to be able to read them

    with open('yearData.json', 'r') as yearData:
        year = json.load(yearData)
    with open('habitData.json', 'r') as habitData:
        habits = json.load(habitData)

    print()
    print("Pick an option you would like to do. ")
    print("1. Log new day.")
    print("2. Check a month.")
    print("3. View or change daily habits.")
    print("4. Quit")
    user_input = input()

    # log a new day
    if user_input == '1':

        print("\n1. Log today.")
        print("2. log another day.")
        newDay = input()

        # checks to make sure that the habits dict is not empty
        if not habitLengthCheck(habits["habits"]):
            print('You need to add some habits before you can view them.')

        # goes through the process of adding whether or not they did the habit for a certain day
        elif habitLengthCheck(habits["habits"]):

            logNewDay(newDay)

        # this happens when they do not 
        else:
            errorMessage()

    # shows the user the entire month that they choose
    elif user_input == '2':
            
        month = input('\nWhat month do you want to look at? (1-12) ')
        
        # tabulate and print table
        table = year[month]

        # adding color to the text in the table
        if ((int(month) >= 1 and int(month) <= 12) and (habitLengthCheck(habits["habits"])) and (monthLengthCheck(month) > 0)):

            colorize(table, month)
            getTable(table)
            
        else:
            print("Either you entered an invalid month, don't have any habits saved, or havent entered days into that month.")

    # view or change habits
    elif user_input == '3':
        print()
        print('1: view habits')
        print('2: set new habits(this will erase previously saved habits)')
        habit_choice = input()

        # view habits made
        if habit_choice == '1':
            
            if habitLengthCheck(habits["habits"]):
                print('Habits')
                print(habits["habits"])
            else:
                print("You have no habits yet.")

        # clear old habits and insert new
        elif habit_choice == '2':
            logNewHabits()

        else:
            errorMessage()

    # quit out of the app
    elif user_input == '4':
        print('Good luck')
        quit()
    
    # tells the user that their input was invalid
    else:
            errorMessage()