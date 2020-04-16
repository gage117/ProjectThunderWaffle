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
