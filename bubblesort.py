f = open('num.txt', 'r')
fp = open('bubblesort.txt', 'w')

numList = []

for line in f:
    numList.append(int(line.strip('\n')))

def bubbleSort(numList):
	n = len(numList)

	for i in range(n):

		for j in range(0, n-i-1):

			if numList[j] > numList[j+1]:
				numList[j], numList[j+1] = numList[j+1], numList[j]

bubbleSort(numList)

numList = list(map(str, numList))
fp.write("\n".join(numList))

f.close()
fp.close()
