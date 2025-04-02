#// Patrick Matuszek
#//Asterpocalypse Program
#//ICS4U
#//11/1/2020
    
#import all required classes
from tkinter import Tk, Canvas, PhotoImage, messagebox
from Bullet import Bullet
from Player import Player
from Asteroid import Asteroid
import pygame

#initialize mixer
pygame.mixer.init()

#load and play backgorund song on repeat
pygame.mixer.music.load("15 MilkyWay (Battle).mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(loops=-1)

#create a function to play a sound effect
def playlasereffect():
    #initialize sound effect
    laser = pygame.mixer.Sound("064-laser.wav")
    #play effect
    pygame.mixer.Sound.play(laser)
 
#create a function to play a sound effect   
def playexplosioneffect():
    #initialize sound effect
    explode = pygame.mixer.Sound("explosion.wav")
    #play effect
    pygame.mixer.Sound.play(explode)

#create a function to pause and un-pause the timers
def pausetimers(flag = True):
    global frametmrid
    global bullettmrid
    global collisionid
    global asterspawntmrid
    
    #check if you want to pause or un-pause (true to pause, false to un-pause)
    if flag == True:
        try:
            #pause these timers
            root.after_cancel(frametmrid)
            root.after_cancel(bullettmrid)
            root.after_cancel(collisionid)
            root.after_cancel(asterspawntmrid)
        except ValueError:
            pass
    else:
        #un-pause these timers
        frame()
        bulletTimer()
        Collisionchk()
        create_Asteroid()

#create a timer that updates the score, every 50ms
def scoretimer():
    global score
    global scoretmrid
    canvas.itemconfig(score_text, text = score)
    scoretmrid = root.after(50, scoretimer)
    
#create a timer that updates the ship frame, every 125ms    
def frame():
    global frametmrid
    #check which animation to play and play it
    P.animate(B.isFired())
    frametmrid = root.after(125, frame)

#create a program to close the game
def exit_program():
    #stop these timers
    root.after_cancel(btid)
    root.after_cancel(scoretmrid)
    #stop all other timers
    pausetimers()
    
    exit()

#create a program to reset the game
def reset(flag = True):
    global score
    global asteroid_spawn_rate
    global asteroid_speed
    #reset the asteroids to the rightmost wall, and offset them
    widthsetback = 0
    for x in range(len(asteroids)):
        asteroids[x].destroy()
        widthsetback += asteroids[x].getWidth()
        asteroids[x].makeinvis(widthsetback)
        
    #reset the laser
    B.reset()
    
    #hard reset the game, make speed the base speed, and reset score
    if flag == True:
        asteroid_speed = 100
        asteroid_spawn_rate =2000
        score = 0
        canvas.itemconfig(score_text, text = score)

#create a function to check whether a player loses a life or has a game over       
def playerlives():

    global score
    
    #check the total lives, if 0 ask if they want to play again
    if P.getLives() == 0:
        #pause timers, reset player health/lives, soft reset the game
        pausetimers()
        P.reset()
        reset(False)
        flag = messagebox.askyesno("Asterpocalypse", "You had " + str(score) + " Points\nYou are out of lives would you like to play again?")
        #hard reset the game
        reset()
        #reset player location
        P.resetlocation()
        #if they choose no exit the program
        if flag == False:
            exit_program()
        #un-pause the timers
        pausetimers(False)
            
            
    if P.getHealth() == 0:
        #pause timers
        pausetimers()
        #reset health  
        P.resethealth()
        #soft reset game
        reset(False)
        #output that they lost a life
        messagebox.showinfo("Asterpocalypse", "You lost a life")
        #reset the player location
        P.resetlocation()
        #un-pause the timers
        pausetimers(False)
        
        
    
#create a function to check if an asteroid was destroyed, and if yes add the points it was worth to the total points     
def asterTimer(spacerock):

    global score
    #check if asteroid is destroyed
    if spacerock.isdestroyed() == True:
        #get its point value
        points = spacerock.getAsteroidpoints()
        #add points to the score
        score += points
        #reset the asteroid
        spacerock.makeinvis()
        
#create a timer to check if the laser goes off the right side of the screen, every 50ms            
def bulletTimer():
    global bullettmrid
    if B.getX() > canvas.winfo_width():
        B.reset()

    bullettmrid = root.after(50, bulletTimer)

#create a timer to animate the background, and call it every 50ms
def background_timer():
    global btid
    
    #cycle through the list of frames
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5
    
    btid = root.after(50, lambda: background_timer())
    root.update()
    
    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

#create a timer to check collision every 1ms
def Collisionchk():
    global collisionid
    
    #go through each asteroid and check if the player is touching the asteroid
    for x in range(len(asteroids)):
        #check if the asteroid is destroyed, if so skip the rest
        if asteroids[x].isdestroyed() == True:
            pass
        else:
            #check that the player and asteroid overlap, if they do take a life from the player
            if P.getX() + P.getWidth() - 10 >= asteroids[x].getxPos() and P.getX() <= asteroids[x].getxPos() + asteroids[x].getWidth() and asteroids[x].isdestroyed() == False:
                if P.getY() + P.getHeight() >= asteroids[x].getyPos() and P.getY() <= asteroids[x].getyPos() + asteroids[x].getHeight():
                    #set the health of the player to 1
                    P.setHealth(1)
                    #take that 1hp away
                    P.takeDamage()
                    #play sound effect
                    playexplosioneffect()
                    #check the lives left
                    playerlives()
                    break
                
    #check if the laser has been fired
    if B.isFired() == True:
        #go through all the asteroids and check if the laser overlaps any of them, if it does, reset the laser and make the asteroid take damage
        for x in range(len(asteroids)):
            if asteroids[x].getxPos() + asteroids[x].getWidth() - 10 >= B.getX() and asteroids[x].getxPos() <= B.getX() + B.getWidth() and asteroids[x].isdestroyed() == False:
                if asteroids[x].getyPos() + asteroids[x].getHeight() >= B.getY() and asteroids[x].getyPos() <= B.getY() + B.getHeight():
                    #reset the laser
                    B.reset()
                    #asteroid takes damage
                    asteroids[x].TakeDamage()
                    #check if it is destroyed
                    asterTimer(asteroids[x])
                        
                
    collisionid = root.after(1, Collisionchk)

#create a function that will check if any asteroids hit the left wall
def AsterWallchk():    
    #if there are no asteroids skip the code
    if len(asteroids) == 0:
        pass
    else:
        #go through all asteroids and check if they are passed the left wall, if yes, the player takes damage 
        for x in range(len(asteroids)):
            if asteroids[x].getxPos() + asteroids[x].getWidth() <= 0 and  asteroids[x].isdestroyed() == False:
                #destroy the asteroid, and offset it
                asteroids[x].destroy()
                asteroids[x].makeinvis()
                
                #make the player take damage and check lives
                P.takeDamage()
                playerlives()               
                break
    
            
                    
ySpawnPos = 0
#create a function to check whether an asteroid can spawn on a specific y-axis value
def checkspawn(A):
    global asteroids
    global ySpawnPos
    
    #go through the asteroids and check whether the newest asteroids spawn overlaps any of them
    for x in range(len(asteroids)):
        #if this asteroid isnt overlapping with the right wall go to the next one
        if asteroids[x].getxPos() + asteroids[x].getWidth() <= canvas.winfo_reqwidth():
            pass
        else:
            #get the hitbox of this asteroid
            ytop = asteroids[x].getyPos()
            ybot = asteroids[x].getHeight()
            xL = asteroids[x].getxPos()
            xR = asteroids[x].getWidth()
            #get a y value that is spawnable
            ySpawnPos = A.genYSpawn(y1 = ytop, y2 = ybot,x1= xL,x2= xR)
            return ySpawnPos
    
    #get a y value that is spawnable
    ySpawnPos = A.genYSpawn()
                
    return ySpawnPos
        
#set base difficulty stats    
asteroid_spawn_rate = 2000
asteroid_speed = 100
difficulty = 0

#create a timer that creates an asteroid, according to the spawn rate (2000ms)
def create_Asteroid():
    global asterspawntmrid
    global asteroid_spawn_rate
    global asteroid_speed

    global difficulty
    canspawn = False
    
    
    
    #check difficulty and make the game more difficult by increasing how fast asteroids move
    if difficulty == 2 and asteroid_speed != 40:
        asteroid_speed -= 30
        difficulty = 0
    elif difficulty == 2 and asteroid_speed != 10:
        asteroid_speed -= 10
        difficulty = 0
       
    #check if there is less than 10 asteroids made  
    if len(asteroids) < 10:
        #make a new asteroid object
        A = Asteroid(canvas, imgTitle)
        #generate the asteroids stats
        A.Generate()
        
        #if it is the first asteroid created spawn it anywhere on the y axis
        if len(asteroids) == 0:
            A.genYSpawn()
        else:
            #check if you can spawn it on the y axis
            checkspawn(A)
        #make the image visible    
        A.SpawnAsteroid()
        #set speed
        A.setSpeed(asteroid_speed)
        #start movin the asteroid
        A.moveAsteroid()
        #add the object to the list
        asteroids.append(A)
   
    elif len(asteroids) == 10:
        #if 10 asteroid objects are already made
        #go through them all and check if the next wave of 10 can spawn
        for y in range(len(asteroids)):
            #if all asteroids are destroyed then spawn the next wave otherwise dont spawn the next wave
            if asteroids[y].isdestroyed() == True:
                canspawn = True
            else:
                canspawn = False
                break
        
        #if the new wave can spawn show text saying that a wave is approaching    
        if canspawn == True:
            canvas.itemconfig(text, text = "New Wave Approaching!")
            #increase difficulty
            difficulty +=1
        
        #if a new wave can spawn re-create the asteroids
        if canspawn == True:  
            
            #create a setback so they dont overlap
            setback = canvas.winfo_reqwidth()
            for x in range(len(asteroids)):
                #go through all asteroids and make them not destroyed
                asteroids[x].undestroy()
                #create new stats for the asteroid
                asteroids[x].Generate()
                #check if the asteroid can spawn there
                checkspawn(asteroids[x])
                #add to the set back
                setback += asteroids[x].getWidth()
                #apply the setback
                asteroids[x].setxPos(setback + 100)
                #make the asteroid visible
                asteroids[x].SpawnAsteroid()
                #set the speed of the asteroid
                asteroids[x].setSpeed(asteroid_speed)
                #move the asteroid
                asteroids[x].moveAsteroid()
                
        #if the first asteroid passes the right wall remove the text on screen      
        if asteroids[0].getxPos() <= canvas.winfo_reqwidth():
            canvas.itemconfig(text, text = "")
                
                
           
    #call to check if an asteroid hits a wall            
    AsterWallchk()
    asterspawntmrid = root.after(asteroid_spawn_rate, create_Asteroid)
    
#create a function that shoots a laser on a key press               
def onkeypress(event):
    global bullx
    global bully
    #if the space bar is pressed shoot the laser
    if event.keysym == 'space' and B.isFired() == False:
        #set the location of the laser infront of the player
        B.setLocation(bullx + P.getWidth() - 10 , bully + P.getHeight() // 2 - 10)
        
        #play sound effect
        playlasereffect()
        #fire the laser
        B.fireBullet()
        #check if it hits right wall
        bulletTimer()
        
        
bullx = 0
bully = 0
#create a function that moves the player on mouse movement
def onmousemove(event):
    global bullx
    global bully
    
    #get the x and y of the mouse, positioned at the center of the ship 
    x = event.x - P.getWidth() // 2
    y = event.y - P.getHeight() // 2
    
    #set screen boundaries, and where the player ship should be if the mouse goes past the boundaries 
    if x <= 0:
        x = 0
    elif x + P.getWidth() >= canvas.winfo_width():
        x = canvas.winfo_reqwidth() - P.getWidth() - 5
    
    if y <= imgTitle.height():
        y = imgTitle.height()
        
    elif y + P.getHeight() >= canvas.winfo_height():
        y = canvas.winfo_height() - P.getHeight() - 5
    
    #set the location of the player ship, on the mouse
    P.setLocation(x,y)
    
    bullx = x + 10
    bully = y


    
    
        
    
    

root = Tk()
root.title('Asterpocalypse')
root.protocol('WM_DELETE_WINDOW', exit_program)
#bind the keyboard and mouse to functions
root.bind('<KeyPress>', onkeypress)
root.bind('<Motion>', onmousemove)

#set a background
imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')

#center the window
root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))

canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()

background_list = [0] * 2
xpos = [0, imgBackground.width()]

#create the background frames
for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')

#set the score, and display it
score = 0
score_text = canvas.create_text(canvas.winfo_reqwidth() //8 , 35, text = score, fill = "orange", font = "neuropol-Regular 30")
text = canvas.create_text(canvas.winfo_reqwidth() //2 , canvas.winfo_reqheight() // 2, text = "", fill = "orange", font = "neuropol-Regular 30")


asteroids = []
#initialize player and laser(bullet) objects
B = Bullet(canvas)
P = Player(canvas, y = 0 + imgTitle.height())

#start these timers
background_timer()
create_Asteroid()
Collisionchk()
scoretimer()
bulletTimer()
frame()

root.mainloop()