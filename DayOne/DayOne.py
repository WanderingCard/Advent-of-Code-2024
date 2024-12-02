

def main():
    dataFile = open('DayOne.txt', 'r', encoding='utf-8')
    leftList = []
    rightList = []
    listTwoCount = {}

    for line in dataFile:
        lineItems = line.split()
        leftList.append(int(lineItems[0]))

        rightListItem = lineItems[1]
        rightList.append(int(rightListItem))
        if rightListItem in listTwoCount:
            listTwoCount[rightListItem] = listTwoCount[rightListItem] + 1
        else:
            listTwoCount[rightListItem] = 1
        
    leftList.sort()
    rightList.sort()

    total = 0
    twoTotal = 0
    for i in range(len(leftList)):
        total += abs(leftList[i] - rightList[i])
        if str(leftList[i]) in listTwoCount:
            twoTotal += (leftList[i] * listTwoCount[str(leftList[i])])

    dataFile.close()

    print(total)
    print(twoTotal)
    return

main()