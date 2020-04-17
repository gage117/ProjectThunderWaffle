from modules.classes import Weapon, Armor, Profession

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