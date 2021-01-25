def colorize(table, month):
    blackOnGreen = "\x1b[1;30;42m"
    blackOnRed = "\x1b[1;30;41m"
    reset = "\x1b[0m"

    for day in table.keys():
        x = 0
        while x <  len(table[day]):
            if table[day][x] == "YES":
                table[day][x] = (blackOnGreen + "YES" + reset)
            elif table[day][x] == "NO":
                table[day][x] = (blackOnRed + "NO" + reset)
            x += 1
