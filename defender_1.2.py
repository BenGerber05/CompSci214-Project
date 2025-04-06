import stddraw

class Player:
    def __init__(self, x, y, fire_rate, health):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.health = health
        self.radius = 0.1
        self.x_vel = 0

    def draw(self):
        """Draw the player as a circle."""
        stddraw.filledCircle(self.x, self.y + self.radius + 0.01, self.radius)

    def update_position(self):
        """Update player position with velocity, respecting screen bounds."""
        next_x = self.x + self.x_vel

        # Check bounds (-1 to 1)
        right_limit = 1 - (self.radius + 0.01)
        left_limit = -1 + (self.radius + 0.01)

        if left_limit <= next_x <= right_limit:
            self.x = next_x

    def handle_key(self, key):
        """Set velocity or actions based on key input."""
        if key == 'd':
            self.x_vel = 0.01
        elif key == 'a':
            self.x_vel = -0.01
        elif key == 's':
            self.x_vel = 0
        elif key == 'q':
            return False  # signal to quit
        return True

    def movement(self):
        """loop for handling movement."""
        stddraw.setXscale(-1, 1)
        stddraw.setYscale(0, 2)
        print("Game started. Click the window, use A/D/S to move, Q to quit.")

        running = True
        while running:
            # Handle input if any
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                running = self.handle_key(key)

            # Update logic
            self.update_position()

            # Drawing
            stddraw.clear()
            self.draw()
            stddraw.show(20)

def main():
    player = Player(x=0, y=0, fire_rate=1, health=3)
    player.movement()

if __name__ == '__main__': main()
