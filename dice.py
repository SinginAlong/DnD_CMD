# for defining dice

import random

# prototype dice
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, adv=False, dis=False):
        if adv:
            r = max(random.randint(1, self.sides), random.randint(1, self.sides))
        elif dis:
            r =  min(random.randint(1, self.sides), random.randint(1, self.sides))
        else:
            r =  random.randint(1, self.sides)
        if r == 20:
            print("Nat 20!")
        return r


    def roll_indiv(self, number_of_dice):
        r = list()
        for n in range(0, number_of_dice):
            r = r + [self.roll()]
        return r

    def roll_sum(self, number_of_dice):
        return(sum(self.roll_indiv(number_of_dice)))

    def stat_roll(self):
        # roll 4d6, drop the lowest, sum the rest
        d = self.roll_indiv(4)
        d.sort()
        return(sum(d[1:]))

    def decode_dice(self, dice):
        # XdYY
        # where X is an integer from 1 to almost infinity
        # YY is the dice type from 2, 4, 6, 8, 10, 12, 20
        pass


class d4(Dice):
    def __init__(self):
        Dice.__init__(self, 4)


class d6(Dice):
    def __init__(self):
        Dice.__init__(self, 6)


class d8(Dice):
    def __init__(self):
        Dice.__init__(self, 8)


class d10(Dice):
    def __init__(self):
        Dice.__init__(self, 10)


class d12(Dice):
    def __init__(self):
        Dice.__init__(self, 12)


class d20(Dice):
    def __init__(self):
        Dice.__init__(self, 20)