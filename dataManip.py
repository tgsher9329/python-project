from tabulate import tabulate
from checks import *
import json

with open('yearData.json', 'r') as yearData:
    year = json.load(yearData)
with open('habitData.json', 'r') as habitData:
    habits = json.load(habitData)

def getTable(table):
    print('Keep in mind, it is going to output them in the order you input them.')
    print(tabulate(table, headers = "keys", showindex = habits["habits"], tablefmt = "pretty"))

def logNewDay():
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


def logNewHabits():
    habits["habits"].clear()
    print('\nKeep in mind, you can only input 5 habits to work on. \nIt would be unlikely to be able to change more habits than that at one time.\nThis will over right any previously saved habits.')
    print('If you want less than 5 habits to work on just leave the space blank and hit enter.\n')
    while habitLengthCheck(habits["habits"]) < 5:
        new_habit = input('New habit: ')
        if new_habit != '':
            habits["habits"].append(new_habit)
            with open('habitData.json', 'w') as habitData:
                json.dump(habits, habitData)
        elif new_habit == '':
            break