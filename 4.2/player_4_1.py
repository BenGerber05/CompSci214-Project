import stddraw, math
from picture import Picture
from color import Color  # Needed for rotating logic
from projectile_4_1 import Projectile
import time

class Player: #Created by Zac: 27855325 and Ben: 27943607
    IMAGE_SCALAR = 0.4
    PINK_SHIP = Picture("Pink_Ship.png")

    def __init__(self, x, y, fire_rate, health, angle_deg):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.health = health
        self.radius = 0.1
        self.x_vel = 0
        self.should_fire = False
        self.angle_deg = angle_deg
        self.original_image = Player.PINK_SHIP
        self.rotated_image = self.original_image
        self.last_fire = time.time()

    def draw(self):
        """Draw the player ship image (rotated if necessary)."""
        stddraw.picture(self.rotated_image, self.x, self.y, self.IMAGE_SCALAR, self.IMAGE_SCALAR)

    def update_position(self):
        """Update player position with velocity, respecting screen bounds."""
        next_x = self.x + self.x_vel
        right_limit = 1 - (self.radius + 0.01)
        left_limit = -1 + (self.radius + 0.01)

        if left_limit <= next_x <= right_limit:
            self.x = next_x

    def handle_key(self): #Ben: 27943607
        """Set velocity or actions based on key input."""
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped().lower()

            if key == 'd':
                self.x_vel = 0.01
            elif key == 'a':
                self.x_vel = -0.01
            elif key == 's':
                self.x_vel = 0
            elif key == ' ':
                self.should_fire = True
            elif key == 'l':
                self.angle_deg += 15
                self.rotate()
            elif key == 'k':
                self.angle_deg -= 15
                self.rotate()
            elif key == 'q':
                return False  # signal to quit

        return True

    def wants_to_fire(self):
        """Return whether the player triggered a fire command."""
        if self.should_fire and time.time() - self.last_fire >= self.fire_rate:
            self.should_fire = False
            self.last_fire = time.time()
            return True
        return False

    def rotate(self):
        """Rotate ship image and save it."""
        if self.angle_deg > 75:
            self.angle_deg = 75
        elif self.angle_deg < -75:
            self.angle_deg = -75

        angle_rad = math.radians(self.angle_deg)
        cos_theta = math.cos(-angle_rad)
        sin_theta = math.sin(-angle_rad)

        w, h = self.original_image.width(), self.original_image.height()
        center_x, center_y = w // 2, h // 2
        rotated = Picture(w, h)

        for tx in range(w):
            for ty in range(h):
                dx = tx - center_x
                dy = ty - center_y

                sx = int(dx * cos_theta - dy * sin_theta + center_x)
                sy = int(dx * sin_theta + dy * cos_theta + center_y)

                color = stddraw.BLACK
                if 0 <= sx < w and 0 <= sy < h:
                    color = self.original_image.get(sx, sy)
                rotated.set(tx, ty, color)

        self.rotated_image = rotated
    
    def is_hit(self, projectile: Projectile):
        half_length = self.IMAGE_SCALAR/2
        return projectile.x >= self.x - half_length/2 and  projectile.x <= self.x + half_length/2 and  projectile.y >= self.y - half_length and projectile.y <= self.y + half_length
