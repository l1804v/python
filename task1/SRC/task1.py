import sys


filePath = sys.argv[1]
numbersFile = open(filePath, 'r')
numbers = sorted([int(number) for number in numbersFile])
average = int(sum(n for n in numbers) / len(numbers))
percentileN = int(len(numbers) * 0.9)

numbersString = ""

for i in range(0, percentileN):
    num = numbers[i]
    if num > average:
        numbersString = numbersString + str(num)

finalSum = sum(int(letter) for letter in numbersString)

print(finalSum)