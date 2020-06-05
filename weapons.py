# for declaring and handling weapons

import dice


class Weapon:
    def __init__(self, type, **kwargs):
        self.type = type

        self.cost = kwargs.get('cost', None)  # in gp
        self.damage_type = kwargs.get('damage_type', None)
        self.damage = kwargs.get('damage', None)
        self.weight = kwargs.get('weight', None)  # in lbs
        self.range = kwargs.get('range', None)
        self.dis_range = kwargs.get('dis_range', None)
        self.thrown = kwargs.get('throwable', False)
        self.finesse = kwargs.get('finesse', False)
        self.ammunition = kwargs.get('ammunition', False)
        self.light = kwargs.get('light', False)
        self.heavy = kwargs.get('heavy', False)
        self.two_handed = kwargs.get('two_handed', False)
        self.versatile = kwargs.get('versatile', False)
        self.loading = kwargs.get('loading', False)
        self.reach = kwargs.get('reach', False)
        self.special = kwargs.get('special', False)
        self.ab_mod_type = kwargs.get('ab_mod_type', None)

    def attack(self, am_mod, prof, target_range, **kwargs):
        pass


class Club(Weapon):
    def __init__(self):
        Weapon.__init__("club", cost=0.1, damage_type='bludgeoning', damage=dice.d4, weight=2, light=True)
