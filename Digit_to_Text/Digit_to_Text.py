# Aufgabe 6 ("sehr schwer"): Struktogramm für eine Zahlenumwandlung
#   Eine nicht-negative Zahl (aus Ziffern) soll in einen Text umgewandelt werden, z. B. „123“ wird zu
#   „einhundertdreiundzwanzig“ (wir beschränken uns auf Kleinbuchstaben). Das Ganze soll in mehreren Schwierigkeitsstufen geschehen:
#   a) Es soll eine maximal zweistellige, natürliche Zahl in einen Text umgewandelt werden. Die Null
#      und die Eins sollen selbstverständlich korrekt genannt werden.
#   b) Es soll eine maximal dreistellige, natürliche Zahl in einen Text umgewandelt werden.
#   c) Es soll eine längere natürliche Zahl (maximal 18 Stellen) in einen Text umgewandelt werden.
#      Ggf. enthaltene Tausender-Punkte in der Zahl-Darstellung sollen ignoriert werden.
#
#   Python version: 3.6
#
#   Made by Linus Behrens

import re


one_diget_dictionary = {
    "1": "ein", "2": "zwei",
    "3": "drei", "4": "vier",
    "5": "fuenf", "6": "sechs",
    "7": "sieben", "8": "acht",
    "9": "neun", "0": "null"
}

two_diget_exeptions_dictionary = {
    "10": "zehn",
    "11": "elf",
    "12": "zwoelf",
    "1": "zehn",
    "2": "zwanzig",
}

len_number_dictionary = {
    "3": "hundert",
    "4": "tausend",
    "7": "milionen",
    "10": "miliarden",
    "13": "bilionen",
    "16": "biliarden",
}


def check_and_get_input():
    input_digit = input("Please enter an Number: ")
    if len(input_digit) > 18:
        print("enter was to long.")
        check_and_get_input()
    elif input_digit.find(",") != -1 or input_digit.find(".") != -1:
        if len(re.findall("\.", input_digit)) > 1:
            print("ip Adresse")
        elif input_digit.find(","):
            print("Doubel")
        else:
            print("Doubel")
    else:
        number_typ = WholeNumbers()
        number_typ.whole_numbers(input_digit)


class WholeNumbers:
    def __init__(self):
        self.result = []
        self.op = Operations()

    @staticmethod
    def reform(number, i):
        number = list(number)
        for i in range(i):
            del number[0]
        return "".join(number)

    def output(self):
        print(self.result)
        self.result = "".join(self.result)
        print(self.result)

    def whole_numbers(self, number):
        if len(number) == 1:
            one_diget_number = self.op.single_digits(number)
            if one_diget_number == "ein":
                one_diget_number += "s"
            number = self.reform(number, 1)
            self.result.append(one_diget_number)
            self.whole_numbers(number)

        elif len(number) == 2:
            two_diget_number = self.op.two_diget_check(number)
            number = self.reform(number, 2)
            if two_diget_number == "ein":
                two_diget_number += "s"
            self.result.append(two_diget_number)
            self.whole_numbers(number)

        elif len(number) in range(3, 19):
            longer_diget_number, i = self.op.longer_numbers(number)
            number = self.reform(number, i)
            if longer_diget_number != "null":
                self.result.append(longer_diget_number)
            self.whole_numbers(number)

        else:
            self.output()


class Operations:
    @staticmethod
    def single_digits(number):
        return one_diget_dictionary[number]

    def two_diget_check(self, number):
        if number[0] == "0":
            return self.single_digits(number[1])

        elif int(number[0]) in range(1, 3):
            if number[0] == "1":
                if int(number[1]) in range(0, 3):
                    return two_diget_exeptions_dictionary[number]
                else:
                    return self.two_digit_numbers(number)

            if number[0] == "2":
                if number[1] == "0":
                    return two_diget_exeptions_dictionary[number[0]]
                else:
                    return self.single_digits(number[1]) + "und" + two_diget_exeptions_dictionary[number[0]]

        elif number[0] > "1":
            return self.two_digit_numbers(number)

    def two_digit_numbers(self, number):
        if number[0] == "1":
            return self.single_digits(number[1]) + two_diget_exeptions_dictionary[number[0]]
        else:
            secound_number = self.single_digits(number[1])
            first_number = self.single_digits(number[0])
            if secound_number == "null":
                return first_number + "zig"
            return secound_number + "und" + first_number + "zig"

    def longer_numbers(self, number):
        if len(number) % 3 == 0:
            if len(number) > 3:
                return self.single_digits(number[0]) + len_number_dictionary[str(len(number) - 3 * (len(number) // 3 - 1))], 1

            else:
                if number[0] == "0":
                    return "null", 1
                else:
                    return self.single_digits(number[0]) + len_number_dictionary[str(len(number))], 1

        elif len(number) % 3 == 1:
            if number[0] == "0":
                return "null", 1
            else:
                return self.single_digits(number[0]) + len_number_dictionary[str(len(number))], 1

        elif len(number) % 3 == 2:
            if number[0] == "1" and len(number) > 6:
                return self.single_digits(number[0]) + len_number_dictionary[str(len(number) - 1)], 1

            else:
                return self.two_diget_check(number[0]+number[1]) + len_number_dictionary[str(len(number)-1)], 2


check_and_get_input()
