# Insert_sort

def insert_sort(mylist):
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i - 1

        while j >= 0 and mylist[j] > key:
            mylist[j + 1 ] = mylist[j]
            j = j - 1
        mylist[j + 1] = key


def printList(mylist):
    for i in range(len(mylist)):
        print(list[i])


list = [7,8,5,2,4,6,3]
insert_sort(list)
printList(list)


# Reference: http://www.geeksforgeeks.org/insertion-sort/