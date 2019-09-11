# Aufgabe 6 ("sehr schwer"): Struktogramm für eine Zahlenumwandlung
#   Eine nicht-negative Zahl (aus Ziffern) soll in einen Text umgewandelt werden, z. B. „123“ wird zu
#   „einhundertdreiundzwanzig“ (wir beschränken uns auf Kleinbuchstaben). Das Ganze soll in mehreren Schwierigkeitsstufen geschehen:
#   a) Es soll eine maximal zweistellige, natürliche Zahl in einen Text umgewandelt werden. Die Null
#      und die Eins sollen selbstverständlich korrekt genannt werden.
#   b) Es soll eine maximal dreistellige, natürliche Zahl in einen Text umgewandelt werden.
#   c) Es soll eine längere natürliche Zahl (maximal 18 Stellen) in einen Text umgewandelt werden.
#      Ggf. enthaltene Tausender-Punkte in der Zahl-Darstellung sollen ignoriert werden.
#   d) Es soll eine (ggf. auch längere) Dezimalzahl in einen Text umgewandelt werden, z. B. wird
#      „123,456“ zu „einhundertdreiundzwanzigkommavierfünfsechs“.
#   Für diese Aufgabe darf selbstverständlich „Pseudo-Code“ verwendet werden: „Wenn Ziffer=2, dann
#   hänge an Ausgabe „zwei“ an.“ bzw. „Wenn Ziffer=2, dann Ausgabe ← Ausgabe+„zwei“ “ usw
#   Wenn du programmieren kannst, kannst du das jeweilige Teil-Problem anschließend auch in einem
#   Programm umsetzen.
#   Eigentlich fehlt noch ein Aufgabenteil e): Eine IP-Adresse wie z. B. „10.51.168.2“ sollte ebenfalls
#   korrekt ausgegeben werden...
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
    input_digit = input("If yo want to exit the Programm just Typ in exit and the Programm will end.\nPlease enter an Number: ")
    if input_digit == "exit":
        quit()

    if len(input_digit) > 18:    # you could easy expand the limit by adding more to the len_number_dictionary
        print("enter was to long.")
        check_and_get_input()
    else:
        number_typ = NumbersTransform()
        if input_digit.find(",") != -1 or input_digit.find(".") != -1:
            if len(re.findall("\.", input_digit)) == 3:
                number_typ.set_typ("ip address")
                number_typ.run(input_digit)
            elif len(re.findall(",", input_digit)) == 1:
                number_typ.set_typ("decimal")
                number_typ.run(input_digit)
            elif len(re.findall("\.", input_digit)) == 1:
                number_typ.set_typ("decimal")
                number_typ.run(input_digit)
            else:
                print("invalid input")
                check_and_get_input()

        else:
            number_typ.set_typ("whole")
            number_typ.run(input_digit)


class NumbersTransform:
    def __init__(self):
        self.interim_result = []
        self.op = Operations()
        self.whole_number_result = ""
        self.result = None
        self.typ = None
        self.len = None

    @staticmethod
    def reform(number, i):
        number = list(number)
        for i in range(i):
            del number[0]
        return "".join(number)

    def set_typ(self, typ):
        self.typ = typ

    def run(self, number):
        if self.typ == "whole":
            self.len = len(number)
            self.whole_numbers(number)
            print("result: " + self.whole_number_result + "\n")
        elif self.typ == "decimal":
            self.len = len(number)
            self.decimal_numbers(number)
            print("result: " + self.result + "\n")
        elif self.typ == "ip address":
            self.ip_address(number)
            print("result: " + self.result + "\n")
        check_and_get_input()

    def whole_numbers(self, number):
        if len(number) == 1:
            one_diget_number = self.op.single_digits(number)
            number = self.reform(number, 1)
            if one_diget_number == "ein":
                one_diget_number += "s"
            if self.len > 1 and one_diget_number == "null":
                pass
            else:
                self.interim_result.append(one_diget_number)
            self.whole_numbers(number)

        elif len(number) == 2:
            two_diget_number = self.op.two_diget_check(number)
            number = self.reform(number, 2)
            if two_diget_number == "ein":
                two_diget_number += "s"
            if self.len > 1 and two_diget_number == "null":
                pass
            else:
                self.interim_result.append(two_diget_number)
            self.whole_numbers(number)

        elif len(number) in range(3, 19):
            longer_diget_number, i = self.op.longer_numbers(number)
            number = self.reform(number, i)
            if longer_diget_number.find("null") == -1:
                self.interim_result.append(longer_diget_number)
            self.whole_numbers(number)

        else:
            result = "".join(self.interim_result)
            self.whole_number_result = result

    def decimal_numbers(self, number):
        if number.find(",") != -1:
            number_split = number.split(",")
        else:
            number_split = number.split(".")
        self.whole_numbers(number_split[0])
        decimal_place = number_split[1]
        decimal_place_result = self.singel_diget_read_out(decimal_place)
        self.result = self.whole_number_result + " komma " + decimal_place_result

    def ip_address(self, number):
        number_split = number.split(".")
        first_number = number_split[0]
        secound_number = number_split[1]
        third_number = number_split[2]
        fourth_number = number_split[3]
        first_number = self.singel_diget_read_out(first_number)
        secound_number = self.singel_diget_read_out(secound_number)
        third_number = self.singel_diget_read_out(third_number)
        fourth_number = self.singel_diget_read_out(fourth_number)
        self.result = first_number + " dot " + secound_number + " dot " + third_number + " dot " + fourth_number

    def singel_diget_read_out(self, number):
        number_result = []
        for i in number:
            interim_result = self.op.single_digits(i)
            if interim_result == "ein":
                interim_result += "s"
            number_result.append(interim_result)
        return "".join(number_result)


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
                singel_digit_num = self.single_digits(number[0])
                len_num = len_number_dictionary[str(len(number))]
                if singel_digit_num == "ein":
                    singel_digit_num += "e"
                return singel_digit_num + len_num, 1

        elif len(number) % 3 == 2:
            if number[0] == "1" and len(number) > 6:
                return self.two_diget_check(number[0]+number[1]) + len_number_dictionary[str(len(number) - 1)], 1

            else:
                return self.two_diget_check(number[0]+number[1]) + len_number_dictionary[str(len(number)-1)], 2


check_and_get_input()
