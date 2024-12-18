

def avg_score(n):
    sum = 0
    #count = 0
    for i in range(len(marklist)):
        if marklist[i] != 'a':
            sum = sum + int(marklist[i])
       # count += 1
    print("Total marks :", sum)
    print("Avarage score of class is : ", sum / n)
    print("-----------------------------------------------")


def high_low_score():
    for i in range(len(marklist)):
        if marklist[i]!='a':
            highest_mark = marklist[i]
            print(highest_mark)
            break
        else:
            highest_mark = marklist[0]
    for i in range(1,len(marklist)):
        if marklist[i] != 'a':
            if marklist[i]>highest_mark:
                highest_mark = marklist[i]
    print("Highest score of class is : ", highest_mark)

    lowest_score = marklist[0]
    for number in marklist:
        if number != 'a':
            if number < lowest_score:
                lowest_score = number
    print("Lowest Score of class is : ", lowest_score)
    print("-----------------------------------------------")


def count_absent():
    count = 0
    for i in range(len(marklist)):
        if marklist[i] == 'a':
            count += 1
    print("Total count of absent student is : ",count)
    print("-----------------------------------------------")


def mark_with_highest_frequency():
    count = 0
    mark = marklist[0]
    for i in marklist:
        if i != 'a':
            freq = marklist.count(i)
            if freq > count:
                count = freq
                mark = i

    # printing result
    print("marks with highest frequency is : " + str(mark) +"and it occures :", str(count) + "times")
    print("-----------------------------------------------")


marklist = []
print("enter the no of student in class")
n = int(input())

print("enter the marks of student. Press 'a' for absent ")
for i in range(n):
    mark = (input(f"Student[{i}]"))
    marklist.append(mark)
print("-----------------------------------------------")
print("Marklist of FDS Subject of class SE is :", marklist)

print("-----------------------------------------------")

while (True):
    print("1.The average score of class ")
    print("2. Highest score and lowest score of class")
    print("3.Count of students who were absent for the test")
    print("4.Display mark with highest frequency")
    print("5. Exit")

    ch = int(input("Enter your choice"))
    print("-----------------------------------------------")

    if ch == 1:
        avg_score(n)
    elif ch == 2:
        high_low_score()
    elif ch == 3:
        count_absent()
    elif ch == 4:
        mark_with_highest_frequency()
    elif ch == 5:
        break
    else:
        print("Enter valid choice from above menu")
