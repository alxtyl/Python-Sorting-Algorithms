from random import randrange

# Opening file and declaring loop counter
f = open('num.txt', 'w')

def generator():
    x = 0
    # Generating nums
    while x < 1000:
        x += 1
        irand = randrange(0, 1001)
        f.write(str(irand))
        f.write("\n")

generator()

# Closing file object
f.close()
