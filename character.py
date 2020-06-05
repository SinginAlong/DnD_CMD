# using dnd character classes to practice python classes and (more importantly) class inheritance

# nomenclature
# ability: str, dex, con, int, wis, cha
# score is the raw value, so for ability modifier the ability score runs from 1 to 20
# modifier (mod) is the 'plus value' you add to skill checks or saving throws or whatnot
# prof = proficiency (mostly because I can't spell proficiency)

import dice

abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']

skills = {
    'acrobatics': 'dex',
    'animal handling': 'wis',
    'arcana': 'int',
    'athletics': 'str',
    'deception': 'cha',
    'history': 'int',
    'insight': 'wis',
    'intimidation': 'cha',
    'investigation': 'int',
    'medicine': 'wis',
    'nature': 'int',
    'perception': 'wis',
    'performance': 'cha',
    'persuasion': 'cha',
    'religion': 'int',
    'slight of hand': 'dex',
    'stealth': 'dex',
    'survival': 'wis',
}

prof_by_lvl = {  # input level, output proficiency bonus
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 3,  # change
    6: 3,
    7: 3,
    8: 3,
    9: 4,   # change
    10: 4,
    11: 4,
    12: 4,
    13: 5,  # change
    14: 5,
    15: 5,
    16: 5,
    17: 6,  # change
    18: 6,
    19: 6,
    20: 6,
}


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        self.level = kwargs.get('level', None)
        self.class_type = kwargs.get('class_type', None)
        self.hp = kwargs.get('hp', None)
        self.race = kwargs.get('race', None)
        self.alignment = kwargs.get('alignment', None)
        self.ac = kwargs.get('ac', None)  # armor class
        self.ab_scores = kwargs.get('ability_scores', None)
        self.ab_mods = kwargs.get('ability_modifiers', None)
        self.hitdice = kwargs.get('hitdice', None)
        self.proficiency = kwargs.get('proficiency', None)
        self.non_prof_mod = kwargs.get('non_prof_mod', 0)
        self.armor = kwargs.get('armor', None)
        self.speed = kwargs.get('speed', None)
        self.prof_skills = kwargs.get('prof_skills', None)  # proficient skills and the # of prof bonuses that are added
        self.prof_saves = kwargs.get('prof_saves', None)  # proficient saves and the # of prof bonuses that are added
        self.skill_mods = kwargs.get('skill_mods', None)
        self.save_mods = kwargs.get('save_mods', None)  # the saving throw modifiers
        self.cantrips_by_lvl = kwargs.get('cantrips_by_lvl', None)
        self.spells_by_lvl = kwargs.get('spells_by_lvl', None)
        self.cantrips_known = kwargs.get('spells_known', None)
        self.spells_slots = kwargs.get('spells_known', None)
        self.spells = kwargs.get('spells', None)
        self.cantrips = kwargs.get('cantrips', None)
        self.prof_by_lvl  = kwargs.get('prof_by_lvl', prof_by_lvl)

        self.init_ab_mods()  # move this

    # housekeeping methods
    @staticmethod
    def score_to_mod(score):
        if score >= 10:
            return int((score-10)/2)
        else:
            return int((score-11)/2)

    def calc_ab_mods(self):
        if self.ab_mods is None:
            self.init_ab_mods()
        if self.ab_scores is None:
            print(f"Can't calculate ability modifiers because abilities have not been set")
            return False
        if any([v is None for v in self.ab_scores.values()]):
            print(f"ability scores are not set, can't calculate ability modifiers")
            return False
        for ab, val in self.ab_scores.items():
            self.ab_mods[ab] = Character.score_to_mod(val)  # can static method return value?
        return True

    def calc_saves(self):
        # use abilities modifiers, prof, & saving prof
        if self.save_mods is None:
            self.init_save_mods()
        if self.proficiency is None:
            print("Can't calculate saving throws because proficiency hasn't been set")
            return
        if self.prof_saves is None:
            print("Can't calculate saving throws because proficient saving throws haven't been set")
            return
        if self.ab_mods is None:
            print(f"Can't calculate saving throws because ability modifiers have not be set")
            return
        for ab in abilities:
            if ab in self.prof_saves:
                mod = self.prof_saves[ab] * self.proficiency
            else:
                mod = 0
            self.save_mods[ab] = self.ab_mods[ab] + mod

    def calc_skills(self):
        # use prof bonus, prof skills,
        if self.prof_skills is None:
            print("Can't calculate skill modifiers because proficient skills have not been set")
            return False
        if self.ab_mods is None:
            print(f"Can't calculate skill modifiers because ability modifiers have not be set")
            return False
        if self.skill_mods is None:
            self.init_skill_mods()
        for s in skills:
            if s in self.prof_skills:
                mod = self.prof_skills[s] * self.proficiency
            else:
                mod = int(self.non_prof_mod * self.proficiency)
            self.skill_mods[s] = self.ab_mods[skills[s]] + mod
        return True

    # initializers
    def init_ab_scores(self):
        self.ab_scores = dict()
        self.ab_scores['str'] = None
        self.ab_scores['dex'] = None
        self.ab_scores['con'] = None
        self.ab_scores['int'] = None
        self.ab_scores['wis'] = None
        self.ab_scores['cha'] = None

    def init_ab_mods(self):
        self.ab_mods = dict()
        # check that abscores is defined and that the values in it are set
        if self.ab_scores is None:
            self.init_ab_scores()
        for ab in self.ab_scores.keys():
            self.ab_mods[ab] = None

    def init_prof_skills(self):
        if self.prof_skills is None:
            self.prof_skills = dict()  # set to empty dict - no proficient skills

    def init_prof_saves(self):
        if self.prof_saves is None:
            self.prof_saves = dict()

    def init_skill_mods(self):
        if self.skill_mods is None:
            self.skill_mods = dict()

    def init_save_mods(self):
        if self.save_mods is None:
            self.save_mods = dict()

    # building character, setters
    def roll_stats(self, stat_die):
        print("Stat rolling...")
        for i in range(0,6):
            print(f"Roll {i+1}: {stat_die.stat_roll()}")

    def set_ab_score(self, ability, value):
        if self.ab_scores is None:
            self.init_ab_scores()
        if ability not in self.ab_scores:
            print(f"error: {ability} is not an ability score")
            print(f"set an ability from this list: {self.ab_scores.keys()}")
            return
        if value > 20:
            print("ability scores can't be greater than 20")
            return
        if value < 0:
            print("you were gonna assign that to int right?  Try a non-negative number")
            return
        self.ab_scores[ability] = value

    def set_level(self, lvl):
        if lvl < 1 or lvl > 20:
            print(f'Level must be between 1 and 20')
            return
        self.level = lvl
        if self.prof_by_lvl is None:
            print(f'Error: Proficiency by level not set')
        else:
            self.proficiency = prof_by_lvl[self.level]

    def set_prof_save(self, ability, prof_mul=1):
        if self.prof_saves is None:
            self.init_prof_saves()
        if ability not in abilities:
            print(f'The input {ability} is not valid.  Please use an ability for the list {abilities}')
            return
        self.prof_saves[ability] = self.proficiency * prof_mul

    def set_prof_skill(self, skill, prof_mul=1):
        if self.prof_skills is None:
            self.init_prof_skills()
        if skill not in skills:
            print(f'The input {skill} is not valid.  Please use a valid skill, list located in characters.py')
            return
        self.prof_skills[skill] = prof_mul

    # things that all characters can do
    def skill_check(self, skill, die=dice.d20(), adv=False, dis=False):
        # takes the skill, checks skill mod for it, rolls with or without advantage
        if self.ab_mods is None:
            print("Ability modifiers haven't been set, trying to calculate those")
            if self.calc_ab_mods() is False:
                return None
        if self.proficiency is None:
            print(f"Proficiency isn't set, set character level which will automatically set proficiency")
            return None
        if self.prof_skills is None:
            print("Can't skill check because proficient skills have not been set")
            return None
        if self.skill_mods is None:
            # if we get this far everything should be good and this can run silently
            if self.calc_skills() is False:
                print("Error: skill mods are not set and could not be automatically set")
                return None
        if skill not in self.skill_mods:
            print(f"{skill} not found in the skill modifiers")
            return None

        if adv:
            return die.roll(adv=True) + self.skill_mods[skill]
        if dis:
            return die.roll(dis=False) + self.skill_mods[skill]
        return die.roll() + self.skill_mods[skill]

    def move(self, distance):
        pass

    def attack(self, weapon, creature):
        # not sure how to handle attacking (and honestly I'm a little bunt out rn)
        pass

    # character description
    def say_name(self):
        print(f"Hail and well met!  I am {self.name}")

    def say_class(self):
        print(f"I am a {self.class_type}")

    def say_ab_mods(self):
        for ab in self.ab_scores.keys():
            print(f'{ab}: {self.ab_mods[ab]} ({self.ab_scores[ab]})')

    def say_skill_mods(self):
        if self.skill_mods is None:
            print("Error: Skill modifiers are not set, trying to automatically calculate them")
            if self.calc_skills() is False:
                print("Couldn't automatically calculate skill mods")
                return
        for s,v in self.skill_mods.items():
            print(f'{s}: {v}')

    def say_save_mods(self):
        if self.save_mods is None:
            print('save modifiers are not set')
            return
        for s,v in self.save_mods.items():
            print(f'{s}: {v}')