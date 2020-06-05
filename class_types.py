# this file to describe the bard class

import character as pt
import dice

caster_spell_slots = {1: [2],
                      2: [3],
                      3: [4, 2],
                      4: [4, 3],
                      5: [4, 3, 2],
                      6: [4, 3, 3],
                      7: [4, 3, 3, 1],
                      8: [4, 3, 3, 2],
                      9: [4, 3, 3, 3, 1],
                      10: [4, 3, 3, 3, 2],
                      11: [4, 3, 3, 3, 2, 1],
                      12: [4, 3, 3, 3, 2, 1],
                      13: [4, 3, 3, 3, 2, 1, 1],
                      14: [4, 3, 3, 3, 2, 1, 1],
                      15: [4, 3, 3, 3, 2, 1, 1, 1],
                      16: [4, 3, 3, 3, 2, 1, 1, 1],
                      17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
                      18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
                      19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
                      20: [4, 3, 3, 3, 3, 2, 2, 1, 1]
                      }


class Bard(pt.Character):
    def __init__(self, name):
        pt.Character.__init__(self, name,
                              class_type="Bard",
                              hitdice=dice.d8(),
                              prof_saves={'dex': 1, 'cha': 1},
                              non_prof_mod=0.5,
                              cantrips_by_lvl={1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4,
                                               12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4},
                              spells_by_lvl=caster_spell_slots,
                              spells_slots={1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 14, 11: 15,
                                            12: 15, 13: 16, 14: 18, 15: 19, 16: 19, 17: 20, 18: 22, 19: 22, 20: 22})


class Sorcerer(pt.Character):
    def __init__(self, name):
        pt.Character.__init__(self, name,
                              class_type="Sorcerer",
                              hitdice=dice.d6(),
                              prof_save={'con': 1, 'cha': 1},
                              cantrips_by_lvl={1: 3, 2: 3, 3: 3, 4: 4, 5: 5, 6: 4, 7: 4, 8: 4, 9: 4, 10: 5, 11: 5,
                                               12: 5, 13: 5, 14: 5, 15: 5, 16: 5, 17: 5, 18: 5, 19: 5, 20: 5},
                              spells_by_lvl=caster_spell_slots,
                              spells_slots={1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12,
                                            12: 12, 13: 13, 14: 13, 15: 14, 16: 14, 17: 15, 18: 15, 19: 15, 20: 15})


class Wizard(pt.Character):
    def __init__(self, name):
        pt.Character.__init__(self, name,
                              class_type="Wizard",
                              hitdice=dice.d6(),
                              prof_saves={'int': 1, 'wis': 1})


class Barbarian(pt.Character):
    def __init__(self, name):
        pt.Character.__init__(self, name,
                              class_type="Barbarian",
                              hitdice=dice.d12(),
                              prof_saves={'str': 1, 'con': 1})


class Cleric(pt.Character):
    def __init__(self, name):
        pt.Character.__init__(self, name,
                              class_type="Cleric",
                              hitdice=dice.d8(),
                              prof_saves={'wis': 1, 'cha': 1})


