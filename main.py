import time
from generator import generator
from bubblesort import bubbleSort
from mergesort import merge_sort
from quicksort import quickSort
from selectionsort import selectionSort

arr = []

generator()

for line in fp:
   arr.append(int(line.strip()))

start = time.process_time()
bubbleSort(arr)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Bubblesort:")
print("%.3f" % (elapsed))

start = time.process_time()
merge_sort(arr)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Mergesort:")
print("%.3f" % (elapsed))

start = time.process_time()
quickSort(arr)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Quicksort:")
print("%.3f" % (elapsed))

start = time.process_time()
selectionSort(arr)
end = time.process_time()
elapsed = (end - start) * (10**6)
print("Time for Selectionsort:")
print("%.3f" % (elapsed))
