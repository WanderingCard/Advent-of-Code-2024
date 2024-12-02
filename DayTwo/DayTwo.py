def partOne():
    dataFile = open('DayTwo.txt', 'r', encoding='utf-8')
    validLines = 0
    for line in dataFile:
        record = convertToint(line.split())
        if safeLine(record):
            validLines += 1
            # print(record)

    print("Part One Solution:", validLines)
    dataFile.close()
    return

def partTwo():
    dataFile = open('DayTwo.txt', 'r', encoding='utf-8')
    # dataFile = open('DayTwoTest.txt', 'r',  encoding='utf-8')
    validLines = 0
    for line in dataFile:
        record = convertToint(line.split())
        if dapenSafeLine(record):
            validLines += 1
            # print(record)
        else:
            print(record)

    print("Part Two Solution:", validLines)
    dataFile.close()
    return

def convertToint(array):
    outArray = []
    for i in range(len(array)):
        outArray.append(int(array[i]))
    return outArray

def safeLine(lineData):
    increasing = lineData[1] > lineData[0]
    if increasing:
        if max(lineData) > int(lineData[0]) + (3 * (len(lineData)-1)) or min(lineData) < lineData[0]:
            return False
    else:
        if max(lineData) > lineData[0] or min(lineData) < lineData[0] - (3 * len(lineData) - 1):
            return False
    for i in range(len(lineData)-1):
        if lineData[i] == lineData[i+1]:
            return False
        if abs(lineData[i+1] - lineData[i]) > 3:
            return False
        if increasing and lineData[i] > lineData[i+1]:
            return False
        if not increasing and lineData[i] < lineData[i+1]:
            return False
    return True

def dapenSafeLine(lineData):
    if safeLine(lineData):
        return True
    for i in range(len(lineData)):
        modifiedLevels = lineData[:i] + lineData[i+1:]
        if safeLine(modifiedLevels):
            return True
    return False

partOne()
partTwo()