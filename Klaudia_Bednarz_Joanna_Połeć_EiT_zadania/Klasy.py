import re

class Zespolone:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __printNumber(self, x, y):
        if y >= 0:
            print("Result:\n" + str(x) + "+" + str(y) + "i")
        else:
            print("Result:\n" + str(x) + str(y) + "i")

    def __add__(self, other):
        x = self.re + other.re
        y = self.im + other.im
        self.__printNumber(x, y)
        return Zespolone(x, y)

    def __sub__(self, other):
        x = self.re - other.re
        y = self.im - other.im
        self.__printNumber(x, y)
        return Zespolone(x, y)

    def __mul__(self, other):
        x = self.re * other.re - self.im * other.im
        y = self.re * other.im + self.re * other.im
        self.__printNumber(x, y)
        return Zespolone(x, y)

    def __truediv__(self, other):
        divider = other.re ** 2 + other.im ** 2 == 0
        if divider:
            raise Exception("Dzielenie przez 0.")
        x = (self.re * other.re + self.im * other.im) / divider
        y = (self.im * other.re - self.re * other.im) / divider
        self.__printNumber(x, y)
        return Zespolone(x, y)


class Kalkulator:
    def __init__(self):
        self.operator = ''
        self.z1 = None
        self.z2 = None
        self.result = None

    def dodawanie(self, z1, z2):
        self.result = z1 + z2

    def odejmowanie(self, z1, z2):
        self.result = z1 - z2

    def mnozenie(self, z1, z2):
        self.result = z1 * z2

    def dzielenie(self, z1, z2):
        self.result = z1 / z2

    def __returnObj(self, stringToParse, userInput):
        if stringToParse == userInput:
            list = []
            sign = re.search('[+|-]', stringToParse)
            if sign.group(0) == '+':
                list = stringToParse.split('+')
            else:
                list = stringToParse.split('-')
            list[1] = list[1][0:1]

            return list

    def __parseChar(self, character):
        if not (character in ['+', '-', '*', '/']):
            raise Exception("Wrong operation!")
        else:
            self.operator = character

    def __parse(self, userInput, isFirstNumber):
        m = re.findall('[0-9]*[+|-][0-9]*i', userInput)
        print(m[0])
        number = self.__returnObj(m[0], userInput)
        print(number)
        if isFirstNumber:
            self.z1 = Zespolone(int(number[0]), int(number[1]))
        elif not isFirstNumber:
            self.z2 = Zespolone(int(number[0]), int(number[1]))

    def __getUserInput(self):
        isFirstNumber = True
        firstNumber = str(input("Enter first complex number:\n"))
        self.__parse(firstNumber, isFirstNumber)
        isFirstNumber = False
        operation = input("Enter operator:\n")
        self.__parseChar(operation)
        secondNumber = str(input("Enter second complex number:\n"))
        self.__parse(secondNumber, isFirstNumber)

    def perform(self):
        self.__getUserInput()
        oper = self.operator
        firstNumber = self.z1
        secondNumber = self.z2

        if oper == '+':
            self.dodawanie(firstNumber, secondNumber)
        elif oper == '-':
            self.odejmowanie(firstNumber, secondNumber)
        elif oper == '*':
            self.mnozenie(firstNumber, secondNumber)
        elif oper == '/':
            self.dzielenie(firstNumber, secondNumber)


kal = Kalkulator()
kal.perform()
