from tkinter import PhotoImage


class Player:
    '''
    Bir oyuncu gemisini temsil eden sınıf

    Nitelikler
    ----------
    __xPos: int
        geminin x konumu
    __yPos: int
        geminin y konumu
    __width: int
        geminin genişliği
    __height: int
        geminin yüksekliği
    __PlayerHealth: int
        oyuncunun sağlığı, varsayılan olarak 10
    __Lives: int
        oyuncunun can sayısı, varsayılan olarak 3
    __counter: int
        hangi gemi karesinin gösterileceğini izlemek için sayaç
    __canvas : tkinter modülü
        bu merminin içinde bulunacağı pencere

    Metotlar
    -------
    animate(self, full):
        gemiyi, bir dizi kareyi döndürerek canlandırır

    setLocation(self, x, y):
        gemiyi verilen konuma taşır

    getHealth(self):
        mevcut sağlık değerini döndürür

    setHealth(self, health):
        yeni sağlık değerini ayarlar

    getLives(self):
        mevcut can değerini döndürür

    setLives(self,lives):
        mevcut can değerini ayarlar

    getWidth(self):
        piksel cinsinden mevcut genişlik değerini döndürür

    getHeight(self):
        piksel cinsinden mevcut yükseklik değerini döndürür

    resethealth(self):
        sağlığı 10'a sıfırlar

    takeDamage(self):
        mevcut sağlıktan 1 çıkarır ve bir canın alınıp alınmayacağını belirler

    getX(self):
        mevcut x değerini döndürür

    getY(self):
        mevcut y değerini döndürür

    reset(self):
        tüm istatistikleri orijinal değerlere sıfırlar

    resetlocation(self):
        konumu pencerenin sol tarafının ortasına sıfırlar

    '''

    def __init__(self, canvasarg, x=0, y=0):
        '''
        PARAMETRELER:
        ------------
        x: int
            Geminin başlangıç x konumu
        y: int
            Geminin başlangıç y konumu
        canvas : tkinter modülü
            bu oyuncunun yer alacağı pencere
        '''
        self.__imgPlayer = [PhotoImage(file="images/spaceship.png"), PhotoImage(file="images/spaceship2.png"),
                            PhotoImage(file="images/spaceship3.png"), PhotoImage(file="images/spaceship4.png"),
                            PhotoImage(file="images/exploded_ship.png")]
        self.__canvas = canvasarg
        self.__dead = False
        self.__xPos = x
        self.__yPos = y
        self.__width = 0
        self.__height = 0
        self.__PlayerHealth = 10
        self.__Lives = 3
        self.__counter = 0
        self.__Lives_img = [PhotoImage(file="images/lives1.png"), PhotoImage(file="images/lives2.png"),
                            PhotoImage(file="images/lives3.png")]

        self.__Healthimg = [PhotoImage(file="images/health0.png"), PhotoImage(file="images/health1.png"),
                            PhotoImage(file="images/health2.png"), PhotoImage(file="images/health3.png"),
                            PhotoImage(file="images/health4.png"),
                            PhotoImage(file="images/health5.png"), PhotoImage(file="images/health6.png"),
                            PhotoImage(file="images/health7.png"), PhotoImage(file="images/health8.png"),
                            PhotoImage(file="images/health9.png"),
                            PhotoImage(file="images/health10.png")]

        self.__playerimg = self.__canvas.create_image(self.__xPos, self.__yPos, image=self.__imgPlayer[0], anchor='nw')

        self.__Health_Bar = self.__canvas.create_image(
            self.__canvas.winfo_reqwidth() - self.__Healthimg[10].width() + 40, 15, image=self.__Healthimg[10])

        self.__Lives_Bar = self.__canvas.create_image(self.__canvas.winfo_reqwidth() - self.__Lives_img[2].width() + 25,
                                                      self.__Healthimg[10].height() + 25, image=self.__Lives_img[2])

    def animate(self, full):
        '''
        Gemiyi canlandırır

        Parametreler
        ------------
        full : boolean
            Oyuncu ateş edebilir mi, True/False durumuna göre kareleri canlandırır
        '''
        if full == False:
            if self.__counter == 0:
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[0])
                self.__counter = 1
            else:
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[1])
                self.__counter = 0
        else:
            if self.__counter == 0:
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[2])
                self.__counter = 1
            else:
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[3])
                self.__counter = 0

    def setLocation(self, x, y):
        '''
        Oyuncunun konumunu ayarlar
        PARAMETRELER:
        ------------
        x: int
            Geminin x konumu
        y: int
            Geminin y konumu

        '''
        self.__xPos = x
        self.__yPos = y
        self.__canvas.coords(self.__playerimg, self.__xPos, self.__yPos)

    def getHealth(self):
        '''
        Oyuncunun sağlığını döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun sağlık değeri
        '''
        return self.__PlayerHealth

    def setHealth(self, health):
        '''
        Oyuncunun sağlığını ayarlar
        PARAMETRELER:
        ------------
        health: int
            Geminin yeni sağlık değeri

        '''
        self.__PlayerHealth = health

    def getLives(self):
        '''
        Oyuncunun can sayısını döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun can değeri
        '''
        return self.__Lives

    def setLives(self, lives):
        '''
        Oyuncunun can sayısını ayarlar
        PARAMETRELER:
        ------------
        lives: int
            Geminin yeni toplam can değeri

        '''
        self.__Lives = lives

    def getWidth(self):
        '''
        Oyuncunun genişliğini döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun piksel cinsinden genişliği
        '''
        return self.__imgPlayer[0].width()

    def getHeight(self):
        '''
        Oyuncunun yüksekliğini döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun piksel cinsinden yüksekliği
        '''
        return self.__imgPlayer[0].height()

    def resethealth(self):
        '''
        resethealth(self):
            Sağlığı 10’a sıfırlar
        '''
        hp = 10
        self.setHealth(hp)
        self.__canvas.itemconfig(self.__Health_Bar, image=self.__Healthimg[hp])

    def takeDamage(self):
        '''
        takeDamage(self):
            Mevcut sağlıktan 1 çıkarır ve bir can kaybedilip kaybedilmeyeceğini belirler
        '''

        hp = self.getHealth()
        L = self.getLives()

        hp -= 1
        if hp <= 0:
            L -= 1
            self.setLives(L)
            if self.getLives() - 1 >= 0:
                self.__canvas.itemconfig(self.__Lives_Bar, image=self.__Lives_img[self.getLives() - 1])
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[4])
            else:
                self.__canvas.itemconfig(self.__Lives_Bar, image=self.__Lives_img[0])
                self.__canvas.itemconfig(self.__playerimg, image=self.__imgPlayer[4])
                return True
        else:
            self.__canvas.itemconfig(self.__Health_Bar, image=self.__Healthimg[hp])

        self.setHealth(hp)

    def getX(self):
        '''
        Oyuncunun x değerini döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun x değeri
        '''
        return self.__xPos

    def getY(self):
        '''
        Oyuncunun y değerini döndürür.
        DÖNÜŞ:
        ------
        int
            Oyuncunun y değeri
        '''
        return self.__yPos

    def reset(self):
        '''
        Oyuncunun istatistiklerini başlangıç değerlerine sıfırlar
        '''
        self.resethealth()
        self.setLives(3)
        self.__canvas.itemconfig(self.__Lives_Bar, image=self.__Lives_img[2])

    def resetlocation(self):
        '''
        Oyuncunun konumunu ekranın sol tarafının ortasına sıfırlar
        '''
        self.setLocation(0, self.__canvas.winfo_reqheight() // 2)
