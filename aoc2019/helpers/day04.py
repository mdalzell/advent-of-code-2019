import re
import sys

consecutiveDigitsRegex = r"(\d)\1"

exactlyTwoConsecutiveDigitsRegex = r"(?:(\d)(?!\1)(\d)(?=\2)\d(?!\2))|(?:^(\d)(?=\3)\d(?!\3))"


def hasRegexMatch(password, regex):
    return re.search(regex, str(password)) is not None


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
    for x in range(begin, end + 1):
        if validPassword(x, regex):
            validCount += 1
    return validCount
