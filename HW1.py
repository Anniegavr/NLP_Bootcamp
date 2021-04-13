Months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
          8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
DaysAndMon = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
              "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}


def getMonth(num):
    return Months[num]


def getDays(year, mon):
    if int(year) % 4 == 0:
        DaysAndMon["February"] = 29
    else:
        DaysAndMon["February"] = 28
    return DaysAndMon[mon]


monNum = int(input("Enter the number of the month:\n"))
print(getMonth(monNum))

year, month = input("Enter year and month:\n").split(',')
print(getDays(year, month))
