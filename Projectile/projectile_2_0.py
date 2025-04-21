class Projectile:
    def __init__(self, x, y, angle_deg, speed=0.02):
        self.x = x
        self.y = y
        self.speed = speed
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


class Bomb(Projectile):
    def __init__(self, x, y, angle_deg, damage=1, radius=1):
        super().__init__(x, y, angle_deg)  # Inherit position and velocity
        self.damage = damage
        self.radius = radius  # Explosion radius

    def explode(self, enemies):
        """Explode and damage enemies within the explosion radius."""
        # List of directions to check (neighbors around the bomb)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dx, dy in directions:
            nx, ny = self.x + dx * self.radius, self.y + dy * self.radius
            for enemy in enemies:
                if enemy.x == nx and enemy.y == ny:
                    enemy.damage(self.damage)
                    break  # Stop checking once we hit an enemy

    def update(self):
        """Update bomb position, then check for explosion when it reaches target."""
        super().update()  # Move the bomb like any projectile

        # Example explosion logic: You can trigger explosion when bomb hits target or at specific time
        if self.is_off_screen():
            return True  # Bomb is off-screen, stop it
        return False
