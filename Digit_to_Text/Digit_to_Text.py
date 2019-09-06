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


result = []

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


def reform(number, i):
    number = list(number)
    for i in range(i):
        del number[0]
    return "".join(number)


def check_and_get_input():
    input_digit = input("Please enter an Number: ")
    if len(input_digit) > 18:
        print("enter was to long.")
        check_and_get_input()

    else:
        typ(input_digit)


def typ(number):
    if len(number) == 1:
        one_diget_number = one_diget(number)
        if one_diget_number == "ein":
            one_diget_number += "s"
        number = reform(number, 1)
        result.append(one_diget_number)
        typ(number)

    elif len(number) == 2:
        two_diget_number = two_diget_check(number)
        number = reform(number, 2)
        if two_diget_number == "ein":
            two_diget_number += "s"
        result.append(two_diget_number)
        typ(number)

    elif len(number) in range(3, 19):
        longer_diget_number, i = longer_diget(number)
        number = reform(number, i)
        if longer_diget_number != "null":
            result.append(longer_diget_number)
        typ(number)

    else:
        print("result: ")


def one_diget(number):
    return one_diget_dictionary[number]


def two_diget_check(number):
    if number[0] == "0":
        return one_diget(number[1])

    elif number[0] == "1":
        if number[1] in str(range(2)):
            return two_diget_exeptions_dictionary[number]
        else:
            return two_diget(number)

    elif number[0] > "1":
        return two_diget(number)


def two_diget(number):
    if number[0] in str(range(1, 2)):
        return one_diget(number[1]) + "und" + two_diget_exeptions_dictionary[number[0]]
    else:
        return one_diget(number[1]) + "und" + one_diget(number[0]) + "zig"


def longer_diget(number):
    if len(number) % 3 == 0:
        if len(number) > 3:
            return one_diget(number[0]) + len_number_dictionary[str(len(number)-3*(len(number)//3-1))], 1

        else:
            if number[0] == "0":
                return "null", 1
            else:
                return one_diget(number[0]) + len_number_dictionary[str(len(number))], 1

    elif len(number) % 3 == 1:
        if number[0] == "0":
            return "null", 1
        else:
            return one_diget(number[0]) + len_number_dictionary[str(len(number))], 1

    elif len(number) % 3 == 2:
        if number[0] == "1" and len(number) > 6:
            return one_diget(number[0]) + len_number_dictionary[str(len(number)-1)], 1

        else:
            return two_diget_check(number[0]+number[1]) + len_number_dictionary[str(len(number)-1)], 2


check_and_get_input()

result = "".join(result)
print(result)
