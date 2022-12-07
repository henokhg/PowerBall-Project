import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)
class Winner:
    powerball_number_t = []
    for i in range(1):
        p_number = random.randint(1, 10)
        powerball_number_t.append(p_number)


    whiteball_numbers = []

    for i in range(0, 5):
        w_number = random.randint(1, 20)
        whiteball_numbers.append(w_number)
    whiteball_numbers.sort()

    print(" Today's powerball winning numbers: ")
    print(Fore.LIGHTMAGENTA_EX + str(whiteball_numbers), Fore.YELLOW + str(powerball_number_t))
class Lucky:
    powerball_number_l = []
    for i in range(1):
        p_number = random.randint(1, 10)
        powerball_number_l.append(p_number)


    user_numbers = []
    for i in range(0, 5):
        u_number = random.randint(1, 20)
        user_numbers.append(u_number)
        user_numbers.sort()

    print(" Your lucky numbers: ")
    print(Fore.LIGHTMAGENTA_EX+ str(user_numbers),Fore.YELLOW+ str(powerball_number_l))