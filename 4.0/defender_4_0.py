import stddraw
from player_4_0 import Player
from projectile_4_0 import Projectile
from enemy_4_0 import Functions, Bonus
import time
import math



def main():
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(0, 2)

    enemyMethods = Functions()
    player = Player(x=0, y=0.15, fire_rate=0.4, health=3, angle_deg = 0)
    projectiles = []
    player_angle = 90  # fixed upward

    player_score = 0

    start_time = time.time()

    enemy_start_rate = 0.4
    enemy_spawn_rate = 0
    enemy_start_speed = 0.003
    enemy_speed = 0
    enemy_last_fire = []
    enemy_projectiles = []

    spawn_scale = 0
    speed_scale = 0

    enemy_list = [enemyMethods.spawnRow(enemy_start_rate,enemy_last_fire)]

    shields = []
    
    print("Game started. Use A/D/S to move, Space to fire, Q to quit.")

    Health_1 = Picture("Lives_1.jpg")
    Health_2 = Picture("Lives_2.jpg")
    Health_3 = Picture("Lives_3.jpg")
    
     # start page ========================
    START_PAGE1 = Picture("START_SCREEN1.png")
    START_PAGE2 = Picture("START_SCREEN2.png")

    running = False # dont run main game yet
    stddraw.setPenColor(stddraw.WHITE)
    while not running:
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

    # start page ========================
    
    while running:
      
        current_time = time.time() - start_time
        
        spawn_scale = math.log(current_time/400 + 1) #scales such that spawn rate increases logarithmically and reaches 1 after around 5 minutes
        
        enemy_spawn_rate = enemy_start_rate + spawn_scale 
 
        if enemy_speed <= 0.006:
            speed_scale = 0.005*math.pow(math.e,current_time/700) - 0.005 #scales exponentially such that the speed reaches its maximum of 0.006 after around 5 minutes
            enemy_speed = enemy_start_speed + speed_scale

        stddraw.clear(stddraw.BLACK)
        player.update_position()
        running = player.handle_key()
        player.draw()
        enemyMethods.move(enemy_list, enemy_spawn_rate, enemy_speed,enemy_last_fire, enemy_projectiles)

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
            proj = Projectile(player.x, player.y + player.radius, player_angle)
            projectiles.append(proj)
        
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
        # Show score
        stddraw.setFontSize(s=22)
        stddraw.setFontFamily(f="Arial")
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(-0.8, 1.93, "Score: " + str(player_score))
        
        # Update and draw enemy projectiles and check player for hits
        for proj in enemy_projectiles[:]:
            proj.update()
            proj.draw()
            if player.is_hit(proj):
                enemy_projectiles.remove(proj)
                player.health -= 1
                if player.health <= 0:
                    running = False
                    #add game over screen
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
                        player_score += enemy.score()
                        #update the score section on the ingame menu
                        if enemy.health <= 0:
                            if isinstance(enemy, Bonus):
                                enemy.powerUp(player,shields)
                            row.remove(enemy)
                            if len(row) == 0:
                                enemy_list.remove(row)
                                enemy_last_fire.pop(count) 
                count +=1                     
               

            if proj.is_off_screen() and proj in projectiles:
                projectiles.remove(proj)
            
        
        stddraw.show(20)

if __name__ == '__main__':
    main()
