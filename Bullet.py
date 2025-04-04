from tkinter import PhotoImage

class Bullet:
    '''
    A class used to represent a bullet
    
    Attributes
    ----------
    __x:int
        the x value of the bullet
    __y:int
        the y value of the bullet
    __width:int
        the width of the bullet
    __height:int
        the height of the bullet
    __fired:boolean
        is bullet fired
    __timerid:none
        the timer
    __canvas : tkinter module
        the window in which this bullet will be located
        
    Methods
    -------
    getX(self):
        gets the current x value
    getY(self):
        gets the current y value
    setX(self, x):
        set the new x value
    setY(self, y):
        sets the new y value
    setLocation(self, x, y):
        sets the location of the bullet, on the x and y axis
    fireBullet(self):
        fires the bullet, and moves it forwards
    isFired(self):
        returns whether the bullet is fired or not
    reset(self):
        stops the bullet from moving, by stopping the timer
    getWidth(self):
        get the width of the bullet in pixels
    getHeight(self):
        get the height of the bullet in pixels
    '''
    def __init__(self, canvasarg):
        '''
        PARAMETERS:
        -----------
        canvas : tkinter module
            the window in which this bullet will be located
        '''
        self.__canvas = canvasarg
        self.__x = 0
        self.__y = 0
        self.__img_bullet = PhotoImage(file = "images/laserbeam_red.png")
        self.__imgBlank = PhotoImage(file = "images/blank.png")
        self.__width = self.__img_bullet.width()
        self.__height = self.__img_bullet.height()
        
        self.__fired = False
        
        self.__timerid = None
        
        self.__imgBullet = self.__canvas.create_image(self.__x - self.__img_bullet.width(), self.__y - self.__img_bullet.height(), image = self.__img_bullet, anchor='nw')
    
    def getX(self):
        '''
        Returns the x value of the bullet.
        RETURNS:
        --------
        int
            The x value of the bullet
        '''
        return self.__x
    
    def getY(self):
        '''
        Returns the y value of the bullet.
        RETURNS:
        --------
        int
            The y value of the bullet
        '''
        return self.__y
    
    def setX(self, x):
        '''
        Sets the x value of the bullet
        PARAMETERS:
        -----------
        x: int
            The new x value of the bullet
        '''
        self.__x = x
    
    def setY(self, y):
        '''
        Sets the y value of the bullet
        PARAMETERS:
        -----------
        y: int
            The new y value of the bullet
        '''
        self.__y = y
    
    def setLocation(self, x, y):
        '''
        Sets the x & y values of the bullet
        PARAMETERS:
        -----------
        x: int
            The new x value of the bullet
        y:int
            the new y value of the bullet
        '''
        self.__x = x
        self.__y = y
        self.__canvas.coords(self.__imgBullet, self.__x, self.__y)
    
    def fireBullet(self):
        '''
        fires the bullet and moves it forward 5 pixels every 5ms
        '''
        self.__fired = True
        self.__x += 5
        self.__canvas.itemconfig(self.__imgBullet, image = self.__img_bullet)
        self.__canvas.coords(self.__imgBullet, self.__x, self.__y)
        self.__timerid = self.__canvas.after(5, self.fireBullet)
    
    def isFired(self):
        '''
        Returns if the bullet is fired
        RETURNS:
        --------
        boolean
            The state of the bullet
        '''
        return self.__fired
    
    def reset(self):
        '''
        stops the bullet from moving, by stopping the timer
        '''
        self.__canvas.itemconfig(self.__imgBullet, image = self.__imgBlank)
        try:
            self.__timerid = self.__canvas.after_cancel(self.__timerid)
            self.__fired = False
        except ValueError:
            pass
    
    def getWidth(self):
        '''
        Returns the width of the bullet.
        RETURNS:
        --------
        int
            The  width of the bullet in pixels
        '''
        return self.__width
    
    def getHeight(self):
        '''
        Returns the height of the bullet.
        RETURNS:
        --------
        int
            The height of the bullet in pixels
        '''
        return self.__height
    
    
    
    
    
    '''
        for x in range(alltxt.count("'")):
            
            if counter % 2 == 0:
                pos = self.text.search("'", pos, "end")
                pos = "{} + {} chars".format(pos,1)
                
                if flag == False and x == alltxt.count("'") -1:
                    pos_end = self.text.search("'", pos, "end")
                    pos_end = "{} + {} chars".format(pos_end,1)
                    pos = "{} - {} chars".format(pos,1)
                    self.text.tag_add(tag,pos,pos_end)
                    flag = True
                
            else:
                pos_end = self.text.search("'", pos, "end")
                print(pos_end)
                if self.text.compare(self.text.search("'", pos, "end"), '>' , self.text.search('\n', pos, 'end')) == True:
                    pos = pos_end
                    flag = False
                    
                else:
                    pos_end = "{} + {} chars".format(pos_end,1)
                    pos = "{} - {} chars".format(pos,1)
                    self.text.tag_add(tag,pos,pos_end)
                      
                pos = "{}".format(pos_end)
            counter += 1   
            '''