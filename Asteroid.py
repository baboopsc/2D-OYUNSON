from tkinter import PhotoImage
import random

class Asteroid:
    '''
    Bir asteroid sınıfını temsil etmek için kullanılan bir sınıf
    
    Attributes
    ----------
    __Points: int listesi
        asteroidin 3 olası puan değerlerini tutar
        
    __Hitpoints: int listesi
        asteroidlerin 3 olası sağlık değerlerini tutar
        
    __Canvas: tkinter modülü
        bu mermi'nin yer alacağı pencere
        
    __height_restriction: int
        minimum y değeri
        
    __Asteroid: 2D int listesi
        asteroidin istatistiklerini tutacak bir 2D liste
        
    __yPos: int
        asteroidin y pozisyonu
        
    __xPos: int
        asteroidin x pozisyonu
        
    __destroyed: boolean
        asteroidin durumu
        
    __timerId: none
        zamanlayıcı
        
    __asteroidspeed: int
        asteroidin temel hızı 
        
    methods
    -------
    SpawnAsteroid(self):
        asteroidin resmini görünür yapar
        
    getSpeed(self):
        asteroidin mevcut hızını alır
        
    setSpeed(self, speed):
        asteroidin yeni hızını ayarlar
        
    moveAsteroid(self):
        asteroidin sola hareket etmesini sağlar
         
    genYSpawn(self, y1 = 0 , y2 = 0, x1 = 0, x2 = 0):
        asteroidin doğma konumunu oluşturur
        
    Generate(self):
        asteroidin istatistiklerini oluşturur
        
    getyPos(self):    
        mevcut y pozisyonunu alır
        
    setyPos(self, y):
        yeni y pozisyonunu ayarlar
        
    getxPos(self):
        mevcut x pozisyonunu alır
        
    setxPos(self, x):
        yeni x pozisyonunu ayarlar
        
    setAsteroidimg(self, size):
        asteroidin resmini ayarlar
        
    getAstroidimg(self):
        asteroidin mevcut resmini alır
        
    setAsteroidhp(self, size):
        asteroidin sağlığını ayarlar
        
    getAsteroidhp(self):
        asteroidin mevcut sağlığını alır
        
    setAsteroidpoints(self,size):
        asteroidin değerini ayarlar
        
    getAsteroidpoints(self):
        asteroidin puan değerini alır
        
    getWidth(self):
        asteroidin genişliğini alır
        
    getHeight(self):
        asteroidin yüksekliğini alır
        
    destroy(self):
        asteroidin durumunu True yapar
        
    isdestroyed(self):
        asteroidin durumunu döndürür
        
    undestroy(self):
        asteroidin durumunu False yapar
        
    makeinvis(self, setback = 0):
        asteroidin ekranın dışına hareket etmesini sağlar
        
    TakeDamage(self):
        asteroidin sağlığından 1 azaltır ve yok olup olmayacağını belirler
    
    '''
    
    def __init__(self, canvasarg, height_restriction):
        '''
        PARAMETRELER:
        -------------
        canvas : tkinter modülü
            bu merminin yer alacağı pencere
        height_restriction: int
            minimum y değeri
        
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
        asteroidin resmini görünür yapar
        '''
        self.__asteroidimg = self.__Canvas.create_image(self.__Canvas.winfo_reqwidth(), self.__Canvas.winfo_reqheight() // 2, anchor = "nw",  image = self.getAstroidimg())    
            
    def getSpeed(self):
        '''
        asteroidin hızını döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin hız değeri
        '''
        return self.__asteroidspeed
    
    def setSpeed(self, speed):
        '''
        asteroidin hızını ayarlar
        PARAMETRELER:
        -------------
        speed: int
            asteroidin yeni hızı
        
        '''
        self.__asteroidspeed = speed
        
    def moveAsteroid(self):
        '''
        asteroidin sola hareket etmesini sağlar, her ___ms de 5 piksel sola hareket eder (zamanlama, kodlayıcının girdiği değere göre değişir, varsayılan olarak 20)
        '''
        
        self.__xPos -= 5
        self.__Canvas.coords(self.__asteroidimg, self.__xPos, self.__yPos)
        speed = self.getSpeed()
            
        self.__timerId = self.__Canvas.after(speed, self.moveAsteroid)
    
    def genYSpawn(self, y1 = 0 , y2 = 0, x1 = 0, x2 = 0):
        '''
        asteroidin doğamayacağı bölgeyi belirler
        geçerli bir konum üretir ve döndürür
        PARAMETRELER:
        -------------
        y1: int
            Üst
        y2: int
            Alt
        x1: int
            Sol
        x2: int
            Sağ
        
        asteroidin doğacağı y değeri döndürülür
        DÖNDÜRÜR:
        --------
        int
            asteroidin doğacağı y değeri piksel olarak
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
        boyutu rastgele seçer ve asteroidin istatistiklerini buna göre oluşturur
        '''
        
        size = random.randint(0,2)
        
        self.setAsteroidimg(size)
        self.setAsteroidhp(size)
        self.setAsteroidpoints(size)
        
        
    
     
    #------------------------------------------------------- 
    def getyPos(self):
        '''
        asteroidin y değerini döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin y değeri
        '''
        return self.__yPos
    
    def setyPos(self, y):
        '''
        asteroidin y değerini ayarlar
        PARAMETRELER:
        -------------
        y: int
            asteroidin yeni y değeri
        
        '''
        self.__yPos = y
    
    #------------------------------------------------------- 
    def getxPos(self):
        '''
        asteroidin x değerini döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin x değeri
        '''
        return self.__xPos
    
    def setxPos(self, x):
        '''
        asteroidin x değerini ayarlar
        PARAMETRELER:
        -------------
        x: int
            asteroidin yeni x değeri
        
        '''
        self.__xPos = x
             
    #------------------------------------------------------- 
    def setAsteroidimg(self, size):
        self.__Asteroid[0][0] = self.__imgAsteroid[size]
        
    def getAstroidimg(self):
        '''
        asteroidin resmini döndürür.
        DÖNDÜRÜR:
        --------
        photoimage
            asteroidin resmi
        '''
        return self.__Asteroid[0][0]
    #------------------------------------------------------- 
    
    def setAsteroidhp(self, size):
        '''
        asteroidin sağlığını ayarlar
        PARAMETRELER:
        -------------
        size: int
            asteroidin yeni sağlığı
        
        '''
        self.__Asteroid[0][1] = self.__Hitpoints[size]
        
    def getAsteroidhp(self):
        '''
        asteroidin sağlığını döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin sağlığı
        '''
        return self.__Asteroid[0][1]
    #------------------------------------------------------- 
      
    def setAsteroidpoints(self,size):
        '''
        asteroidin puanını ayarlar
        PARAMETRELER:
        -------------
        size: int
            asteroidin yeni puanı
        
        '''
        self.__Asteroid[0][2] = self.__Points[size]
        
    def getAsteroidpoints(self):
        '''
        asteroidin puanını döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin puanı
        '''
        return self.__Asteroid[0][2]
    #------------------------------------------------------- 
    def getWidth(self):
        '''
        asteroidin genişliğini döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin genişliği piksel olarak
        '''
        img = self.getAstroidimg()
        return img.width()
    
    def getHeight(self):
        '''
        asteroidin yüksekliğini döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin yüksekliği piksel olarak
        '''
        img = self.getAstroidimg()
        return img.height()
    #-------------------------------------------------------
    def destroy(self):
        '''
        asteroidin durumunu True yapar
        '''
        self.__destroyed = True
        
    def isdestroyed(self):
        '''
        asteroidin durumunu döndürür.
        DÖNDÜRÜR:
        --------
        bool
            asteroidin durumu
        '''
        return self.__destroyed
    
    def undestroy(self):
        '''
        asteroidin durumunu False yapar
        '''
        self.__destroyed = False
        
    def makeinvis(self, setback = 0):
        '''
        asteroidin hareketini durdurur
        ve sağdaki ekranın dışına yerleştirir
        PARAMETRELER:
        -------------
        setback: int
            asteroidin x pozisyonundaki geri çekilme miktarı
        
        '''
        try:
            self.__timerId = self.__Canvas.after_cancel(self.__timerId) 
        except ValueError:
            pass
        
        
        self.setxPos(self.__Canvas.winfo_reqwidth() + self.getWidth() + setback)
        self.__Canvas.coords(self.__asteroidimg, self.__xPos, self.getyPos())
        
        
    def TakeDamage(self):
        '''
        asteroidin sağlığından 1 azaltır ve yok olup olmayacağını belirler. 
        yok olduysa, asteroidin puanını döndürür.
        DÖNDÜRÜR:
        --------
        int
            asteroidin puanı
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
