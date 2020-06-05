# this file use do define armor prototype add specific armor items


class Armor:
    def __init__(self, type, **kwargs):
        self.type = type

        self.cost = kwargs.get('cost', None)  # in gold pieces (until I make a money class)
        self.base_ac = kwargs.get('base_ac', None)
        self.weight = kwargs.get('weight', None)  # in lbs
        self.str_min_score = kwargs.get('str_min', None)  # in ab score, not ab mod
        self.max_mod = kwargs.get('max_mod', None)  # sets max additional from modifier

        self.mod_type = kwargs.get('mod_type', 'dex')
        self.stealth_dis_adv = kwargs.get('stealth_dis_adv', False)

    def calc_ac(self, abmods):
        if self.max_mod is None:
            mod = abmods[self.mod_type]
        elif abmods[self.mod_type] > self.max_mod:
            mod = self.max_mod
        else:
            mod = abmods[self.mod_type]

        return self.base_ac + mod

class Padded(Armor):
    def __init__(self):
        Armor.__init__(self, 'Padded', cost=5, base_ac=11, weight=8, stealth_dis_adv=True)


class Leather(Armor):
    def __init__(self):
        Armor.__init__(self, 'Leather', cost=10, base_ac=11, weight=10)


class StuddedLeather(Armor):
    def __init__(self):
        Armor.__init__(self, 'Studded leather', cost=45, base_ac=12, weight=13)


class Hide(Armor):
    def __init__(self):
        Armor.__init__(self, 'Hide', cost=10, base_ac=12, max_mod=2, weight=12)


class ChainShirt(Armor):
    def __init__(self):
        Armor.__init__(self, 'Chain shirt', cost=50, base_ac=13, max_mod=2, weight=20)


class ScaleMail(Armor):
    def __init__(self):
        Armor.__init__(self, 'Scale mail', cost=50, base_ac=14, max_mod=2, weight=45, stealth_dis_adv=True)


class Breastplate(Armor):
    def __init__(self):
        Armor.__init__(self, 'Breastplate', cost=400, base_ac=14, max_mod=2, weight=20)


class HalfPlate(Armor):
    def __init__(self):
        Armor.__init__(self, 'Half plate', cost=750, base_ac=15, max_mod=2, weight=40, stealth_dis_adv=True)


class RingMail(Armor):
    def __init__(self):
        Armor.__init__(self, "Ring mail", cost=30, base_ac=14, max_mod=0, weight=40, stealth_dis_adv=True)


class ChainMail(Armor):
    def __init__(self):
        Armor.__init__(self, "Chain mail", cost=75, base_ac=16, max_mod=0, weight=55, str_min_score=13, stealth_dis_adv=True)


class Splint(Armor):
    def __init__(self):
        Armor.__init__(self, "Splint", cost=200, base_ac=17, max_mod=0, weight=60, str_min_score=15, stealth_dis_adv=True)


class Plate(Armor):
    def __init__(self):
        Armor.__init__(self, "Plate", cost=1500, base_ac=18, max_mod=0, weight=65, str_min_sccore=15, stealth_dis_adv=True)

