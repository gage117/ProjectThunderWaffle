from os import system, name as os_name

# GLOBAL VARIABLES

# conditions = {

# }
# spells = {

# }

# professions
class Weapon:
  def __init__(self, id, name, damage):
    self.id = id
    self.name = name
    self.damage = damage
  def printInfo(self):
    print("""
Weapon Info:
  Name: %s
  Damage: %d
""" % (self.name, self.damage))

default_weapon = Weapon(0, 'None', 0)

class Armor:
  def __init__(self, id, name, category, defense):
    self.id = id
    self.name = name
    self.category = category
    self.defense = defense
  def printInfo(self):
    print("""
Armor Info:
  Name: %s
  Category: %s
  Defense: %d
""" % (self.name, self.category, self.defense))

default_armor = Armor(0, 'None', 'Heavy', 0)

class Profession:
  def __init__(self, id, name, default_weapon):
    self.id = id
    self.name = name
    self.default_weapon = default_weapon
  def printInfo(self):
    print("""
Profession Info:
  Name: %s
  Default Weapon: %s
""" % (self.name, self.default_weapon.name))

default_profession = Profession(0, 'None', default_weapon)

class User:
  def __init__(self, name, profession = default_profession, weapon = default_weapon, armor = default_armor, gold = 10, hp = 20):
    self.name = name 
    self.profession = profession
    self.weapon = weapon
    self.armor = armor
    self.gold = gold
    self.hp = hp
  def printInfo(self):
    print("""
User Info
  Name: %s
  Profession: %s
  Weapon: %s
  Armor: %s
  Gold: %d
  HP: %d
""" % (self.name, self.profession.name, self.weapon.name, self.armor.name, self.gold, self.hp))

# DICTIONARIES
armors = {
  'Linen Robes': Armor(1, 'Linen Robes', 'Light', 5),
  'Leather Armor': Armor(2, 'Leather Armor', 'Medium', 10),
  'Chainmail': Armor(3, 'Chainmail', 'Heavy', 20)
}
weapons = {
  'Wooden Staff': Weapon(1, 'Wooden Staff', 5),
  'Iron Broad Sword': Weapon(2, 'Iron Broad Sword', 10),
  'Iron Dagger': Weapon(3, 'Iron Dagger', 7),
  'Old Bow': Weapon(4, 'Old Bow', 6)
}
professions = {
  'Wizard': Profession(1, 'Wizard', weapons.get('Wooden Staff')),
  'Warrior': Profession(2, 'Warrior', weapons.get('Iron Broad Sword')),
  'Ranger': Profession(3, 'Ranger', weapons.get('Old Bow')),
  'Rogue': Profession(4, 'Rogue', weapons.get('Iron Dagger'))
}
user = User('None')

### Clears the console
def clear():
  if os_name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def wait_for_read(what_to_print):
  print(what_to_print)
  input("> ")
  clear()

#########################################################

# START OF GAME
### Game title'
clear()
print('Welcome to Project Thunderwaffle\n')
name_input = input('Enter your character name: ')
# Not an empty string
# Not all spaces
# First Char not a space
while name_input == '' or name_input[0] == ' ' or name_input.count(' ') == len(name_input):
  print('Cannot be empty string, start with a space, or be all spaces')
  name_input = input('Enter your character name: ')
user.name = name_input

# Pick Profession
clear()
print('Please pick your profession: ')
for item in professions:
  print(' %d) %s' % (professions[item].id, professions[item].name))
user_input = input('\nType a choice or number from above: ').title()
try:
  user_input = int(user_input)
  for item in professions:
    if user_input == professions[item].id:
      user_input = professions[item].name
except:
  pass
finally:
  while user_input not in professions:
    print('\nPlease pick from one of the provided choices.')
    print('Please pick your profession: ')
    for item in professions:
      print(' %d) %s' % (professions[item].id,professions[item].name))
    user_input = input('\nType a choice or number from above: ').title()
  user.profession = professions[user_input]
  user.weapon = user.profession.default_weapon

# Greeting
clear()
wait_for_read("Welcome to the land of Thunder Waffle, %s the %s. You've come searching coin with your trusty %s. So far you have been unfruitful in your search and have had a turn of bad luck." % (user.name, user.profession.name, user.weapon.name))
wait_for_read("""After arriving at a town called Ghimori, you've been staying at a local inn. On your third morning there, you wake to a knock at your door...

Innkeeper: %s! You've been here for days! It's time to pay up!
""" % (user.profession.name))
user_choice = input("""... You owe me 15 gold already! Do you not have any gold?

You currently have %d gold. Pay innkeeper?

1) Yes
2) No

Please type number or choice: """ % (user.gold)).lower()
choices = ('yes', '1', 'no', '2')
while user_choice not in choices:
  print("Invalid Choice")
  user_choice = input("> ")
if user_choice in choices:
  print("What sort of pushover do you take me for? I'm sick of adventurers thinking they can short me! Looks like I'll have to get the rest from selling that nice %s." % (user.weapon.name))
print()