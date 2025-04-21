import stddraw
from player_2_4 import Player
from projectile_1_0 import Projectile
from enemy_2_2 import Functions, Enemy

def main():
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(0, 2)

    enemyMethods = Functions()
    player = Player(x=0, y=0.15, fire_rate=1, health=3, angle_deg=0)
    enemy_list = [enemyMethods.spawnRow()]
    projectiles = []

    print("Game started. Use A/D/S to move, K/L to rotate, Space to fire, Q to quit.")

    running = True
    while running:
        stddraw.clear(stddraw.BLACK)

        player.update_position()
        running = player.handle_key()
        player.draw()
        enemyMethods.move(enemy_list)

        if player.wants_to_fire():
            proj = Projectile(player.x, player.y + player.radius, player.angle_deg)
            projectiles.append(proj)

        for proj in projectiles[:]:
            proj.update()
            proj.draw()

            for row in enemy_list:
                for enemy in row:
                    if enemy.is_hit(proj):
                        enemy.health -= 1
                        if proj in projectiles:
                            projectiles.remove(proj)
                        if enemy.health <= 0:
                            row.remove(enemy)
                            if len(row) == 0:
                                enemy_list.remove(row)

            if proj.is_off_screen() and proj in projectiles:
                projectiles.remove(proj)

        stddraw.show(20)

if __name__ == '__main__':
    main()
