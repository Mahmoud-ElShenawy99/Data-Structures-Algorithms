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




def create_random_list(number_of_elements=100, sorted=False):
    list = []
    while (number_of_elements > 0):
        list.append(random.randint(-999999, 1000000))
        number_of_elements = number_of_elements - 1
        if sorted:
            list.sort()
    return list


if __name__ == '__main__':
    list = create_random_list(1000000)

    selection_time = selection_sort(list)

    print("Array size is ",str(len(list)))

    print("Running time for Selection sort  is " + str(selection_time * 100) + "ms")

