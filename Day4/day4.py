import re
import sys

consecutiveDigitsRegex = r"(\d)\1"

exactlyTwoConsecutiveDigitsRegex = r"(?:(\d)(?!\1)(\d)(?=\2)\d(?!\2))|(?:^(\d)(?=\3)\d(?!\3))"

def hasRegexMatch(password, regex):
    return re.search(regex, str(password)) != None

def validPassword(password, regex):
    return hasRegexMatch(password, regex) and alwaysIncreasing(password)

def alwaysIncreasing(password):
    passwordString = str(password)
    for x in range(0, len(passwordString) - 1):
        if int(passwordString[x + 1]) < int(passwordString[x]):
            return False
    return True

def countValidPasswordsInRange(begin, end, regex):
    validCount = 0
    for x in range(begin, end +  1):
        if validPassword(x, regex):
            validCount += 1
    return validCount

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == "part2"):
        print(countValidPasswordsInRange(152085, 670283, exactlyTwoConsecutiveDigitsRegex))
    else:
        print(countValidPasswordsInRange(152085, 670283, consecutiveDigitsRegex))