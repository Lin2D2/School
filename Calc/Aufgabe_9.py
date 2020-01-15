import re
from termcolor import colored  # pip install termcolor


class IsIBAN_Valid():
    def __init__(self):
        self.IBAN = None
        self.str_R = None
        self.int_CS = None
        self.int_BZ = None
        self.int_KN = None

    def get_IBAN(self):
        valid = False
        while not valid:
            str_input_IBAN = input("gebe eine Kontonummer ein: ")
            str_input_IBAN = "".join(re.split(" ", str_input_IBAN))
            
            if len(str_input_IBAN) == 22:
                self.IBAN = "".join(colored(str_input_IBAN[:2], "green") +
                                    colored(str_input_IBAN[2:4], "cyan")) + " " + \
                            "".join(colored(str_input_IBAN[4:8], "magenta")) + " " + \
                            "".join(colored(str_input_IBAN[8:12], "magenta")) + " " + \
                            "".join(colored(str_input_IBAN[12:16], "blue")) + " " + \
                            "".join(colored(str_input_IBAN[16:20], "blue")) + " " + \
                            "".join(colored(str_input_IBAN[20:22], "blue"))
                try:
                    self.str_R = str_input_IBAN[:2]
                    self.int_CS = int(str_input_IBAN[2:4])
                    self.int_BZ = int(str_input_IBAN[4:12])
                    self.int_KN = int(str_input_IBAN[12:22])
                    valid = True

                except ValueError:
                    str_failure = [colored(str_input_IBAN[:2], "green")]
                    for e in str_input_IBAN[2:]:
                        if not e.isdigit():
                            str_failure.append(colored(e, "red"))
                        else:
                            str_failure.append(colored(e, "blue"))
                    str_failure = "".join(str_failure)

                    print("The entert IBAN: " +
                          str_failure +
                          "\n was incorrect please check if you entert the right one.")

            else:
                print("the entered IBAN was " + str(len(str_input_IBAN)) + "but it has to be 22 long.")

        print("\n" +
              "--" * 26 +
              "\n" +
              "The entered IBAN was " + self.IBAN + ".\n" +
              "--" * 9 + "-Checking IBAN" + "--" * 10 +
              "\n"
              )

    def check_correct(self):
        int_mod_IBAN = int(str(self.int_BZ) +
                           str(0) * (10 - len(str(self.int_KN))) + str(self.int_KN) +
                           str(1314) +
                           str(self.int_CS)) \
                       % 97
        if int_mod_IBAN == 1 and self.int_CS in range(2, 98):
            print("The IBAN is " + colored("correct", "red") + ".")
        elif not int_mod_IBAN == 1 and self.int_CS in range(2, 98):
            print("The IBAN is " + colored("not correct", "red") + ", the sum is not 1, but: " + str(int_mod_IBAN))
        elif int_mod_IBAN == 1 and self.int_CS not in range(2, 98):
            print("The IBAN's Check sum is " + colored("out of Range", "red") +
                  " of 2 to 98, instead it's: " + str(self.int_CS))
        elif not int_mod_IBAN == 1 and self.int_CS not in range(2, 98):
            print("The IBAN is " + colored("not correct", "red") + ", the sum is not 1, but: " +
                  str(int_mod_IBAN) +
                  "\nand The IBAN's Check sum is " + colored("out of Range", "red") +
                  " of 2 to 98,"
                  "\ninstead it's: " + str(self.int_CS))
        print("\n" +
              "--" * 11 + "-Done-" + "--" * 13)


isIBAN = IsIBAN_Valid()
isIBAN.get_IBAN()
isIBAN.check_correct()
