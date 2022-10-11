from os import listdir
from os.path import isfile

myFiles = []
listOfTimes = []
listOfDates = []
toDoList = []
desicion = 10
global notebookFileName

def tablePrint(list):
    print("{:<2} {:<20} {:<5} {:<10} {:<14} {:<6}".format('Id','Task','Time','Date','Priority','Status'))
    for note in list:
        id, task, time, date, priority, status = note.values()
        print("{:<2} {:<20} {:<5} {:<10} {:<14} {:<6}".format(id,task,time,date,priority,status))

def byPriority(list):
    if (list["priority"].lower() == "very important"):
        return 0
    elif (list["priority"].lower() == "important"):
        return 1
    elif (list["priority"].lower() == "not important"):
        return 2
    else:
        return 3

def byStatus(list):
    if (list["status"].lower() == "done"):
        return 0
    elif (list["status"].lower() == "in process"):
        return 1
    elif (list["status"].lower() == "failed"):
        return 2
    else:
        return 3

def byId(list):
    counter = 0
    lst = []
    a = int(list["id"])
    while (counter != a):
        if (int(list["id"]) != counter + 1):
            counter += 1
            lst.append(counter)
        else:
            counter = int(list["id"])
    return counter
    

def byTime(mainList):
    #listOfTimes.append(mainList["time"])
    listOfTimes.sort()
    print(listOfTimes)
    pos = 0
    for j in listOfTimes:
        if (mainList["time"]) == str(j):
            pos = j
            break
        else:
            pos += 1
    return pos

def byDate(mainList):
    day, month, year = mainList["date"].split(".")
    #print(day, month, year)
    newList = []
    indicator = 0
    pos = -1
    for i in listOfDates:
        newList.append(i["day"])
    for i in newList:
        if (newList[0] == i):
            indicator = 1
        else:
            indicator = 0
            break 
    #print(indicator)
    if (indicator == 1):
        newList = []
        for i in listOfDates:
            newList.append(i["month"])
        for i in newList:
            if (newList[0] == i):
                indicator = 1
            else:
                indicator = 0
                break 
        if (indicator == 1):
            newList = []
            for i in listOfDates:
                newList.append(i["year"])
            for i in newList:
                if (newList[0] == i):
                    indicator = 1
                else:
                    indicator = 0
                    break 
            if (indicator != 1):
                newList.sort()
                for i in newList:
                    if (year == i):
                        pos = i
        else:
            newList.sort()
            for i in newList:
                if (month == i):
                    pos = i
    else:
        newList.sort()
        for i in newList:
            if (day == i):
                pos = i
    return pos

def UIFileInteraction():
    myFiles = []
    for filename in listdir("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//"):
        if isfile("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + filename) and (filename[-4:] == ".csv"):
            myFiles.append(filename)
    print("Here is the list of your notebooks:")
    print(myFiles)
    print("Enter a notebook name you want to work with")
    global notebookFileName
    notebookFileName = input()
    if not notebookFileName in myFiles:
        print("There is no file with name '%s'. Do you want to create new file?\nEnter:\n1 - to create new file\n0 - to enter new notebook name." %(notebookFileName))
        chose = int(input())
        answers = [0, 1]
        while chose not in answers:
            print("You can't enter %i\nEnter:\n1 - to create new file\n 0 - to enter new notebook name." % (chose))
            chose = int(input())
        if chose == 1:
            with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName +".csv","w") as f:
                n = []
        if chose == 0:
            UIFileInteraction()

    else: 
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName,"r") as f:
            for line in f:
                lstWithNoSpaces = []
                lst = line.split(",")
                for i in lst:
                    i = i.strip()
                    lstWithNoSpaces.append(i)
                note = {
                    "id": int(lstWithNoSpaces[0]),
                    "task": lstWithNoSpaces[1],
                    "time": lstWithNoSpaces[2],
                    "date": lstWithNoSpaces[3],
                    "priority": lstWithNoSpaces[4],
                    "status": lstWithNoSpaces[5]
                }
                toDoList.append(note)

        


def newLine(list):
    number = 10
    answers = [0, 1, 2]
    while number not in answers:
        print("If you want to add a full line enter '1'. In this case you need to use ','.\nIf u want to enter task, time, date e.c.t. separetly enter '2'.\nIf you want to go back enter '0'")
        number = int(input())
    if number == 2:
        print("Enter a task")
        tsk = input().strip()
        print("Enter a time (Example: '10.32')")
        time = input().strip()
        print("Enter a date (Example: '31.01.2001')")
        date = input().strip()
        print("Enter a priority (Very important, Important or Not important)")
        prior = input().strip()
        print("Enter a status (Done, In process or Failed)")
        stat = input().strip()
        note = {
            "id": len(list) + 1,
            "task": tsk,
            "time": time,
            "date": date,
            "priority": prior,
            "status": stat
        }
        list.append(note)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "a") as f:
            if (len(list) != 1):
                f.write("\n")
            f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
            #f.write(", ".join(note["task"]))
            #f.write(", ".join(note["time"]))
            #f.write(", ".join(note["date"]))
            #f.write(", ".join(note["priority"]))
            #f.write(", ".join(note["status"]))
    if number == 1:
        print("Enter a line. Use ',' to separate task, time, date e.c.t.")
        lst1 = input()
        lst = lst1.split(",")
        lstWithNoSpaces = []
        for i in lst:
            i = i.strip()
            lstWithNoSpaces.append(i)
        note = {
            "id": len(list) + 1,
            "task": lstWithNoSpaces[0],
            "time": lstWithNoSpaces[1],
            "date": lstWithNoSpaces[2],
            "priority": lstWithNoSpaces[3],
            "status": lstWithNoSpaces[4]
        }
        list.append(note)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "a") as f:
            if (len(list) != 1):
                f.write("\n")
            f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])

