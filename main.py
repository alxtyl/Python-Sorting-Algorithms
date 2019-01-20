import time
import timeit
from generator import generator
from bubblesort import bubbleSort
from mergesort import merge_sort, merge
from quicksort import quickSort
from selectionsort import selectionSort

f = open('num.txt', 'r')
bubbleWrite = open('bubblesort.txt', 'w')
mergeWrite = open('mergesort.txt', 'w')
quicksortWrite = open('quicksort.txt', 'w')
selectionsortWrite = open('selectionsort.txt', 'w')

generator()

unsorted_list = []

for line in f:
    unsorted_list.append(int(line.strip()))

start = time.process_time()
bubbleSort(unsorted_list)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Bubblesort:")
print("%.3f" % (elapsed))

start = time.process_time()
merge_sort(unsorted_list)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Mergesort:")
print("%.3f" % (elapsed))
mergeWrite.write('\n'.join(map(str, merge_sort(unsorted_list))))

start = time.process_time()
quickSort(unsorted_list)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Quicksort:")
print("%.3f" % (elapsed))

start = time.process_time()
selectionSort(unsorted_list)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Selectionsort:")
print("%.3f" % (elapsed))

f.close()
bubbleWrite.close()
mergeWrite.close()
quicksortWrite.close()
selectionsortWrite.close()
