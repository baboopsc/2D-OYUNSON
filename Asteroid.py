from tkinter import PhotoImage
import random

class Asteroid:
    '''
    A class used to represent an asteroid
    
    Attributes
    ----------
    __Points: list of int
        stores the 3 possible point values of the asteroid
        
    __Hitpoints: list of int
        stores the 3 possible health values of the asteroids
        
    __Canvas: tkinter module
        the window in which this bullet will be located
        
    __height_restriction: int
        the minimum y value
        
    __Asteroid: 2D list of int
        a 2d  list to hold the stats of the asteroid
        
    __yPos: int
        the yposition of the asteroid
        
    __xPos: int
        the x position of the asteroid
        
    __destroyed: boolean
        the state of the asteroid
        
    __timerId: none
        the timer
    
    __asteroidspeed: int
        the base speed of the asteroid 
        
    methods
    -------
    SpawnAsteroid(self):
        make the image of the asteroid visible
        
    getSpeed(self):
        get the current speed of the asteroid
        
    setSpeed(self, speed):
        set the new speed of the asteroid
        
    moveAsteroid(self):
         move the asteroid to the left
         
    genYSpawn(self, y1 = 0 , y2 = 0, x1 = 0, x2 = 0):
        generate the spawn location of the asteroid
        
    Generate(self):
        generate the stats of the asteroid
        
    getyPos(self):    
        gets the current y position
        
    setyPos(self, y):
        sets the new y position
        
    getxPos(self):
        gets the current x position
        
    setxPos(self, x):
        sets the new x position
        
    setAsteroidimg(self, size):
        sets the image of the asteroid
        
    getAstroidimg(self):
        gets the current image of the asteroid
        
    setAsteroidhp(self, size):
        sets the Asteroids health
        
    getAsteroidhp(self):
        gets the current hp of the asteroid
        
    setAsteroidpoints(self,size):
        sets the points the asteroid is worth
        
    getAsteroidpoints(self):
        gets the points value of the asteroid
        
    getWidth(self):
        gets the width of the asteroid
        
    getHeight(self):
        gets the height of the asteroid
        
    destroy(self):
        sets the state of the asteroid to True
        
    isdestroyed(self):
        returns the state of the asteroid
        
    undestroy(self):
        sets the state of the asteroid to False
        
    makeinvis(self, setback = 0):
        moves the asteroid off screen
        
    TakeDamage(self):
        removes 1 health from the asteroid and determines if it should be destroyed
    
    '''
    
    def __init__(self, canvasarg, height_restriction):
        '''
        PARAMETERS:
        -----------
        canvas : tkinter module
            the window in which this bullet will be located
        height_restriction: int
            the minimum y value
        
        '''
        
        self.__imgAsteroid = [PhotoImage(file = "images/asteroid0.png"), PhotoImage(file = "images/asteroid1.png"), PhotoImage(file = "images/asteroid2.png"), PhotoImage(file = "images/explosion0.png"), PhotoImage(file = "images/blank.png")]
        self.__Points = [10,20,30]
        self.__Hitpoints = [1,2,3]
        self.__Canvas = canvasarg
        self.__height_restriction = height_restriction
        self.__Asteroid = [[0 for cols in range(3)]for rows in range(1)]
        self.__yPos = 0
        self.__xPos = canvasarg.winfo_reqwidth() + 180
        self.__destroyed = False
        self.__asteroidimg = None
        self.__timerId = None
        self.__asteroidspeed = 20
       
    def SpawnAsteroid(self):
        '''
        make the image of the asteroid visible
        '''
        self.__asteroidimg = self.__Canvas.create_image(self.__Canvas.winfo_reqwidth(), self.__Canvas.winfo_reqheight() // 2, anchor = "nw",  image = self.getAstroidimg())    
            
    def getSpeed(self):
        '''
        Returns the speed of the asteroid.
        RETURNS:
        --------
        int
            The value of the asteroids speed
        '''
        return self.__asteroidspeed
    
    def setSpeed(self, speed):
        '''
        Sets the speed of the asteroid
        PARAMETERS:
        -----------
        speed: int
            The new speed of the asteroid
        
        '''
        self.__asteroidspeed = speed
        
    def moveAsteroid(self):
        '''
        move the asteroid to the left, 5 pixels every ___ms (the time it takes varies on the value that the coder inputs, set to 20 by default)
        '''
        
        self.__xPos -= 5
        self.__Canvas.coords(self.__asteroidimg, self.__xPos, self.__yPos)
        speed = self.getSpeed()
            
        self.__timerId = self.__Canvas.after(speed, self.moveAsteroid)
    
    def genYSpawn(self, y1 = 0 , y2 = 0, x1 = 0, x2 = 0):
        '''
        
        Sets the hitbox that the asteroid cannot spawn in asteroid
        generates a spawnable location and returns it
        PARAMETERS:
        -----------
        y1: int
            The top
        y2: int
            The bot
        x1: int
            The left
        x2: int
            The right
        
        Returns the y value the asteroid will spawn at
        RETURNS:
        --------
        int
            The y value the asteroid will spawn at in pixels
        '''
        width = self.getWidth()
        Yspawn = 0
        Ybottom = 0
        
        while Yspawn == 0 or Ybottom == 0 or Yspawn > y1 and Yspawn < y2 or Ybottom > y1 and Ybottom < y2:
            Yspawn = random.randint(self.__height_restriction.height(), self.__Canvas.winfo_reqheight() - width)
            Ybottom = Yspawn + width
            
            if self.getxPos() + self.getWidth() >= x1 and self.getxPos() <= x1 + x2:
                if Ybottom >= y1 and Yspawn <= y1 + y2:
                    Yspawn = 0
                
            
            
        self.setyPos(Yspawn) 
        return Yspawn
        
    def Generate(self):
        '''
        randomizes the size and generates the stats of the asteroid accordingly
        '''
        
        size = random.randint(0,2)
        
        self.setAsteroidimg(size)
        self.setAsteroidhp(size)
        self.setAsteroidpoints(size)
        
        
    
     
    #------------------------------------------------------- 
    def getyPos(self):
        '''
        Returns the y value of the asteroid.
        RETURNS:
        --------
        int
            The y value of the asteroid 
        '''
        return self.__yPos
    
    def setyPos(self, y):
        '''
        Sets the y value of the asteroid
        PARAMETERS:
        -----------
        y: int
            The new y value of the asteroid
        
        '''
        self.__yPos = y
    
    #------------------------------------------------------- 
    def getxPos(self):
        '''
        Returns the x value of the asteroid.
        RETURNS:
        --------
        int
            The x value of the asteroid 
        '''
        return self.__xPos
    
    def setxPos(self, x):
        '''
        Sets the x value of the asteroid
        PARAMETERS:
        -----------
        x: int
            The new x value of the asteroid
        
        '''
        self.__xPos = x
            
    #------------------------------------------------------- 
    def setAsteroidimg(self, size):
        self.__Asteroid[0][0] = self.__imgAsteroid[size]
        
    def getAstroidimg(self):
        '''
        Returns the image of the asteroid.
        RETURNS:
        --------
        photoimage
            The image of the asteroid 
        '''
        return self.__Asteroid[0][0]
    #------------------------------------------------------- 
    
    def setAsteroidhp(self, size):
        '''
        Sets the health of the asteroid
        PARAMETERS:
        -----------
        size: int
            The new health of the asteroid
        
        '''
        self.__Asteroid[0][1] = self.__Hitpoints[size]
        
    def getAsteroidhp(self):
        '''
        Returns the health of the asteroid.
        RETURNS:
        --------
        int
            The health of the asteroid
        '''
        return self.__Asteroid[0][1]
    #------------------------------------------------------- 
      
    def setAsteroidpoints(self,size):
        '''
        Sets the points of the asteroid
        PARAMETERS:
        -----------
        size: int
            The new points of the asteroid
        
        '''
        self.__Asteroid[0][2] = self.__Points[size]
        
    def getAsteroidpoints(self):
        '''
        Returns the points of the asteroid.
        RETURNS:
        --------
        int
            The points of the asteroid
        '''
        return self.__Asteroid[0][2]
    #------------------------------------------------------- 
    def getWidth(self):
        '''
        Returns the width of the asteroid.
        RETURNS:
        --------
        int
            The width of the asteroids in pixels
        '''
        img = self.getAstroidimg()
        return img.width()
    
    def getHeight(self):
        '''
        Returns the height of the asteroid.
        RETURNS:
        --------
        int
            The height of the asteroids in pixels
        '''
        img = self.getAstroidimg()
        return img.height()
    #-------------------------------------------------------
    def destroy(self):
        '''
        destroy(self):
        sets the state of the asteroid to True
        '''
        self.__destroyed = True
        
    def isdestroyed(self):
        '''
        Returns the state of the asteroid.
        RETURNS:
        --------
        bool
            The state of the asteroid
        '''
        return self.__destroyed
    
    def undestroy(self):
        '''
        sets the state of the asteroid to False
        '''
        self.__destroyed = False
        
    def makeinvis(self, setback = 0):
        '''
        stops moving the asteroid
        and places it beyond the right side of the window
        PARAMETERS:
        -----------
        setback: int
            The setback of the asteroids x postion
        
        '''
        try:
            self.__timerId = self.__Canvas.after_cancel(self.__timerId) 
        except ValueError:
            pass
        
        
        self.setxPos(self.__Canvas.winfo_reqwidth() + self.getWidth() + setback)
        self.__Canvas.coords(self.__asteroidimg, self.__xPos, self.getyPos())
        
        
    def TakeDamage(self):
        '''
        removes 1 health from the asteroid and determines if it should be destroyed. 
        if destroyed returns the points of the asteroid.
        RETURNS:
        --------
        int
            The points of the asteroid
        '''
        hp = self.getAsteroidhp()
        hp-=1
        if hp <= 0:
            self.setAsteroidimg(3)
            self.__Canvas.itemconfig(self.__asteroidimg, image = self.getAstroidimg())
            self.destroy()
            return self.getAsteroidpoints()
            
        else:
            
            self.setAsteroidhp(hp - 1)
            self.setAsteroidimg(hp - 1)
            self.__Canvas.itemconfig(self.__asteroidimg, image = self.getAstroidimg())
            
            self.setyPos(self.__yPos + self.__imgAsteroid[hp].height()//4)
            self.__Canvas.coords(self.__asteroidimg, self.__xPos, self.getyPos())
 
    
    
    