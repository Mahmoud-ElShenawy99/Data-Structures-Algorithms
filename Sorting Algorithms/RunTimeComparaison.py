import random
import time

def selection_sort(list: list):
    begin = time.time()
    list_length = len(list)
    for i in range(0, list_length - 1):
        minimum_index = i
        for j in range(i + 1, list_length):
            if (list[j] < list[minimum_index]):
                minimum_index = j
        list[i], list[minimum_index] = list[minimum_index], list[i]
    end = time.time()
    return end - begin

def bubble_sort(list: list):
    begin = time.time()
    list_length = len(list)
    sorted = True
    for i in range(1, list_length):
        for j in range(0, list_length - i):
            if (list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
                sorted = False
        if (sorted):
            break
    end = time.time()
    return end - begin

def insertion_sort(list: list):
    begin = time.time()
    list_length=len(list)
    for hole in range(1,list_length):
        key=list[hole]
        j=hole-1
        while( j>=0 and list[j]>key):
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
    end = time.time()
    return end - begin

def create_random_list(number_of_elements=100, sorted=False):
    list = []
    while (number_of_elements > 0):
        list.append(random.randint(-999999, 1000000))
        number_of_elements = number_of_elements - 1
        if sorted:
            list.sort()
    return list


if __name__ == '__main__':
    list = create_random_list(10000)
    listcopy1 = list.copy()
    listcopy2 = list.copy()


    selection_time = selection_sort(list)
    insertione_time = insertion_sort(listcopy1)
    bubble_time = bubble_sort(listcopy2)
    print("Array size is ",str(len(list)))
    print("Running time for Bubble sort  is " + str(bubble_time * 100) + "ms")
    print("Running time for Selection sort  is " + str(selection_time * 100) + "ms")
    print("Running time for Insertion sort  is " + str(insertione_time * 100) + "ms")


