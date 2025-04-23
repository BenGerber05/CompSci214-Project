import stddraw
import stdarray
import random
from projectile_4_1 import Projectile
from picture import Picture
import time
from player_4_1 import Player
from shield_4_1 import Shield

class Enemy:

   
    HOR_SPACING = 0.25
    VERT_SPACING = 0.1
    ALIEN_SIZE = 0.2
    HALF_LENGTH = ALIEN_SIZE/2

    REF_SPEED = 0.025

    VERT_START = 0.17
    HOR_START = ALIEN_SIZE - 1
    COLUMNS = 5

    LEFT_BOUND = ALIEN_SIZE - 1
    RIGHT_BOUND = 1-ALIEN_SIZE

    SCREEN_WIDTH = 2
    SCREEN_HEIGHT = 2

    FIRE_RATE = 2 # 1 bullet every 2 seconds
    FIRE_CHANCE = 0.6 # change now

    ref_left = HOR_START
    ref_right = HOR_SPACING*(COLUMNS-1) + HOR_START
    ref_direction = 1

    
    def __init__(self,x, y, health): 

        self.x = x
        self.y = y

        self.width = 0.2

        self.health = health
        self.image_scalar = Enemy.ALIEN_SIZE
      
    def updateX(self,speed):
        self.x += speed*Enemy.ref_direction

    def updateY(self):
        self.y = self.y - Enemy.VERT_SPACING
    
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
    def shoot(self, enemy_projectiles):
        proj = Projectile(self.x, self.y - Enemy.HALF_LENGTH, -90)
        enemy_projectiles.append(proj)
    def score(self):
        return 200  

class Bomber(Enemy): #Shoots bullets with blast radius 
    def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
        self.bomber_image = Picture("Bomber_Alien.png")
    def draw(self):
        stddraw.picture(self.bomber_image, self.x, self.y, self.image_scalar  ,self.image_scalar) 
    def shoot(self, enemy_projectiles):
        proj = Projectile(self.x, self.y - Enemy.HALF_LENGTH, -90)
        enemy_projectiles.append(proj)
    def score(self):
        return 300  

class Bonus(Enemy): #Drops Power ups
     def __init__(self,x, y, alive):
        super().__init__(x, y, alive)
        self.bonus_image = Picture("Bonus_Alien.png") #image
     def draw(self): 
        stddraw.picture(self.bonus_image, self.x, self.y, self.image_scalar  ,  self.image_scalar )
     def powerUp(self,player:Player, shields:list):
        r = random.random()
        if r <= 0.5:
            if len(shields) == 3: #Increase health of all shields  
                for shield in shields:
                    if shield.health < Shield.START_HEALTH:
                        shield.health += 1
            else: # add new shield at random position 
                openPos = [-1,0,1]
                for shield in shields:
                    if shield.position in openPos:
                        openPos.remove(shield.position)
                newPos = openPos[int(random.random()*len(openPos)) - 1]
                shields += [Shield(newPos)] 
        elif player.health < 3:   
             player.health +=1
        elif player.fire_rate == 0.45:
             player.fire_rate = 0.25     
        

         
     def score(self):
        return 500  
       
class Functions: #Methods to be used on an array of enemies          

    def drop(self,enemy_list:list[list]): 
        '''Vertical Animation'''

        Enemy.ref_direction*=-1

        for row in enemy_list:
            for enemy in row:
                enemy.updateY()

    def move(self,enemy_list:list[list], spawn_chance: float, speed: float, last_fire: list[float], enemy_projectiles: list[Projectile]): 
        '''Horizontal Animation and shooting'''

        Enemy.ref_left += Enemy.ref_direction*speed
        Enemy.ref_right += Enemy.ref_direction*speed

        if Enemy.ref_left <= Enemy.LEFT_BOUND and Enemy.ref_direction<0: #if an imaginary enemy in the 0th column hits the left bound => switch direction and spawn a row
                    self.drop(enemy_list)
                    enemy_list += [self.spawnRow(spawn_chance, last_fire)] 
                 
        if Enemy.ref_right >= Enemy.RIGHT_BOUND and Enemy.ref_direction>0: #if an imaginary enemy in the maximum column hits the right bound => switch direction
                    self.drop(enemy_list)
        
        count = 0 
        for row in enemy_list:
            fire_row = False
            if (time.time() - count - last_fire[count] >= Enemy.FIRE_RATE): #Firing of each row offset by 1 second
                    last_fire[count] = time.time()
                    fire_row = True
            for enemy in row:
                if fire_row and isinstance(enemy, (Bomber, Shooter)):
                    fire = random.random()
                    if fire<= Enemy.FIRE_CHANCE: #Each enemy in the row eligible to fire shoots if the random number is lower than the fire chance
                        
                        enemy.shoot(enemy_projectiles)

                enemy.updateX(speed)
                enemy.draw()
            count+=1
                    

    def spawnRow(self, spawn_chance,last_fire):  
        """Spawn row"""

        last_fire += [time.time() - 1] # Can fire 1 second after spawning
        enemyRow = []
    
        for j in range(Enemy.COLUMNS):
          
            x = (Enemy.HOR_SPACING)*j +Enemy.HOR_START
            y = Enemy.SCREEN_HEIGHT-Enemy.VERT_SPACING - Enemy.VERT_START

            spawn = random.random()

            if (spawn < spawn_chance): 

                random_type = random.random()
                if random_type<0.2:
                    enemyRow += [Bomber(x,y,2)]
                elif random_type<0.6:
                    enemyRow += [Shooter(x,y,1)]
                elif random_type<0.95:
                    enemyRow += [Brute(x,y,2)]
                elif random_type<1:
                    enemyRow += [Bonus(x,y,3)]

        return enemyRow       

        

   

        



    