from modules.functions import clear, wait_for_read, clear_and_wait
from modules.classes import User
from modules.enemies import enemies
from modules.dictionaries import armors, weapons, professions
from modules.color import modifyText

user = User('combat-test', 1, professions['Wizard'], weapons['Wooden Staff'], armors['Linen Robes'])
bandit = enemies['Bandit']
user.printCombatInfo()
bandit.printAllInfo()

class Combat:
  def __init__(self, enemies):
    self.enemies = enemies if isinstance(enemies, list) or isinstance(enemies, tuple) else [enemies]
    self.total_dead = 0
  # Enter Combat
  def enter(self):
    ### Create Prompt String e.g.:'You've entered combat with 2 Wolves, 1 Bandit and 1 Bandit Leader!'
    enter_combat_str = ''
    if len(self.enemies) == 1:
      enter_combat_str = 'a %s' % (modifyText(self.enemies[0].name, 'red'))
    elif len(self.enemies) > 1:
      enemy_amounts = {}
      for enemy in self.enemies:
        if enemy.name not in enemy_amounts:
          enemy_amounts[enemy.name] = 1
        elif enemy.name in enemy_amounts:
          enemy_amounts[enemy.name] += 1
      counter = 1
      for amount in enemy_amounts:
        if counter < len(enemy_amounts):
          enter_combat_str += "%d %s, " % (enemy_amounts[amount], modifyText(enemies[amount].name, 'red') if enemy_amounts[amount] == 1 else modifyText(enemies[amount].plural_name, 'red'))
          counter += 1
        else:
          enter_combat_str += "and %d %s" % (enemy_amounts[amount], modifyText(enemies[amount].name, 'red') if enemy_amounts[amount] == 1 else modifyText(enemies[amount].plural_name, 'red'))
    wait_for_read("You've entered combat with %s!" % (enter_combat_str))
    ### Execute start
    self.next_stage()
  def next_stage(self):
    print('Executing Encounter...')
    

  ###
  ### if total_dead == len(enemies), end combat


## Make encounter
banditEncounter = Combat([enemies['Bandit'], enemies['Wolf']])

testEncounter = Combat(enemies['Bandit'])

## Execute encounter
# print(testEncounter.enemies[0].name)
banditEncounter.enter()