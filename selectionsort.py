f = open('num.txt', 'r')
fp = open('selectionsort.txt', 'w')

arr = []

for line in f:
    arr.append(int(line.strip()))

def selectionSort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

fp.write('\n'.join(map(str, selectionSort(arr))))

f.close()
fp.close()
