import stddraw


def player():
    '''player movement function'''
    
    RADIUS = 0.05
    x,y = 0,0
    x_vel = 0
    vel_inc_flag = True #flag to allow vel increase
    vel_dec_flag = True #flag to allow vel decrease


    stddraw.setXscale(-1,1)
    stddraw.setYscale(0,2)
    stddraw.filledCircle(x, y + RADIUS, RADIUS)
    
    
    while True: #idk if this is a good idea
        if stddraw.hasNextKeyTyped(): #if a key was typed
            vel_inc_flag = True
            vel_dec_flag = True
            stddraw.clear()  #refresh on any keystroke
            key_pressed = stddraw.nextKeyTyped()
            if key_pressed == 'd':
                x_vel:float = 0.01
            
            elif key_pressed == 'a':
                x_vel:float = -0.01

            elif key_pressed == 's':
                x_vel:float = 0

        #check whether in bounds
        if (x > (1 - RADIUS)):
            vel_inc_flag = False #only change x if it doesnt go out of bounds 

        if (x < (-1 + RADIUS)):
            vel_dec_flag = False #only change x if it doesnt go out of bounds

        #change x pos accordingly
        if vel_inc_flag and (x_vel > 0):
            x += x_vel

        if vel_dec_flag and (x_vel < 0):
            x += x_vel


        stddraw.clear()
        stddraw.filledCircle(x, y + RADIUS, RADIUS)
        stddraw.show(30)

if __name__ == '__main__':
    player()
