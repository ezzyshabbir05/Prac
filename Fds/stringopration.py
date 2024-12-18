def isPalindrome(str):
    # Run loop from 0 to len/2

    reverse_str = ""
    for i in range(len(str), 0, -1):
        reverse_str = reverse_str + str[i - 1]
    print(reverse_str)
    if (str == reverse_str):
        print(" String is Palindrom")
    else:
        print("String is not palindrom")


def frequency_of_Character(str):
    count = 0
    char = input("Enter the character to find its frequency")
    for i in range(len(str)):
        if str[i] == char:
            count += 1
    print("Frequency count of "+char+"in given string is :",count)


def word_with_longest_length(str):
    l = list(str.split(" "))
    longest_word = ''
    for word in l:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word in given string is :", longest_word)


def frequency_of_each_word(str):

    str = str.split()
    newlist = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in newlist:
            # insert value in str2
            newlist.append(i)

    for i in range(0, len(newlist)):
        # count the frequency of each word(present
        # in str2) in str and print
        print('Frequency of', newlist[i], 'is :', str.count(newlist[i]))


def index_of_first_substring(str):
    str_sub=input("enter substring")
    str_list = str.split(" ")
    print(str_list)
    for i in range(len(str_list)):
        if(str_sub == str_list[i]):
            print(str)
            print("Index of first appearance of substring",'"{}"'.format(str_sub),"is :",i)
            break
    pass


while True:
    print("1.Check weather string is Palindrom or not")
    print("2.Determine frequency count of particular character in given string")
    print("3. Display word with longest length")
    print("4.Count the occurance of each word in given string")
    print("5.Display index of first appearance of substring")
    print("6.Exit")

    ch = int(input("enter your choice"))
    if ch == 1:
        str = input("enter the string")
        isPalindrome(str)
    elif ch == 2:
        str = input("enter the string")
        frequency_of_Character(str)
    elif ch == 3:
        str = input("enter the string")
        word_with_longest_length(str)
    elif ch == 4:
        str = input("enter the string")
        frequency_of_each_word(str)
    elif ch == 5:
        str = input("enter the string")
        index_of_first_substring(str)
    elif ch==6:
        break
    else:
        print("Invalid choice")

