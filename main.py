from os import system, name as os_name

# GLOBAL VARIABLES

# conditions = {

# }
# spells = {

# }
weapons = {
  'Wooden Staff': {
    'weapon_id': 1,
    'name': 'Wooden Staff',
    'damage': 3
  },
  'Iron Broad Sword': {
    'weapon_id': 2,
    'name': 'Iron Broad Sword',
    'damage': 6
  },
  'Iron Dagger': {
    'weapon_id': 3,
    'name': 'Iron Dagger',
    'damage': 5

  },
  'Old Bow': {
    'weapon_id': 4,
    'name': 'Old Bow',
    'damage': 4
  }
}
classes = {
  'Wizard': {
    'class_id': 1,
    'class_name': 'Wizard',
    'default_weapon': weapons.get('Wooden Staff')
  },
  'Warrior': {
    'class_id': 2,
    'class_name': 'Warrior',
    'default_weapon': weapons.get('Iron Broad Sword')
  },
  'Ranger': {
    'class_id': 3,
    'class_name': 'Ranger',
    'default_weapon': weapons.get('Old Bow')
  },
  'Rogue': {
    'class_id': 4,
    'class_name': 'Rogue',
    'default_weapon': weapons.get('Iron Dagger')
  }
}
user = {
  'user_name': None,
  'user_class': None,
  'user_weapon': None
}

### Clears the console
def clear():
  if os_name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

#########################################################

# START OF GAME
### Game title'
clear()
print('Welcome to Project Thunderwaffle\n')
user['user_name'] = input('Enter your character name: ')
# Not an empty string
# Not all spaces
# First Char not a space
while user['user_name'] == '' or user.get('user_name')[0] == ' ' or user['user_name'].count(' ') == len(user['user_name']):
  print('Cannot be empty string, start with a space, or be all spaces')
  user['user_name'] = input('Enter your character name: ')

# Pick Class
clear()
print('Please pick your class: ')
for item in classes:
  print(' > %s' % (classes[item]['class_name']))
user_input = input('\nType a choice from above: ').title()
while user_input not in classes:
  print('Please pick from one of the provided choices.')
  print('Please pick your class: ')
  for item in classes:
    print('> %s' % (classes[item]['class_name']))
  user_input = input('\nType a choice from above: ').title()
if user_input in classes:
  user['user_class'] = classes[user_input]
user['user_weapon'] = user.get('user_class')['default_weapon']

# Greeting
clear()
print("Welcome to the land of Thunder Waffle, %s the %s. You've come searching coin with your trusty %s" % (user.get('user_name'), user.get('user_class')['class_name'], user.get('user_weapon')['name']))

# Gage's Change