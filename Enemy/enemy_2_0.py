import stddraw
import stdarray
import random

class Enemy:

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
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1) 
    def score(self):
        return 100  
    

class Shooter(Enemy): #Shoots standard bullets
    def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
    def draw(self):
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1)  
    def shoot(self):
        pass
    def score(self):
        return 200  

class Bomber(Enemy): #Shoots bullets with blast radius 
    def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
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
     def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
     def draw(self): 
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledRectangle(self.x, self.y, 0.1, 0.1)  
     def dropPowerUp():
         pass
     def score(self):
        return 400  
     
class Functions: #Methods to be used on an array of enemies
    
    columns:int = 9

    def killEnemy(self,enemy_list:list[list]):
        '''Removes enemy with health 0 from list'''

        for i in len(enemy_list):
                for j in range(len(enemy_list[i])):
                    if enemy_list[i][j].health <= 0:
                        enemy_list[i].pop(j)

    def drop(self,enemy_list:list[list]): 
        '''Vertical Animation'''
    
        rows = len(enemy_list)

        for i in range(rows):
            for j in range(len(enemy_list[i])):
                enemy_list[i][j].updateY()
                enemy_list[i][j].xSpeed *= -1

    def move(self,enemy_list:list[list]): 
        '''Horizontal Animation'''
        rows = len(enemy_list)

        for i in range(rows):
            for j in range(len(enemy_list[i])):
                enemy_list[i][j].updateX()
                if enemy_list[i][j].hitLeft():
                     self.drop(enemy_list)
                     enemy_list += [self.spawnRow()] 
                 
                if enemy_list[i][j].hitRight():
                    self.drop(enemy_list)
                if enemy_list[i][j].health > 0:    
                    enemy_list[i][j].draw()

    def spawnRow(self):  
        """Spawn row"""

        enemyRow = []

        initial = -1+0.1
        shift = 0.15

        spawn_chance = 0.5 # initially a 50% chance of spawning
    
        for j in range(self.columns):
          
            x = (0.01+shift)*j +initial
            y = 2-1*0.15

            spawn = random.random()

            if not(spawn < spawn_chance): 

                random_type = random.random()
                if random_type<0.3:
                    enemyRow += [Brute(x,y,2)]
                elif random_type<0.6:
                    enemyRow += [Shooter(x,y,1)]
                elif random_type<0.9:
                    enemyRow += [Bomber(x,y,1)]
                elif random_type<1:
                    enemyRow += [Bonus(x,y,3)]

        return enemyRow       

        

   

        



    
