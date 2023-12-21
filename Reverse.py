
def reversed(givenList):
    givenList.reverse()
    for i in givenList:
        if isinstance(i,list):
            i.reverse()

    return givenList


myList = [[1, 2], [3, 4], [5, 6, 7]]
print(reversed(myList))