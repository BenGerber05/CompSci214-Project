import stddraw
from player_2_1 import Player
from projectile_1_0 import Projectile
from enemy_2_1 import Functions, Enemy

def main():
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(0, 2)

    enemyMethods = Functions()
    player = Player(x=0, y=0, fire_rate=1, health=3)
    enemy_list = [enemyMethods.spawnRow()]
    projectiles = []
    player_angle = 90  # fixed upward

    print("Game started. Use A/D/S to move, Space to fire, Q to quit.")

    running = True
    while running:
        stddraw.clear()

        player.update_position()
        running = player.handle_key()
        player.draw()
        enemyMethods.move(enemy_list)

        # Fire projectile
        if player.wants_to_fire():
            proj = Projectile(player.x, player.y + player.radius, player_angle)
            projectiles.append(proj)

        # Update and draw projectiles
        for proj in projectiles[:]:
            proj.update()
            proj.draw()

            # Check collision with enemies
            for row in enemy_list:
                for enemy in row:
                    if enemy.is_hit_by(proj):
                        enemy.health -= 1
                        if proj in projectiles:
                            projectiles.remove(proj)
                        break

            if proj.is_off_screen() and proj in projectiles:
                projectiles.remove(proj)

        # Remove dead enemies
        enemyMethods.killEnemies(enemy_list)

        stddraw.show(20)

if __name__ == '__main__':
    main()
