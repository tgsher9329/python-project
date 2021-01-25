from color import *
import json
# import sys
from tabulate import tabulate
# from Color_Console import *
# maybe try color-console^^^^^^^^to add color to text

# def colorize(table, month):
#     blackOnGreen = "\x1b[1;30;42m"
#     blackOnRed = "\x1b[1;30;41m"
#     reset = "\x1b[0m"

#     for day in table.keys():
#         x = 0
#         while x <  len(table[day]):
#             if table[day][x] == "YES":
#                 table[day][x] = (blackOnGreen + "YES" + reset)
#             elif table[day][x] == "NO":
#                 table[day][x] = (blackOnRed + "NO" + reset)
#             x += 1

# opens the two files we will be using to be able to read them
with open('yearData.json', 'r') as yearData:
    year = json.load(yearData)
with open('habitData.json', 'r') as habitData:
    habits = json.load(habitData)

    # make the menu put it in a while loop with a quit option
while True:
        print()
        print("Pick an option you would like to do. ")
        print("1. Log new day.")
        print("2. Check a month.")
        print("3. View or change daily habits.")
        print("4. Quit")
        user_input = input()

        # log a new day
        if user_input == '1':
            # checks to make sure that the habits dict is not empty
            if len(habits["habits"]) <= 0:
                print('You need to add some habits before you can view them.')

            # goes through the process of adding whether or not they did the habit for a certain day
            elif len(habits["habits"]) > 0:
                month = input('What month do you want to look at? (1-12) ')
                day = input('What day do you want to look at? (1-31) ')
                year[month][day].clear()
                with open('yearData.json', 'w') as yearData:
                    json.dump(year, yearData)
                habit_length = len(habits["habits"])

                # goes through each habit and asks if it as completed
                for i in range(habit_length):
                    that_habit = habits["habits"][i]
                    answer = input(f'Did you {that_habit}?("yes" or "no"')
                    answer = answer.upper()
                    year[month][day].append(answer)

                    # writes data to the other file
                    with open('yearData.json', 'w') as yearData:
                        json.dump(year, yearData)

            # this happens when they do not 
            else:
                print("It seems like you didnt enter a valid month and/or day")

        # shows the user the entire month that they choose
        elif user_input == '2':
            
            month = input('\nWhat month do you want to look at? (1-12) ')
                # print(year[month])
                # ^^^^^^ this prints the entire dict, in a hard to read manner
            

            # check to see if the month they want to see if there is anything in the days, if not tell them to enter a day, or multiple days
            # if the len of each day added together is longer than 0 then go to the table
            length = 0
            for i in year[month]:
                if (len(year[month][i]) > 0):
                    length += 1
                else:
                    length = length
                
            
            # tabulate and print table
            table = year[month]

            # adding color to the text in the table
            if ((int(month) >= 1 and int(month) <= 12) and (len(habits["habits"]) > 0) and (length > 0)):

                # gets the colorize funciton from the other file and uses it here
                colorize(table, month)


                print('Keep in mind, it is going to output them in the order you input them.')
                print(tabulate(table, headers = "keys", showindex = habits["habits"], tablefmt = "pretty"))
                

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
                
                if len(habits["habits"]) > 0:
                    print('Habits')
                    print(habits["habits"])
                else:
                    print("You have no habits yet.")

            # clear old habits and insert new
            elif habit_choice == '2':
                habits["habits"].clear()
                print('\nKeep in mind, you can only input 5 habits to work on. \nIt would be unlikely to be able to change more habits than that at one time.\nThis will over right any previously saved habits.')
                print('If you want less than 5 habits to work on just leave the space blank and hit enter.\n')
                while len(habits["habits"]) < 5:
                    new_habit = input('New habit: ')
                    if new_habit != '':
                        habits["habits"].append(new_habit)
                        with open('habitData.json', 'w') as habitData:
                            json.dump(habits, habitData)
                    elif new_habit == '':
                        break

            else:
                print('Invalid option.')

        # quit out of the app
        elif user_input == '4':
            print('Good luck')
            quit()
        
        # tells the user that their input was invalid
        else:
            print('Invalid choice, choose another.')