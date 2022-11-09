from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = {
        1000:'M', 900:'CM', 500:'D', 400:'CD',
        100:'C', 90:'XC', 50:'L', 40:'XL',
        10:'X', 9:'IX', 5:'V', 4:'IV',
        1:'I'
    }

    result = ''
    for value in sorted(romans.keys(), reverse=True): #내림차순
        while n >= value:
            result += romans[value]
            n -= value

    return result


def romanToDec(numStr):
    N = 0
    numStr = str(numStr)
    while(len(numStr) > 0):
        if numStr.find('M') == 0:
            N = N + 1000
            numStr = numStr[1:]
        elif numStr.find('CM') == 0:
            N = N + 900
            numStr = numStr[2:]
        elif numStr.find('D') == 0:
             N = N + 500
             numStr = numStr[1:]
        elif numStr.find('CD') == 0:
             N = N + 400
             numStr = numStr[2:]
        elif numStr.find('C') == 0:
             N = N + 100
             numStr = numStr[1:]
        elif numStr.find('XC') == 0:
             N = N + 90
             numStr = numStr[2:]
        elif numStr.find('L') == 0:
             N = N + 50
             numStr = numStr[1:]
        elif numStr.find('XL') == 0:
             N = N + 40
             numStr = numStr[2:]
        elif numStr.find('X') == 0:
            N = N + 10
            numStr = numStr[1:]
        elif numStr.find('IX') == 0:
            N = N + 9
            numStr = numStr[2:]
        elif numStr.find('V') == 0:
            N = N + 5
            numStr = numStr[1:]
        elif numStr.find('IV') == 0:
            N = N + 4
            numStr = numStr[2:]
        elif numStr.find('I') == 0:
            N = N + 1
            numStr = numStr[1:]
        else:
            return 'Error!'
    return N




