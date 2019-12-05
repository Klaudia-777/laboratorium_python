def deleting():
    input = open('test.txt', "r")
    line = input.read()
    words = ('sie', 'i', 'oraz', 'nigdy', 'dlaczego')
    for w in words:
        line = line.replace(w,'')
    with open('test2.txt', 'w') as input:
        input.write(line)

deleting()


def changing():
    input = open('test.txt', "r")
    line = input.read()

    set={'i ':'oraz ', 'oraz ':'i ', 'nigdy ':'prawie nigdy ', 'dlaczego ':'czemu '}
    for i,j in set.items():
        line = line.replace(i,j)
    with open('test2.txt', 'a') as input:
        input.write(line)

changing()



