from random import randrange

irand = randrange(0, 1000001)

f = open('num.txt', 'w')
x = 0

while x < 10000:
    x += 1
    irand = randrange(0, 10001)
    f.write(str(irand))
    f.write("\n")
    if (x == 10000):
        f.close()
        break
