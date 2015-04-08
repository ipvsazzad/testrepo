fileOpener = open('dbconfig.conf', 'r')
lines = fileOpener.readlines()
fileOpener.close()
modificationWord = raw_input("Enter the value you want to change : ")

lineCounter = 0
for line in lines:
    if modificationWord in line:
        newValue = raw_input("enter New Value : ")
        lineArray = line.split(':')
        lines[lineCounter] = lineArray[0] + ':' + newValue + '\n'
        print("edit successful")
        break
    lineCounter += 1
if lineCounter == len(lines):
    print("keyword not found")
else:
    fileWriter = open('dbconfig.conf', 'w')
    fileWriter.writelines(lines)
    fileWriter.close()