import stddraw
from picture import Picture

class Player:

    IMAGE_SCALAR = 0.4
    PINK_SHIP = Picture("Pink_Ship.png") #image

    def __init__(self, x, y, fire_rate, health):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.health = health
        self.radius = 0.1
        self.x_vel = 0
        self.should_fire = False

    def draw(self):
        """Draw the player as a circle."""
        
        stddraw.picture(self.PINK_SHIP, self.x, self.y, self.IMAGE_SCALAR,  self.IMAGE_SCALAR )

    def update_position(self):
        """Update player position with velocity, respecting screen bounds."""
        next_x = self.x + self.x_vel

        # Check bounds (-1 to 1)
        right_limit = 1 - (self.radius + 0.01)
        left_limit = -1 + (self.radius + 0.01)

        if left_limit <= next_x <= right_limit:
            self.x = next_x

    def handle_key(self):
        """Set velocity or actions based on key input."""
        key = ""
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
            elif key == 'q':
                return False  # signal to quit

        return True

    def wants_to_fire(self):
        """Return whether the player triggered a fire command."""
        if self.should_fire:
            self.should_fire = False
            return True
        return False