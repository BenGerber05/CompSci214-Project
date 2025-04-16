
import stddraw
import player_2_0
from player_2_0 import Player
import enemy_2_0 
  
def main():

    #initialize stddraw
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(0, 2)

    #initialize enemyfunctions class
    enemyMethods = enemy_2_0.Functions()
 
    #initialize objects
    player = Player(x=0, y=0, fire_rate=1, health=3)
    enemy_list = []
    enemy_list += [enemyMethods.spawnRow()]

    print("Game started. Click the window, use A/D/S to move, Q to quit.")

    #main game loop
    running = True
    while running:

        stddraw.clear()   

        player.update_position() #moves player
        running = player.handle_key() #updates player velocity
        player.draw() #draws player
        enemyMethods.move(enemy_list) #draws list of enemies

        stddraw.show(20)


if __name__ == '__main__': main()
