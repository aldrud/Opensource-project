# Selection sorting (최소값 중심 정리)

def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

        list[i], list[min_idx] = list[min_idx], list[i]

# Bubble sorting

def bubbleSort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]

# Function to do insertion sort

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1

        while j>=0 and key < list[j]:
            list[j+1] =  list[j]
            j -= 1
        list[j+1] = key

import time
import random

print("각 sorting 알고리즘 수행 시간")
test_list = list(i for i in range(10000))


#=======================================================#

# Selection sorting 시간측정

random.shuffle(test_list)

start_time=time.time()
selectionSort(test_list)
end_time=time.time()

elapsed_time=end_time-start_time
print("\nSelection sorting : ")
print(elapsed_time)

# Bubble sorting 시간측정

random.shuffle(test_list)

start_time=time.time()
bubbleSort(test_list)
end_time=time.time()

elapsed_time=end_time-start_time
print("\nBubble sorting : ")
print(elapsed_time)

# Function to do insertion sort 시간측정

random.shuffle(test_list)

start_time=time.time()
insertionSort(test_list)
end_time=time.time()

elapsed_time=end_time-start_time
print("\nInsertion sorting : ")
print(elapsed_time)

# list.sort() 시간측정

random.shuffle(test_list)

start_time=time.time()
test_list.sort()
end_time=time.time()

elapsed_time=end_time-start_time
print("\nPython function sorting : ")
print(elapsed_time)

