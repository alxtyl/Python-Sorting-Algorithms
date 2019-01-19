import datetime
from generator import generator
from bubblesort import bubbleSort
from mergesort import merge_sort, merge
from quicksort import quickSort
from selectionsort import selectionSort

f = open('num.txt', 'w')
fp = open('num.txt', 'r')
bubbleWrite = open('bubblesort.txt', 'a')
mergeWrite = open('mergesort.txt', 'a')
quicksortWrite = open('quicksort.txt', 'a')
selectionsortWrite = open('selectionsort.txt', 'a')

generator()

array = []

for line in fp:
    array.append(int(line.strip('\n')))

start = datetime.datetime.now()
bubbleSort(array)
end = datetime.datetime.now()
elapsed = end - start
print("Time for Bubblesort:")
print(elapsed.seconds,":",(elapsed.microseconds)*1000)

start = datetime.datetime.now()
merge_sort(array)
end = datetime.datetime.now()
elapsed = end - start
print("Time for Mergesort:")
print(elapsed.seconds,":",(elapsed.microseconds)*1000)

start = datetime.datetime.now()
quickSort(array)
end = datetime.datetime.now()
elapsed = end - start
print("Time for Quicksort:")
print(elapsed.seconds,":",(elapsed.microseconds)*1000)

start = datetime.datetime.now()
selectionSort(array)
end = datetime.datetime.now()
elapsed = end - start
print("Time for Selectionsort:")
print(elapsed.seconds,":",(elapsed.microseconds)*1000)
