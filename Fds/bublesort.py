

def selectionSort(array,n):
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if array[minIndex] > array[j]:
                minIndex =j
            temp = array[i]
            array[i]=array[minIndex]
            array[minIndex]=temp
    print("Sorted array after applying Selection Sort")
    for i in array:
        print(i, end=" ")


def bubbleSort(array , n):
    for i in range(n):
        for j in range(i+1,n):
            if array[i]>array[j]:
                temp = array[i]
                array[i]= array[j]
                array[j]=temp
    print("Sorted array after applying Bubble Sort")
    for i in array:
        print(i,end=" ")

    print("\n Top five score are")
    for i in range(len(array)-1,1,-1):
        print(array[i],end=" ")


print("enter the number of student in class")
n = int(input())
array = []
i =0
for i in range(n):
    print(f"Enter the percentage of student[{i}]")
    percentage = float(input())
    array.append(percentage)
print("You have entered following percentage:")

for i in array:
    print(i, end=" ")

while True:
    print()
    print("---------Main Menu---------")
    print("1.Selection Sort")
    print("2.Bubble Sort")
    print("3.Exit")
    ch = int(input("Enter your choice"))
    if ch ==1:
        selectionSort(array,n)
    elif ch == 2:
        bubbleSort(array, n)
    elif ch == 3:
        break
    else:
        print("Enter valid choice")