from os import system, name as os_name
from modules.dictionaries import armors, weapons, professions
from modules.classes import User

# GLOBAL VARIABLES

# conditions = {

# }
# spells = {

# }


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

def clear_and_wait(what_to_print):
  clear()
  wait_for_read(what_to_print)

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
clear_and_wait("""After arriving at a town called Ghimori, you've been staying at a local inn. On your third morning there, you wake to a knock at your door...

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
  wait_for_read("What sort of pushover do you take me for? I'm sick of adventurers thinking they can short me! Looks like I'll have to get the rest from selling that nice %s." % (user.weapon.name))
clear_and_wait("***Some sort of transition text from the conversation to the combat***")