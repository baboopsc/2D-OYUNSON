from tkinter import PhotoImage

class Bullet:
   '''
    Bir mermiyi temsil etmek için kullanılan bir sınıf

    Özellikler
    ----------
    __x:int
        merminin x değeri
    __y:int
        merminin y değeri
    __width:int
        merminin genişliği
    __height:int
        merminin yüksekliği
    __fired:boolean
        mermi ateşlendi mi
    __timerid:none
        zamanlayıcı
    __canvas : tkinter modülü
        bu merminin yer alacağı pencere

    Yöntemler
    -------
    getX(self):
        mevcut x değerini alır
    getY(self):
        mevcut y değerini alır
    setX(self, x):
        yeni x değerini ayarlar
    setY(self, y):
        yeni y değerini ayarlar
    setLocation(self, x, y):
        merminin yerini x ve y eksenlerinde ayarlar
    fireBullet(self):
        mermiyi ateşler ve ileriye hareket ettirir
    isFired(self):
        merminin ateşlenip ateşlenmediğini döndürür
    reset(self):
        merminin hareketini durdurur, zamanlayıcıyı durdurarak
    getWidth(self):
        merminin genişliğini piksel cinsinden alır
    getHeight(self):
        merminin yüksekliğini piksel cinsinden alır
'''

    def __init__(self, canvasarg):
       '''
        PARAMETRELER:
        -----------
        canvas : tkinter modülü
            bu merminin yer alacağı pencere
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
        Merminin x değerini döndürür.
        DÖNDÜRÜR:
        --------
        int
            Merminin x değeri
'''
        return self.__x
    
    def getY(self):
        
        return self.__y
    
    def setX(self, x):
       
        self.__x = x
    
    def setY(self, y):
      
        self.__y = y
    
    def setLocation(self, x, y):
       
        self.__x = x
        self.__y = y
        self.__canvas.coords(self.__imgBullet, self.__x, self.__y)
    
    def fireBullet(self):
       
        self.__fired = True
        self.__x += 5
        self.__canvas.itemconfig(self.__imgBullet, image = self.__img_bullet)
        self.__canvas.coords(self.__imgBullet, self.__x, self.__y)
        self.__timerid = self.__canvas.after(5, self.fireBullet)
    
    def isFired(self):
       
        return self.__fired
    
    def reset(self):
        self.__canvas.itemconfig(self.__imgBullet, image = self.__imgBlank)
        try:
            self.__timerid = self.__canvas.after_cancel(self.__timerid)
            self.__fired = False
        except ValueError:
            pass
    
    def getWidth(self):
        
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    
    
    
    
   '''
        alltxt.count("'") kadar döngü çalıştır:
            
            Eğer sayaç % 2 == 0 ise:
                pos = self.text.search("'", pos, "end")
                pos = "{} + {} chars".format(pos,1)
                
                Eğer flag False ise ve x, alltxt.count("'") - 1'e eşitse:
                    pos_end = self.text.search("'", pos, "end")
                    pos_end = "{} + {} chars".format(pos_end,1)
                    pos = "{} - {} chars".format(pos,1)
                    self.text.tag_add(tag,pos,pos_end)
                    flag = True
                
            Aksi takdirde:
                pos_end = self.text.search("'", pos, "end")
                print(pos_end)
                Eğer self.text.compare(self.text.search("'", pos, "end"), '>' , self.text.search('\n', pos, 'end')) == True:
                    pos = pos_end
                    flag = False
                    
                Aksi takdirde:
                    pos_end = "{} + {} chars".format(pos_end,1)
                    pos = "{} - {} chars".format(pos,1)
                    self.text.tag_add(tag,pos,pos_end)
                      
                pos = "{}".format(pos_end)
            sayaç += 1   
'''
