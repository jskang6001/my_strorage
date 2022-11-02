from practice.assignment.제출 import calcFunctions


def Fucntion(key, n):
    if key == 'factorial (!)':
        return calcFunctions.factorial(n)

    elif key == '-> binary' :
        return calcFunctions.decToBin(n)

    elif key == 'binary -> dec' :
        return calcFunctions.binToDec(n)

    elif key == '-> roman' :
        return  calcFunctions.decToRoman(n)

