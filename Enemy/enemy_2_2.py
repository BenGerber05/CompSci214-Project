import stddraw
import stdarray
import random
from projectile_1_0 import Projectile
from picture import Picture

class Enemy:

   
    HOR_SPACING = 0.25
    VERT_SPACING = 0.1
    ALIEN_SIZE = 0.2
    HALF_LENGTH = ALIEN_SIZE/2

    REF_SPEED = 0.003

    VERT_START = 0.1
    HOR_START = ALIEN_SIZE - 1
    COLUMNS = 6

    LEFT_BOUND = ALIEN_SIZE - 1
    RIGHT_BOUND = 1-ALIEN_SIZE

    SCREEN_WIDTH = 2
    SCREEN_HEIGHT = 2

    reference_left = HOR_START
    reference_right = HOR_SPACING*(COLUMNS-1) + HOR_START

    spawn_chance = 0.5
    

    def __init__(self,x, y, health): 

        self.x = x
        self.y = y

        self.width = 0.2

        self.health = health
        self.image_scalar = Enemy.ALIEN_SIZE
    
    def draw(self): #overridden
        pass     

    def updateX(self):
        self.x += Enemy.REF_SPEED

    def updateY(self):
        self.y = self.y - Enemy.VERT_SPACING

    def hitLeft(self): #Hit left boundary
        
        return self.x <= Enemy.LEFT_BOUND and self.Enemy.REF_SPEED<0
    
    def hitRight(self): #Hit right boundary
        right = 1-Enemy.ALIEN_SIZE
        return self.x >= right and self.Enemy.REF_SPEED>0
    
    def is_hit(self, projectile: Projectile):
        half_length = Enemy.ALIEN_SIZE/2
        return projectile.x >= self.x - half_length and  projectile.x <= self.x + half_length and  projectile.y >= self.y - half_length and projectile.y <= self.y + half_length
    
   
class Brute(Enemy): #Standard no functionality
    def __init__(self,x, y, health):
        super().__init__(x, y, health)
        self.brute_image = Picture("Brute_Alien.png")
        
    def draw(self):
        stddraw.picture(self.brute_image, self.x, self.y,  self.image_scalar ,  self.image_scalar )
    def score(self):
        return 100  
    

class Shooter(Enemy): #Shoots standard bullets
    def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
        self.shooter_image = Picture("Shooter_Alien.png")
    def draw(self):
        stddraw.picture(self.shooter_image, self.x, self.y,  self.image_scalar , self.image_scalar )
    def shoot(self):
        pass
    def score(self):
        return 200  

class Bomber(Enemy): #Shoots bullets with blast radius 
    def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
        self.bomber_image = Picture("Bomber_Alien.png")
    def draw(self):
        stddraw.picture(self.bomber_image, self.x, self.y, self.image_scalar  ,self.image_scalar) 
    def shoot(self):
        pass
    def score(self):
        return 300  

class Bonus(Enemy): #Drops Power ups
     def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
        self.bonus_image = Picture("Bonus_Alien.png") #image
     def draw(self): 
        stddraw.picture(self.bonus_image, self.x, self.y, self.image_scalar  ,  self.image_scalar )
     def dropPowerUp():
         pass
     def score(self):
        return 400  
       
class Functions: #Methods to be used on an array of enemies          

    def drop(self,enemy_list:list[list]): 
        '''Vertical Animation'''

        Enemy.REF_SPEED*=-1

        for row in enemy_list:
            for enemy in row:
                enemy.updateY()


    def move(self,enemy_list:list[list]): 
        '''Horizontal Animation'''

        Enemy.reference_left += Enemy.REF_SPEED
        Enemy.reference_right += Enemy.REF_SPEED

        if Enemy.reference_left <= Enemy.LEFT_BOUND and Enemy.REF_SPEED<0:
                    self.drop(enemy_list)
                    enemy_list += [self.spawnRow()] 
                 
        if Enemy.reference_right >= Enemy.RIGHT_BOUND and Enemy.REF_SPEED>0:
                    self.drop(enemy_list)

        for row in enemy_list:
            for enemy in row:
                enemy.updateX()
                enemy.draw()
                    

    def spawnRow(self):  
        """Spawn row"""

        enemyRow = []
    
        for j in range(Enemy.COLUMNS):
          
            x = (Enemy.HOR_SPACING)*j +Enemy.HOR_START
            y = Enemy.SCREEN_HEIGHT-Enemy.VERT_SPACING - Enemy.VERT_START

            spawn = random.random()

            if not(spawn < Enemy.spawn_chance): 

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

        

   

        



    