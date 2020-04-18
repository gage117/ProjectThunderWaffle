from modules.classes import User
from modules.enemies import enemies
from modules.dictionaries import armors, weapons, professions
from modules.color import modifyText

user = User('combat-test', 1, professions['Wizard'], weapons['Wooden Staff'], armors['Linen Robes'])
bandit = enemies['Bandit']
user.printCombatInfo()
bandit.printAllInfo()