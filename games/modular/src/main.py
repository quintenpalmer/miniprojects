from model.Model import Model
from control.Control import Control
from view.View import View

model = Model()
print model.ship.health
print model.enemy.health
model.ship.attack(0,model.enemy)
print model.ship.health
print model.enemy.health
