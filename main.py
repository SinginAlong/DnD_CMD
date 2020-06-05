# using dnd character classes to practice python classes and (more importantly) class inheritance

# not sure what main will be used for, lol


import dice
import class_types
import armor

# testing Dice
d4 = dice.d4()
d6 = dice.d6()
d8 = dice.d8()
d10 = dice.d10()
d12 = dice.d12()
d20 = dice.d20()
"""
print(f"Rolling d4: {d4.roll()}")
print(f"Rolling d4: {d4.roll()}")
print(f"Rolling d4: {d4.roll()}")

print(f"Rolling d6: {d6.roll()}")
print(f"Rolling d8: {d8.roll()}")
print(f"Rolling d20: {d20.roll()}")

print(f"Rolling 4d6, indiv: {d6.roll_indiv(4)}")
print(f"Rolling 6d8, summed: {d8.roll_sum(4)}")
"""

Drat = class_types.Bard("Drat of Hithendale")

Drat.say_name()
Drat.say_class()
# Drat.roll_stats(d6)

Drat.set_ab_score("str", 19)
Drat.set_ab_score("dex", 16)
Drat.set_ab_score("con", 20)
Drat.set_ab_score("int", 10)
Drat.set_ab_score("wis", 12)
Drat.set_ab_score("cha", 18)

Drat.calc_ab_mods()
Drat.say_ab_mods()

'''
Scale = armor.ScaleMail()
print(f'AC for Dratt wearing scale mail is {Scale.calc_ac(Drat.ab_mods)}')
Plate = armor.Plate()
print(f'AC for Dratt wearing Plate is {Plate.calc_ac(Drat.ab_mods)}')
StLeat = armor.StuddedLeather()
print(f'AC for Dratt wearing Studded Leather is {StLeat.calc_ac(Drat.ab_mods)}')
'''

Drat.set_level(8)

Drat.calc_saves()

print(f'My saving throws are: ')
Drat.say_save_mods()


Drat.set_prof_skill('persuasion', 2)
Drat.set_prof_skill('perception', 2)
Drat.set_prof_skill('deception')
Drat.set_prof_skill('intimidation')

Drat.say_skill_mods()

print(Drat.skill_check('medicine', d20))
print(Drat.skill_check('deception'))
print(Drat.skill_check('persuasion'))
print(f"Rolling for acrobatics: {Drat.skill_check('acrobatics')}")
print(f"Rolling for animal handling: {Drat.skill_check('animal handling')}")