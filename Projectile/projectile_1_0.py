import math
import stddraw

class Projectile:
    def __init__(self, x, y, angle_deg, speed=0.02):
        self.x = x
        self.y = y
        self.angle_deg = angle_deg
        self.speed = speed
        angle_rad = math.radians(angle_deg)
        self.x_vel = speed * math.sin(angle_rad)
        self.y_vel = speed * math.cos(angle_rad)
        self.radius = 0.02

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x, self.y, self.radius)

    def is_off_screen(self):
        return self.y > 2 or self.y < 0 or self.x < -1 or self.x > 1
