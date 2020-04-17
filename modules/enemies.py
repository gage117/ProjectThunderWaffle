from modules.classes import Enemy
import random

commonality_choices = ('common', 'rare', 'epic', 'legendary')

def loot_generator(loot_level, commonality):
  if loot_level > 0 and loot_level <= 3:
    if commonality == commonality_choices[0]:  # common
      return {
        'gold': random.randint(3, 7)  # generates random integer from 3 to 7
      }

enemies = {
  'Bandit': Enemy('Bandit', 'Humanoid', 1, 10, 3, 5, loot_generator(1, 'common')),
  'Bandit Leader': Enemy('Bandit Leader', 'Humanoid', 2, 12, 4, 5, loot_generator(2, 'common')),
  'Wolf': Enemy('Wolf', 'Beast', 2, 12, 4, 4, loot_generator(2, 'common')),
}


# It runs this if it's not commented out but imported elsewhere

# for enemy in enemies:
#   enemies[enemy].printAllInfo()