import os
import pandas

if os.path.isfile("exel.csv") == True:
    text = pandas.read_csv("exel.csv", sep='\t')
    print(text)
    delete_record = input("Do you want to delete last entries? y/n")
    if delete_record == "y":
        text.drop(text.tail(1).index, inplace=True)
        text.to_csv("exel.csv", sep='\t')
        print(text)


add_record = input("Do you want to add new record? y/n")
if add_record == "y":
    q1 = input("Name of reader: ")
    q2 = input("Title of book: ")
    q3 = input("Time of rental a book: ")

    text_add = pandas.DataFrame({"name": [q1],
                       "book": [q2],
                       "days": [q3]})

    if os.path.isfile("exel.csv") == True:
        if text.empty == False:
            text_add.to_csv("exel.csv", sep='\t', mode='a', header=False)
        else:
            text_add.to_csv("exel.csv", sep='\t', header=True)
    else:
        text_add.to_csv("exel.csv", sep='\t', header=True)
