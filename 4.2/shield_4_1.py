import stddraw
from projectile_4_1 import Projectile


class Shield: #Created by Rourke: 27547957
    
    START_HEALTH = 4

    def __init__(self, position): 

        self.width = 0.2
        self.height = 0.1

        self.x = position*0.5 - self.width/2
        self.y = 0.5

        self.position = position

        self.health = 4

    def draw(self):
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(self.x, self.y, self.width, self.height) 
           
        if self.health < Shield.START_HEALTH:

            width = self.width*(Shield.START_HEALTH-self.health)/Shield.START_HEALTH
            height = self.height*(Shield.START_HEALTH-self.health)/Shield.START_HEALTH
            x = self.x + (self.width - width)/2
            y = self.y + (self.height - height)/2

            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledRectangle(x, y,width , height)

    def is_hit(self, projectile: Projectile):
        return projectile.x>=self.x and projectile.x<=self.x + self.width and projectile.y >=self.y and projectile.y<=self.y + self.height
