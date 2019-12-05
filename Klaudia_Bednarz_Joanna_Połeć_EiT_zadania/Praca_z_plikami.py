import os, os.path

path = '/dev'

def counting():
    l = list(os.listdir(path))
    # print(len(l))
    length = 0
    for i in l:
        if not (os.path.isdir('/dev/' + i)):
            length = length + 1
        # print(length)
    return length

counting()


def structure(p):
    for i in os.listdir(p):
        if (os.path.isdir(os.path.join(p, i))):
            subP = p + '/' + i
            print(subP)
            print(os.listdir(subP))
            structure(subP)

structure(path)


# konwersja jpg na png
def conversion(path):
    for i in os.listdir(path):
        if (os.path.isfile(os.path.join(path, i))):
            if i[-4:] == '.jpg':
                os.rename(path + '/' + i, path + '/' + i[:-4] + '.png')

conversion(path)

