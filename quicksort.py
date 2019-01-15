f = open('num.txt', 'r')
fp = open('quicksort.txt', 'w')

alist = []

for line in f:
    alist.append(int(line.strip()))

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

# first --> Starting index, last --> Ending index
def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

# the main function that implements QuickSort alist --> Array to be sorted, first --> Starting index, last --> Ending index
def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

quickSort(alist)
fp.write('\n'.join(map(str, alist)))
