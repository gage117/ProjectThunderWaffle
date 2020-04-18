from modules.classes import User
from modules.enemies import enemies
from modules.dictionaries import armors, weapons, professions, modifyText

user = User('combat-test', 1, professions['Wizard'], weapons['Wooden Staff'], armors['Linen Robes'])
bandit = enemies['Bandit']
print(modifyText(7, 'bold'))
# user.printAllInfo()
# bandit.printAllInfo()