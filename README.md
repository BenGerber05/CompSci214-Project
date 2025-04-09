03/04/2025: started making classes, and defining attributes. ~ Ben

04/04/2025: made the player movement work. Could not find a function in stddraw which reads a held keystroke, so entering 'a' or 'd' will make it move until it hits a wall, or is stopped with 's' ~ Z

06/04/2025: consolidated movement with classes. movement working as in z's previous version, with efficiency and modularity kept in mind.

07/04/2025: Started building basic skeleton of enemy class ~ Rourke

09/04/2025: Task division - Zak --> Rotation, Drawings & Title Screen 
                            Ben --> Consolidate w/hardcode, Firing of Projectiles, & Power Up Projectile Class
                            Rourke --> Consolidate w/function loop, Destrucion of enemies on impact

09/04/2025: The game runs through the game loop inside defender_2_0.py 
The rest is seperated into the enemy class and player class
Enemy class: created a Functions class where all the functions that work on the array of enemies are run. Created a killEnemy method
Player class: removed the movement class: Instead ran the handle key and updatePosition straight from the main game loop ~ Rourke
