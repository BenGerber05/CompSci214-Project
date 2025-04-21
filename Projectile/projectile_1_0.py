import math
import stddraw
from player_2_4.py import Player

class Projectile:
    def __init__(self, x, y, angle_deg, speed=0.02):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle_deg = Player.angle_deg
        # Convert angle to radians for math functions
        
        angle_rad = math.radians(angle_deg)
        self.x_vel = speed * math.cos(angle_rad)
        self.y_vel = speed * math.sin(angle_rad)
        self.radius = 0.02

    def update(self):
        """Update the projectile's position based on its velocity."""
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        """Draw the projectile as a small filled circle."""
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x, self.y, self.radius)

    def is_off_screen(self):
        """Check if the projectile has moved out of the screen bounds."""
        return self.y > 2 or self.y < 0 or self.x < -1 or self.x > 1