def editLine(list):
    print("What line do you want to edit? Enter line's number.")
    lineNumber = int(input())
    while (lineNumber > len(list)):
        print("There is no line № %i. Try one more time" % (lineNumber))
        lineNumber = int(input())
    des = 10
    answers = [0, 1, 2]
    while des not in answers:
        print("If you want to edit full line, enter '1'.\nIf you want to edit something particular enter '2'.\nIf you want to go back enter '0'")
        des = int(input())
    if des == 1:
        print("Enter new line. Use ',' to separate task, date, time e.c.t.")
        lst = input().split(",")
        lstWithNoSpaces = []
        for i in lst:
            i = i.strip()
            lstWithNoSpaces.append(i)
        note = {
            "id": lineNumber,
            "task": lstWithNoSpaces[0],
            "time": lstWithNoSpaces[1],
            "date": lstWithNoSpaces[2],
            "priority": lstWithNoSpaces[3],
            "status": lstWithNoSpaces[4]
        }
        list[lineNumber - 1] = note
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            counter = 0
            for note in list:
                a = note["id"]
                #print(a)
                #print(note)
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(a) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    if des == 2:
        print("What column do you want to edit?")
        field = input()
        print("Enter new value for this field.")
        newValue = input()
        list[lineNumber - 1][field] = newValue
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])


def deleteLine(list):
    number = 10
    answers = [0, 1]
    while number not in answers:
        print("Do you really want to delete line?\n1 - Yes\n0 - No")
        number = int(input())
    if number == 1:
        print("What line do you want to delete? Enter it's number")
        lineID = int(input())
        while (lineID > len(list)):
            print("There is no line with №%i. Try one more time" % (lineID))
            lineID = int(input())
        idOFDeletedLine = list[lineID - 1]["id"]
        del list[lineID - 1]
        for note in list:
            if (int(note["id"]) > idOFDeletedLine):
                note["id"] -= 1
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    
def listSort(list):
    print("How do you want to sort list?\n1 - by priority\n2 - by status\n3 - by time\n4 - by ID\n5 - by Date\n0 - go back")
    answers = [0, 1, 2, 3, 4, 5]
    answer = int(input())
    while answer not in answers:
        print("You can't enter %i\n1 - by priority\n2 - by status\n3 - by time\n4 - by ID\n5 - by Date\n0 - go back" % (answer))
        answer = int(input())
    if answer == 1:
        list.sort(key = byPriority)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    if answer == 2:
        list.sort(key = byStatus)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    if answer == 3:
        for i in list:
            listOfTimes.append(i["time"])
        list.sort(key = byTime)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    if answer == 4:
        list.sort(key = byId)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            for note in list:
                counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])
    if answer == 5:
        for i in list:
            day, mounth, year = i["date"].split(".")
            note = {
                "day": day,
                "month": mounth, 
                "year": year
                }
            listOfDates.append(note)
        list.sort(key = byDate)
        with open("C://Users//Gleb//Desktop//developer//python//rk1//notebooks//" + notebookFileName, "w") as f:
            counter = 0
            for note in list:
                if (counter == 0):
                    counter = 1
                else:
                    f.write("\n")
                f.write(str(note["id"]) + ", " + note["task"] + ", " + note["time"] + ", "  + note["date"] + ", "  + note["priority"] + ", "  + note["status"])


'''with open("c://Users//Gleb//Desktop//developer//python//rk1//notebook.csv", "r") as f:
    for line in f:
        lstWithNoSpaces = []
        lst = line.split(",")
        for i in lst:
            i = i.strip()
            lstWithNoSpaces.append(i)
        note = {
            "id": int(lstWithNoSpaces[0]),
            "task": lstWithNoSpaces[1],
            "time": lstWithNoSpaces[2],
            "date": lstWithNoSpaces[3],
            "priority": lstWithNoSpaces[4],
            "status": lstWithNoSpaces[5]
        }
        toDoList.append(note)'''


UIFileInteraction()
while not (desicion == 0):
    answers = [0, 1, 2, 3, 4, 5]
    tablePrint(toDoList)
    print("What do you want to do?\nEnter:\n1 - to add a line\n2 - to edit a line\n3 - to delete a line\n4 - to sort list\n5 - to choose a new file\n0 - to exit")
    desicion = int(input())
    while desicion not in answers:
        print("You can't enter %i\nEnter:\n1 - to add a line\n2 - to edit a line\n3 - to delete a line\n0 - to exit" % (desicion))
        desicion = int(input())
    if desicion == 1:
        newLine(toDoList)
    if desicion == 2:
        editLine(toDoList)
    if desicion == 3:
        deleteLine(toDoList)
    if desicion == 4:
        listOfTimes = []
        listOfDates = []
        listSort(toDoList)
    if desicion == 5:
        toDoList = []
        UIFileInteraction()
