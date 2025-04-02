from tkinter import PhotoImage


class Player:
    '''
    A class used to represent a player ship
    
    Attributes
    ----------
    __xPos: int
        the x position of the ship
    __yPos: int
        the y position of the ship
    __width: int
        the width of the ship
    __height: int
        the height of the ship
    __PlayerHealth: int
        the health players havem set at 10
    __Lives: int
        the lives players have set at 3
    __counter: int
        a counter to track what frame to show of the ship
    __canvas : tkinter module
            the window in which this bullet will be located
        
    Methods
    -------
    animate(self, full):
        animates the ship by going through a list of frames
        
    setLocation(self, x, y):
        moves the ship to the location given in the parameters
        
    getHealth(self):
        gets the current health value
        
    setHealth(self, health):
        sets the new health value
        
    getLives(self):
        get the current lives value
        
    setLives(self,lives):
        sets the current lives value
        
    getWidth(self):
        gets the current width value in pixels
        
    getHeight(self):
        gets the current height value in pixels
        
    resethealth(self):
        resets the health to 10
        
    takeDamage(self):
        subtracts 1 from the current health, and determines whether a life should be taken or not
        
    getX(self):
        gets the current x value
        
    getY(self):
        gets the current y value
        
    reset(self):
        resets all the stats to the original values
        
    resetlocation(self):
        resets location the the middle of the left side of the window
    
    '''
    def __init__(self, canvasarg, x = 0, y = 0):
        '''
        PARAMETERS:
        -----------
        x: int
            The starting x location of the ship
        y: int
            The starting y location of the ship
        canvas : tkinter module
            the window in which this player will be located
        '''
        self.__imgPlayer = [PhotoImage(file ="images/spaceship.png"), PhotoImage(file ="images/spaceship2.png"), PhotoImage(file ="images/spaceship3.png"), PhotoImage(file ="images/spaceship4.png"), PhotoImage(file = "images/exploded_ship.png") ]
        self.__canvas = canvasarg
        self.__dead = False
        self.__xPos = x
        self.__yPos = y
        self.__width = 0
        self.__height = 0
        self.__PlayerHealth = 10
        self.__Lives = 3
        self.__counter = 0
        self.__Lives_img = [PhotoImage(file ="images/lives1.png"), PhotoImage(file ="images/lives2.png"), PhotoImage(file ="images/lives3.png")]
        
        self.__Healthimg = [PhotoImage(file = "images/health0.png"), PhotoImage(file = "images/health1.png"), PhotoImage(file = "images/health2.png"), PhotoImage(file = "images/health3.png"), PhotoImage(file = "images/health4.png"),
                            PhotoImage(file = "images/health5.png"), PhotoImage(file = "images/health6.png"), PhotoImage(file = "images/health7.png") ,PhotoImage(file = "images/health8.png"), PhotoImage(file = "images/health9.png"), 
                            PhotoImage(file = "images/health10.png")]
        
        self.__playerimg = self.__canvas.create_image(self.__xPos, self.__yPos, image = self.__imgPlayer[0], anchor='nw')
        
        self.__Health_Bar =  self.__canvas.create_image(self.__canvas.winfo_reqwidth() - self.__Healthimg[10].width() + 40, 15, image = self.__Healthimg[10])
        
        self.__Lives_Bar = self.__canvas.create_image(self.__canvas.winfo_reqwidth() - self.__Lives_img[2].width() + 25, self.__Healthimg[10].height() + 25, image = self.__Lives_img[2])
    
    def animate(self, full):
        '''
        animates the ship
        
        parameters
        ----------
        full : boolean
            can the player shoot, animate the frames based on whether it is true/false
        '''
        if full == False: 
            if self.__counter == 0:
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[0])
                self.__counter = 1
            else:
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[1])
                self.__counter = 0
        else:
            if self.__counter == 0:
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[2])
                self.__counter = 1
            else:
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[3])
                self.__counter = 0
            
        
    
   
    def setLocation(self, x, y):
        '''
        Sets the location of the player
        PARAMETERS:
        -----------
        x: int
            The x location of the ship
        y: int
            The y location of the ship
            
        '''
        self.__xPos = x
        self.__yPos = y
        self.__canvas.coords(self.__playerimg, self.__xPos, self.__yPos)
    
    def getHealth(self):
        '''
        Returns the health of the player.
        RETURNS:
        --------
        int
            The value of the players health
        '''
        return self.__PlayerHealth
    
    def setHealth(self, health):
        '''
        Sets the health of the player
        PARAMETERS:
        -----------
        health: int
            The new health of the ship
        
        '''
        self.__PlayerHealth = health
    
    def getLives(self):
        '''
        Returns the lives of the player.
        RETURNS:
        --------
        int
            The value of the players lives
        '''
        return self.__Lives
    
    def setLives(self,lives):
        '''
        Sets the lives of the player
        PARAMETERS:
        -----------
        lives: int
            The new total lives of the ship
        
        '''
        self.__Lives = lives
        
      
    def getWidth(self):
        '''
        Returns the width of the player.
        RETURNS:
        --------
        int
            The value of the players width in pixels
        '''
        return self.__imgPlayer[0].width()
    
    def getHeight(self):
        '''
        Returns the height of the player.
        RETURNS:
        --------
        int
            The value of the players height in pixels
        '''
        return self.__imgPlayer[0].height()
    
    def resethealth(self):
        '''
        resethealth(self):
            resets the health to 10
        '''
        hp = 10
        self.setHealth(hp)
        self.__canvas.itemconfig(self.__Health_Bar, image = self.__Healthimg[hp])
    
    def takeDamage(self):
        '''
        takeDamage(self):
            subtracts 1 from the current health, and determines whether a life should be taken or not
        '''
        
        hp = self.getHealth()
        L = self.getLives() 
        
        hp -= 1
        if hp <= 0:
            L -= 1
            self.setLives(L)
            if self.getLives() - 1 >= 0:
                self.__canvas.itemconfig(self.__Lives_Bar, image = self.__Lives_img[self.getLives() - 1]) 
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[4])
            else:
                self.__canvas.itemconfig(self.__Lives_Bar, image = self.__Lives_img[0])
                self.__canvas.itemconfig(self.__playerimg, image = self.__imgPlayer[4])
                return True
        else:
            self.__canvas.itemconfig(self.__Health_Bar, image = self.__Healthimg[hp])
            
        self.setHealth(hp)
        
    def getX(self):
        '''
        Returns the x value of the player.
        RETURNS:
        --------
        int
            The x value of the players 
        '''
        return self.__xPos
    
    def getY(self):
        '''
        Returns the y value of the player.
        RETURNS:
        --------
        int
            The y value of the players 
        '''
        return self.__yPos
    
    def reset(self):
        '''
        resets the players stats to their original values
        '''
        self.resethealth()
        self.setLives(3)
        self.__canvas.itemconfig(self.__Lives_Bar, image = self.__Lives_img[2])
        
    def resetlocation(self):
        '''
        resets the location of the player to the middle of the left side of the screen
        '''
        self.setLocation(0, self.__canvas.winfo_reqheight() // 2)
        
            
    