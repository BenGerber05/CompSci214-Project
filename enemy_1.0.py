import stddraw
import stdarray
import random

class Enemy:
    
    columns = 9

    def __init__(self,x, y, health): 

        self.x = x
        self.y = y
        self.xSpeed = 0.0015

        self.health = health
    
    def draw(self): #overridden
        pass     

    def updateX(self):
        self.x = self.x + self.xSpeed

    def updateY(self):
        self.y = self.y - 0.075

    def hitLeft(self): #Hit left boundary
        left = -1+0.1
        return self.x <= left and self.xSpeed<0
    
    def hitRight(self): #Hit right boundary
        right = 1-0.2
        return self.x >= right and self.xSpeed>0
    
   
class Brute(Enemy): #Standard no functionality
    def __init__(self,x, y, health):
        super().__init__(x, y, health)
        
    def draw(self):
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1) 
    def score(self):
        return 100  
    

class Shooter(Enemy): #Shoots standard bullets
    def __init__(self,x, y, health):
        super().__init__(x, y, health)
    def draw(self):
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1)  
    def shoot(self):
        pass
    def score(self):
        return 200  

class Bomber(Enemy): #Shoots bullets with blast radius 
    def __init__(self,x, y, health):
        super().__init__(x, y, health)
    def draw(self):
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1)  
    def shoot(self):
        pass
    def score(self):
        return 300  

class Bonus(Enemy): #Drops Power ups
     def __init__(self,x, y, health):
        super().__init__(x, y, health)
     def draw(self): 
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1)  
     def dropPowerUp():
         pass
     def score(self):
        return 400  

def drop(enemy:list[list]): #Vertical Animation
    
    rows = len(enemy)
    columns = Enemy.columns
    for i in range(rows):
        for j in range(columns):
            enemy[i][j].updateY()
            enemy[i][j].xSpeed *= -1

def move(enemy:list[list]): #Horizontal Movement

    stddraw.clear()
    rows = len(enemy)
    columns = Enemy.columns

    for i in range(rows):
        for j in range(columns):
            enemy[i][j].updateX()
            if enemy[i][j].hitLeft():
                 drop(enemy)
                 enemy += [spawnRow()] 
                 
            if enemy[i][j].hitRight():
                drop(enemy)
            if enemy[i][j].health > 0:    
                enemy[i][j].draw()
            
    stddraw.show(20)
    
def updateSpeed(speed, enemy): #To increase speed later on 
    rows, columns = getDims(enemy)

    for i in range(rows):
        for j in range(columns):
            enemy[i][j].speed = speed

def spawnRow():  # Method

        columns = 9   
        enemy = stdarray.create1D(columns,Enemy(0,0, 0))

        initial = -1+0.1
        shift = 0.15

        spawn_chance = 0.5 # initially a 50% chance of spawning
     
        for j in range(columns):

            x = (0.01+shift)*j +initial
            y = 2-1*0.15

            spawn = random.random()
            if spawn < spawn_chance: #doesnt spawn
                enemy[j] = Enemy(x,y, 0)
            else: #sets enemy type
                random_type = random.random()
                if random_type<0.3:
                    enemy[j] = Brute(x,y,2)
                elif random_type<0.6:
                    enemy[j] = Shooter(x,y,1)
                elif random_type<0.9:
                    enemy[j] = Bomber(x,y,1)
                elif random_type<1:
                    enemy[j] = Bonus(x,y,3)

        return enemy       

def main(): 

   enemy = []
   enemy += [spawnRow()]
   
   while(True): 
        move(enemy)

if __name__ == '__main__': main()
        

   

        



    
