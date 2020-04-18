from modules.color import modifyText

def c_t(text):  # c_t(cyan_text) Requires execution from parent folder and modifyText from dictionaries.py to be imported
  return modifyText(text, 'cyan')

class Weapon:
  def __init__(self, id, name, damage):
    self.id = id  # int
    self.name = name  # str
    self.damage = damage  # int
  def printInfo(self):
    print("""
Weapon Info:
  Name: %s
  Damage: %s
""" % (c_t(self.name), c_t(self.damage)))

default_weapon = Weapon(0, 'None', 0)

class Armor:
  def __init__(self, id, name, category, defense):
    self.id = id  # int
    self.name = name  # str
    self.category = category  # str
    self.defense = defense  # int
  def printInfo(self):
    print("""
Armor Info:
  Name: %s
  Category: %s
  Defense: %s
""" % (c_t(self.name), c_t(self.category), c_t(self.defense)))

default_armor = Armor(0, 'None', 'Heavy', 0)

class Profession:
  def __init__(self, id, name, default_weapon):
    self.id = id  # int
    self.name = name  # str
    self.default_weapon = default_weapon  # Weapon class
  def printInfo(self):
    print("""
Profession Info:
  Name: %s
  Default Weapon: %s
""" % (c_t(self.name), c_t(self.default_weapon.name)))

default_profession = Profession(0, 'None', default_weapon)

class User:
  def __init__(self, name, level = 1, profession = default_profession, weapon = default_weapon, armor = default_armor, gold = 10, hp = 20):
    self.name = name  # str
    self.level = level  # int
    self.profession = profession  # Profession class
    self.weapon = weapon  # Weapon class
    self.armor = armor  # Armor class
    self.gold = gold  # int
    self.hp = hp  # int
  def printCombatInfo(self):
    print("""
User Info
  Name: %s
  Profession: %s
  Level: %s
  Weapon: %s
    Damage: %s
  Armor: %s
    Defense: %s
  HP: %s
""" % (c_t(self.name), c_t(self.profession.name), c_t(self.level), c_t(self.weapon.name), c_t(self.weapon.damage), c_t(self.armor.name), c_t(self.armor.defense), c_t(self.hp)))
  def printAllInfo(self):
    print("""
User Info
  Name: %s
  Profession: %s
  Level: %s
  Weapon: %s
    Damage: %s
  Armor: %s
    Defense: %s
  Gold: %s
  HP: %s
""" % (c_t(self.name), c_t(self.profession.name), c_t(self.level), c_t(self.weapon.name), c_t(self.weapon.damage), c_t(self.armor.name), c_t(self.armor.defense), c_t(self.hp)))

class Enemy:
  def __init__(self, name, classification, level, hp, damage, defense, loot):
    self.name = name  # str
    self.level = level  # int
    self.classification = classification # str
    self.hp = hp  # int
    self.damage = damage  # int
    self.defense = defense  # int
    self.loot = loot  # list
  def printCombatInfo(self):
    print("""
Enemy Info
  Name: %s
  Classification: %s
  Level: %s
  HP: %s
""" % (c_t(self.name), c_t(self.classification), c_t(self.level), c_t(self.hp)))
  def printAllInfo(self):
    print("""
Enemy Info
  Name: %s
  Classification: %s
  Level: %s
  HP: %s
  Damage: %s
  Defense: %s
""" % (c_t(self.name), c_t(self.classification), c_t(self.level), c_t(self.hp), c_t(self.damage), c_t(self.defense)))