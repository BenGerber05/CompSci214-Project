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

12/04/2025: projectile class created. player updated to have a new method: wants_to_fire which fires a projectille. handle_key method updated to have a shooting processor for the SPACE key.
enemy class updated for removal of baddies when health = 0
updated game loop to v2.1, adding a collision clause (sorry rourke, i was on a roll :) ) ~ Ben

14/04/2025: uoloaded player2_2 and enemy 2_1. For enemy i only changed it to include the pngs but i kept the boxes for now incase we want to make the enemies larger so it will be easier to scale the images. player file now includes the rotation of the space ship. I dont know if you guys want to have different ships or not but there are more if you guys want that to be random maybe ~ Z

16/04/2025: Ben ~ consolidate Z's function into new loop. Sounds, Power Ups, Projectile types
            Zak ~ Loading screen & End screen & in game bg
            Rourke ~ Score, enemy proj's, Diff scaling
            Priority : Loading screen & End screen & Score & Background
            Extra: Shooting, proj types, power ups

21/04/2025: Added basic shooting functionality and difficulty scaling for enemies. Added score update in main class. Still need to add different projectile types for enemies but that will take the backseat for now. - Rourke

