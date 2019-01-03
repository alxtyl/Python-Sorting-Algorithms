f = open('num.txt', 'r')
fp = open('sorted.txt', 'w')

numList = []

for line in f:
    numList.append(int(line.strip('\n')))

def bubblesort(numList):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


bubblesort(numList)
fp.write(str(numList) + "\n")
