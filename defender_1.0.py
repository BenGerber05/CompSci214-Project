import stddraw
import stdio
import sys
import random
import math

#custom classes

#==========================================================

            """PLAYER"""
class Player:
    def initialise(self, x, y, fire_rate, health):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.health = health

    def shoot_faster(self, time):
        self.fire_rate *= 2
        delay(time)
        self.fire_rate /= 2

#==========================================================

            """ALIEN GENERAL""" 
class Alien:
    def initialise(self, x, y, speed, health):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health

    def move(self):
        self.y += self.speed
        self.x += self.speed

    def take damage(self)
        self.health -= 1
        if self.health <= 0

            """LEVEL 1 ALIEN"""
class Level1(Alien):
    def initialise(self, x, y):
        super().initialise(x, y, speed = 1, health = 1)

            """LEVEL 2 ALIEN"""
class Level2(Alien):
    def initialise(self, x, y):
        super().initialise(x, y, speed = 1.5, health = 2)

            """LEVEL 3 ALIEN"""
class Level3(Alien):
    def initialise(self, x, y):
        super().initialise(x, y, speed = 2, health = 3)

#=========================================================

def main():
    y = 10
    for i in range(1, 3):
        y += 15
        x = 10
        for j in range (1, 5):
            x += 15
            enemies += []

