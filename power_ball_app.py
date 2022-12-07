
from power_ball_utiles import Winner
from power_ball_utiles import Lucky

class Grade:
    def price(self):
        count = 0
        count2 = 0
        for i in Winner.powerball_number_t:
            for j in Lucky.powerball_number_l:
                if i == j:
                    count += 1
        for a in Winner.whiteball_numbers:
            for b in Lucky.user_numbers:
                if a == b:
                    count2 += 1
        print(count2,"white ball and ",count,"power ball:",end= " ")
        if count2 == 5 and  count == 1 :
            print("jack point $324,000,000")
        elif count2 == 5 and count == 0 :
            print("$1,000,000")
        elif count2 == 4 and count == 1 :
            print("$10,000")
        elif count2 == 4 and count == 0 :
            print("$100")
        elif count2 == 3 and count == 1 :
            print("$100")
        elif count2 == 3 and count == 0 :
            print("$7")
        elif count2 == 2 and count == 1 :
            print("$7")
        elif count2 == 1 and count == 1 :
            print("$4")
        elif count2 == 0 and count == 1 :
            print("$4")
        else:

            print("try again")


h = Grade()
h.price()