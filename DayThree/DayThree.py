import re

def main():
    # dataFile = open('DayThreeTest.txt', 'r', encoding='utf-8')
    dataFile = open('DayThree.txt', 'r', encoding='utf-8')

    lines = []
    for line in dataFile:
        lines.append(line)

    # print(lines)

    print("Part One Total: " + str(partOne(lines)))
    print("Part Two Total: " + str(partTwo(lines)))

    dataFile.close()

    return

def partOne(lines):
    total = 0
    for line in lines:
        regex = 'mul\(\d{1,3},\d{1,3}\)'
        validOuts = re.findall(regex, line)

        for validMul in validOuts:
            nums = re.findall('\d+', validMul)
            total += (int(nums[0]) * int(nums[1]))
    return total

def partTwo(lines):
    total = 0
    enabled = True
    for line in lines:
        regex = "(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"
        validInst = re.findall(regex, line)
        for inst in validInst:
            if inst == 'do()':
                print('do()')
                enabled = True
            elif inst == "don't()":
                enabled = False
                print("don't()")
            elif enabled == True:
                nums = re.findall('\d+', inst)
                total += (int(nums[0]) * int(nums[1]))
                print(inst)
    return total


main()