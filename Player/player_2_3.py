import stddraw, math
from picture import Picture

class Player:
    def __init__(self, x, y, fire_rate, health):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.health = health
        self.radius = 0.2
        self.x_vel = 0
        self.should_fire = False
        self.filename = "Pink_Ship.png"
        self.angle_deg = 0
        self.original_image = Picture(self.filename)
        self.rotated_image = self.original_image

    def draw(self):
        """Draw the player as a circle."""
        stddraw.picture(self.rotated_image, self.x, self.y + self.radius, 0.5, 0.6) #changed to show picture

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
            key = stddraw.nextKeyTyped()

            if key == 'd':
                self.x_vel = 0.01
            elif key == 'a':
                self.x_vel = -0.01
            elif key == 's':
                self.x_vel = 0
            elif key == ' ':
                self.should_fire = True
            elif key == "l": #rotate left
                self.angle_deg += 15       
            elif key == "k": #rotate right
                self.angle_deg -= 15


            elif key == 'q':
                return False  # signal to quit

        return True

    def wants_to_fire(self):
        """Return whether the player triggered a fire command."""
        if self.should_fire:
            self.should_fire = False
            return True
        return False

    def rotate(self):
        """Rotate ship on l or k keypress. Save rotated ship as picture"""

        #limiting rotation =================== 

        if self.angle_deg >= 75:
            #undo the change of the angle and pass function
            self.angle_deg -= 15
            return

        if self.angle_deg <= -75:
            #undo the change of the angle and pass function
            self.angle_deg += 15
            return

        #rotation =================== 
        copy_x: int = self.original_image.width() // 2
        copy_y: int = self.original_image.height() // 2

        angle_rad = math.radians(self.angle_deg) #convert to rad
        cosMinusTheta: float = math.cos(-angle_rad)
        sinMinusTheta: float = math.sin(-angle_rad)

        w: int = self.original_image.width() 
        h: int = self.original_image.height()
        rotated_image:Picture = Picture(w, h)

        for tx in range(w):
            for ty in range(h):
                deltaX: int = tx - copy_x
                deltaY: int = ty - copy_y

                #formula from tut 3
                sx: int = int(deltaX*cosMinusTheta - deltaY*sinMinusTheta + copy_x)
                sy: int = int(deltaX*sinMinusTheta + deltaY*cosMinusTheta + copy_y)

                color: Color = stddraw.BLACK #fill with black if there is no colour
                if ((sx >= 0) and (sx < w) and (sy >= 0) and (sy < h)): #colour reading is in the image borders
                    color = self.original_image.get(sx, sy)
                rotated_image.set(tx, ty, color)

        self.rotated_image = rotated_image
        
        return
