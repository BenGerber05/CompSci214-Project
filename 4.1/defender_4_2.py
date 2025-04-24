import stddraw
from player_4_1 import Player
from projectile_4_1 import Projectile, Bomb
from enemy_4_1 import Functions, Bonus
from picture import Picture
import time
import math
import pygame



def main():
    
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(0, 2)

    pygame.mixer.init()
    shoot_sound = pygame.mixer.Sound("Pew.mp3")
    power_up_sound = pygame.mixer.Sound("PowerUp.mp3")
    
    enemyMethods = Functions()
    projectiles = []


    highest_score:int = -3000


    START_TIME = time.time()

    ENEMY_START_SPAWN_RATE = 0.4
    enemy_spawn_rate = 0
    ENEMY_START_SPEED = 0.0025
    enemy_speed = 0
    enemy_last_fire = []

    enemy_projectiles = []

    LOWER_BOUND = 0.2

    spawn_scale = 0
    speed_scale = 0


    lowest_enemy: float

    shields = []
    
    print("Game started. Use A/D/S to move, Space to fire, Q to quit.")

    Health_1 = Picture("Lives_1.jpg")
    Health_2 = Picture("Lives_2.jpg")
    Health_3 = Picture("Lives_3.jpg")

    GameOver1 = Picture("GAMEOVER_SCREEN1.png")
    GameOver2 = Picture("GAMEOVER_SCREEN2.png")

    menu1 = True
    menu2 = False
    
     # start page ========================
    START_PAGE1 = Picture("START_SCREEN1.png")
    START_PAGE2 = Picture("START_SCREEN2.png")
    
    ingame = True

    running = False # dont run main game yet
    while ingame:
    
        enemy_list = [enemyMethods.spawnRow(ENEMY_START_SPAWN_RATE,enemy_last_fire)]
        lowest_enemy = 0
        player_score = 0
        player = Player(x=0, y=0.15, fire_rate=0.45, health=3, angle_deg = 0)

        while menu1:
            stddraw.clear()
            stddraw.picture(START_PAGE1, 0, 1, 2.3, 2.3)
            stddraw.show(150)
            stddraw.clear()
            stddraw.picture(START_PAGE2, 0, 1, 2.3, 2.3)
            stddraw.show(150)

            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped().lower() # account for caps
                if key == 'e':
                    running = True # only start main game loop now
                    menu1 = False
                if key == 'q':
                    menu1 = False
                    ingame = False

        # start page ========================


        while running:
     
            current_time = time.time() - START_TIME
            
            spawn_scale = math.log(current_time/400 + 1) #scales such that spawn rate increases logarithmically and reaches 1 after around 5 minutes
            
            enemy_spawn_rate = ENEMY_START_SPAWN_RATE + spawn_scale 
     
            if enemy_speed <= 0.006:
                speed_scale = 0.005*math.pow(math.e,current_time/700) - 0.005 #scales exponentially such that the speed reaches its maximum of 0.006 after around 5 minutes
                enemy_speed = ENEMY_START_SPEED + speed_scale

            stddraw.clear(stddraw.BLACK)
            player.update_position()
            running = player.handle_key()
            player.draw()

            #health hud ===============
            if player.health == 3:
                stddraw.picture(Health_3, 0.7,1.9,0.5,0.15)
            elif player.health == 2:
                stddraw.picture(Health_2, 0.7,1.9,0.5,0.15)
            elif player.health == 1:                
                stddraw.picture(Health_1, 0.7,1.9,0.5,0.15)
            # =========================
            
            # Fire projectile
            if player.wants_to_fire():
                shoot_sound.play()
                if Bonus.powerUp == "BOOM":
                    proj = Bomb(player.x, player.y + player.radius, player.angle_deg)
                else:
                    proj = Projectile(player.x, player.y + player.radius, player.angle_deg)
                projectiles.append(proj)
            
            # Show score
            stddraw.setFontSize(s=22)
            stddraw.setFontFamily(f="Arial")
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.text(-0.8, 1.93, "Score: " + str(player_score))

            #Start of change
            #Put shield hit checking in its own loop
            for shield in shields:
                 shield.draw()
                 for proj in projectiles[:]:
                     if shield.is_hit(proj):
                         projectiles.remove(proj)
                         shield.health-=1
                         if shield.health == 0:
                             shields.remove(shield)
                 for proj in enemy_projectiles[:]:
                     if shield.is_hit(proj):
                         enemy_projectiles.remove(proj)
                         shield.health-=1
                         if shield.health == 0:
                             shields.remove(shield)
            #End of change
            
            # Update and draw enemy projectiles and check player for hits
            for proj in enemy_projectiles[:]:
                proj.update()
                proj.draw()

                if player.is_hit(proj):
                    enemy_projectiles.remove(proj)
                    player.health -= 1
                    player.fire_rate = 0.45
                    player_score -= 100
                    if player.health <= 0: # player dies
                        running = False
                        menu2 = True
                        if player_score > highest_score:
                            highest_score = player_score
                        break
                        

                if proj.is_off_screen() and proj in enemy_projectiles:
                    enemy_projectiles.remove(proj)
            
            # Update and draw projectiles
            for proj in projectiles[:]:
                proj.update()
                proj.draw()

                # Check collision with enemies
                count = 0
                for row in enemy_list:
                    for enemy in row:
                        if enemy.is_hit(proj):
                            enemy.health-=1
                            projectiles.remove(proj)
                            if enemy.health <= 0:
                                player_score += enemy.score()
                                if isinstance(enemy, Bonus):
                                    power_up_sound.play()
                                    enemy.powerUp(player,shields)
                                row.remove(enemy)
                                if len(row) == 0:
                                    enemy_list.remove(row)
                                    enemy_last_fire.pop(count) 
                    count +=1                     
                   
                if proj.is_off_screen() and proj in projectiles:
                    projectiles.remove(proj)

            enemyMethods.move(enemy_list, enemy_spawn_rate, enemy_speed,enemy_last_fire, enemy_projectiles)

            if len(enemy_list)>0 and len(enemy_list[0])>0:
                lowest_enemy = enemy_list[0][0].y
                if lowest_enemy <= LOWER_BOUND:
                    running = False
                    break
            
                     
            stddraw.show(20)
        stddraw.setPenColor(stddraw.WHITE)
        while menu2:
            #display endmenu
            pygame.mixer.music.load("GameOver.mp3")
            pygame.mixer.music.set_volume(0.5)
            stddraw.clear()
            stddraw.picture(GameOver1, 0, 1, 2.3, 2.3)
            stddraw.text(0, 0.75, str(player_score))
            stddraw.text(0, 1.1, str(highest_score))
            stddraw.show(150)

            stddraw.clear()
            stddraw.picture(GameOver2, 0, 1, 2.3, 2.3)
            stddraw.text(0, 0.75, str(player_score))
            stddraw.text(0, 1.1, str(highest_score))
            stddraw.show(150)

            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped().lower() # account for caps
                if key == 'e':
                    running = True # only start main game loop now
                    menu2 = False
                if key == 'q':
                    menu2 = False
                    ingame = False


        
        


        
        

if __name__ == '__main__':
    main()
