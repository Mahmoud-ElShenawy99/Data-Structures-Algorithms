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

def merge(left_list:list,right_list:list,list:list):

    left_length=len(left_list)
    right_length=len(right_list)
    i=j=k=0
    while(i<left_length and j<right_length):
        if(left_list[i]>right_list[j]):
            list[k]=right_list[j]
            j=j+1
        else:
            list[k] =left_list[i]
            i = i +1
        k = k + 1
    while(i<left_length):
        list[k] = left_list[i]
        k = k + 1
        i = i + 1
    while(j<right_length):
        list[k] = right_list[j]
        k = k + 1
        j = j + 1

def merge_sort(list):
    begin = time.time()
    if len(list)<2:
        return
    mid=int(len(list)/2)
    left_list=list[:mid]
    right_list=list[mid:]
    merge_sort(left_list)
    merge_sort(right_list)
    merge(left_list,right_list,list)
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
    listcopy3 = list.copy()

    selection_time = selection_sort(list)
    insertione_time = insertion_sort(listcopy1)
    merge_time = merge_sort(listcopy2)
    bubble_time = bubble_sort(listcopy3)
    print("Array size is ",str(len(list)))
    print("Running time for Merge sort  is " + str(merge_time * 100) + "ms")
    print("Running time for Selection sort  is " + str(selection_time * 100) + "ms")
    print("Running time for Insertion sort  is " + str(insertione_time * 100) + "ms")
    print("Running time for Bubble sort  is " + str(bubble_time * 100) + "ms")


