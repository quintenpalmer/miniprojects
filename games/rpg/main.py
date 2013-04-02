#!/usr/bin/env python

red=0
yellow=1
blue=2
orange=3
green=4
purple=5

class Slot:
	def __init__(self,stype):
		self.stype = stype
		self.gem = None
	def accept(gem):
		if self.gem == None:
			self.gem = gem
	def destroy():
		self.gem = None

class Item:
	def __init__(self,name):
		self.size = 1
		self.value = 0
		self.name = name
	def is_weapon(self):
		return False

class Bag(Item):
	def __init__(self,name="Simple_Satchel",capacity=5):
		Item.__init__(self,name)
		self.pockets = [None for x in range(capacity)]
		self.capacity = capacity
	def add(self,item):
		for i in range(len(self.pockets)):
			if self.pockets[i] == None:
				self.pockets[i] = item
				self.capacity -= 1
				break
	def remove(self,index):
		to_remove = self.pockets[index]
		self.pockets[index] = None
		self.capacity += 1
		return to_remove
	def has_room(self):
		return self.capacity > 0
	def to_string(self):
		return self.pockets

class Armor(Item):
	def __init__(self,name,slots=[],armor_value=1):
		Item.__init__(self,name)
		self.slots = []
		for slot in slots:
			self.slots.append(Slot(slot))
		self.armor_value=armor_value

class Tunic(Armor):
	def __init__(self,name,slots=[],armor_value=1):
		Armor.__init__(self,name,slots=slots,armor_value=armor_value)

class Weapon(Item):
	def __init__(self,name,slots=[],damage=1):
		Item.__init__(self,name)
		self.slots = []
		for slot in slots:
			self.slots.append(Slot(slot))
		self.damage=damage
	def is_weapon(self):
		return True

class Empty_Hand(Weapon):
	def __init__(self,name,damage=1):
		Weapon.__init__(self,name,damage=damage)

class Sword(Weapon):
	def __init__(self,name,slots=[],damage=1):
		Weapon.__init__(self,name,slots=slots,damage=damage)

class Player:
	def __init__(self,name):
		self.name = name
		self.health = 10
		self.magic = 10
		self.strength = 10
		self.left_hand_weapon = Empty_Hand('Fist',damage=self.strength)
		self.right_hand_weapon = Empty_Hand('Fist',damage=self.strength)
		self.armor = Tunic('Snazzy_Green_Tunic')
		self.inventory = Bag(name="Small_Satchel",capacity=5)
	def equip_left_hand(self,weapon=None):
		self.equip_to_hand(weapon,self.left_hand_weapon)
	def equip_right_hand(self,weapon=None):
		self.equip_to_hand(weapon,self.right_hand_weapon)
	def equip_to_hand(self,weapon,hand_weapon):
		if weapon == None:
			if hand_weapon.is_item():
				if self.inventory.has_room():
					self.inventory.add(hand_weapon)
				else:
					raise Exception("No room in inventory")
			else:
				raise Exception("No item is equiped")
		else:
			weapon = self.inventory.remove(weapon)
			if weapon.is_weapon():
				hand_weapon = weapon
			else:
				raise Exception("Only weapons can be equipped to hands")

q = Player('Quin')
print q.name,q.left_hand_weapon.damage
print q.inventory.to_string()
q.inventory.add(Sword(name="Rodent Poker",damage=5))
print q.inventory.to_string()
q.equip_left_hand(weapon=0)
print q.inventory.to_string()
