from modules.classes import Weapon, Armor, Profession

# DICTIONARIES
color = {
   'PURPLE': '\033[95m',
   'CYAN': '\033[96m',
   'DARKCYAN': '\033[36m',
   'BLUE': '\033[94m',
   'GREEN': '\033[92m',
   'YELLOW': '\033[93m',
   'RED': '\033[91m',
   'BOLD': '\033[1m',
   'UNDERLINE': '\033[4m',
   'END': '\033[0m'
}
def modifyText(text, modifier):
  return color[modifier.upper()] + str(text) + color['END']
  
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