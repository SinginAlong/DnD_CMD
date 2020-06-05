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

Drat.set_ab_score("str", d6.stat_roll())
Drat.set_ab_score("dex", d6.stat_roll())
Drat.set_ab_score("con", d6.stat_roll())
Drat.set_ab_score("int", d6.stat_roll())
Drat.set_ab_score("wis", d6.stat_roll())
Drat.set_ab_score("cha", d6.stat_roll())

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
