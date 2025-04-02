#// ALİ MUHSİN MIŞRAKLI / OKAN KARAHAN
#//Asterpocalypse Programı
#//02/04/2025
    
#import edilen tüm gerekli sınıfları dahil et
from tkinter import Tk, Canvas, PhotoImage, messagebox
from Bullet import Bullet
from Player import Player
from Asteroid import Asteroid
import pygame

#mixer'ı başlat
pygame.mixer.init()

#arka plan müziğini yükle ve tekrarlı çal
pygame.mixer.music.load("15 MilkyWay (Battle).mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(loops=-1)

#create a function to play a sound effect
def playlasereffect():
    #ses efektini başlat
    laser = pygame.mixer.Sound("064-laser.wav")
    #efekti çal
    pygame.mixer.Sound.play(laser)
 
#create a function to play a sound effect   
def playexplosioneffect():
    #ses efektini başlat
    explode = pygame.mixer.Sound("explosion.wav")
    #efekti çal
    pygame.mixer.Sound.play(explode)

#create a function to pause and un-pause the timers
def pausetimers(flag = True):
    global frametmrid
    global bullettmrid
    global collisionid
    global asterspawntmrid
    
    #pause veya un-pause yapılmak istenip istenmediğini kontrol et (true -> pause, false -> un-pause)
    if flag == True:
        try:
            #bu zamanlayıcıları durdur
            root.after_cancel(frametmrid)
            root.after_cancel(bullettmrid)
            root.after_cancel(collisionid)
            root.after_cancel(asterspawntmrid)
        except ValueError:
            pass
    else:
        #bu zamanlayıcıları çalıştır
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
    #hangi animasyonun oynatılacağını kontrol et ve onu çalıştır
    P.animate(B.isFired())
    frametmrid = root.after(125, frame)

#create a program to close the game
def exit_program():
    #bu zamanlayıcıları durdur
    root.after_cancel(btid)
    root.after_cancel(scoretmrid)
    #tüm diğer zamanlayıcıları durdur
    pausetimers()
    
    exit()

#create a program to reset the game
def reset(flag = True):
    global score
    global asteroid_spawn_rate
    global asteroid_speed
    #asteroidleri sağdaki duvara sıfırla ve offset yap
    widthsetback = 0
    for x in range(len(asteroids)):
        asteroids[x].destroy()
        widthsetback += asteroids[x].getWidth()
        asteroids[x].makeinvis(widthsetback)
        
    #lazeri sıfırla
    B.reset()
    
    #oyunu tamamen sıfırla, hızı temel hıza ayarla, ve skoru sıfırla
    if flag == True:
        asteroid_speed = 100
        asteroid_spawn_rate =2000
        score = 0
        canvas.itemconfig(score_text, text = score)

#create a function to check whether a player loses a life or has a game over       
def playerlives():

    global score
    
    #toplam hayatları kontrol et, eğer 0 ise tekrar oynamak isteyip istemediğini sor
    if P.getLives() == 0:
        #zamanlayıcıları durdur, oyuncunun sağlık/hayat durumunu sıfırla, oyunu yumuşak bir şekilde sıfırla
        pausetimers()
        P.reset()
        reset(False)
        flag = messagebox.askyesno("Asterpocalypse", "Senin " + str(score) + " Puanın Var\nHayatın bitti, tekrar oynamak ister misin?")
        #oyunu tamamen sıfırla
        reset()
        #oyuncu konumunu sıfırla
        P.resetlocation()
        #hayır derse, programı kapat
        if flag == False:
            exit_program()
        #zamanlayıcıları çalıştır
        pausetimers(False)
            
    #eğer oyuncunun sağlığı sıfır ise
    if P.getHealth() == 0:
        #zamanlayıcıları durdur
        pausetimers()
        #sağlığı sıfırla  
        P.resethealth()
        #oyunu yumuşak bir şekilde sıfırla
        reset(False)
        #hayat kaybı mesajı göster
        messagebox.showinfo("Asterpocalypse", "Bir Hayat Kaybettin")
        #oyuncu konumunu sıfırla
        P.resetlocation()
        #zamanlayıcıları çalıştır
        pausetimers(False)
        
        
    
#create a function to check if an asteroid was destroyed, and if yes add the points it was worth to the total points     
def asterTimer(spacerock):

    global score
    #asteroidin yok edilip edilmediğini kontrol et
    if spacerock.isdestroyed() == True:
        #puan değerini al
        points = spacerock.getAsteroidpoints()
        #puanı skora ekle
        score += points
        #asteroidi sıfırla
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
    
    #arka plan resimlerinin listesini döngüye al
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
    
    #her bir asteroid üzerinde dön ve oyuncunun asteroide çarpıp çarpmadığını kontrol et
    for x in range(len(asteroids)):
        #eğer asteroid yok edilmişse, devam et
        if asteroids[x].isdestroyed() == True:
            pass
        else:
            #oyuncu ve asteroidin üst üste gelip gelmediğini kontrol et, eğer geldiyse oyuncudan 1 hayat eksilt
            if P.getX() + P.getWidth() - 10 >= asteroids[x].getxPos() and P.getX() <= asteroids[x].getxPos() + asteroids[x].getWidth() and asteroids[x].isdestroyed() == False:
                if P.getY() + P.getHeight() >= asteroids[x].getyPos() and P.getY() <= asteroids[x].getyPos() + asteroids[x].getHeight():
                    #oyuncunun sağlığını 1 yap
                    P.setHealth(1)
                    #1hp kaybetmesini sağla
                    P.takeDamage()
                    #ses efekti çal
                    playexplosioneffect()
                    #hayatlar kontrol et
                    playerlives()
                    break
                
    #lazer ateşlendi mi diye kontrol et
    if B.isFired() == True:
        #tüm asteroidleri kontrol et ve lazerin onlara çarpıp çarpmadığını kontrol et, çarparsa lazeri sıfırla ve asteroidi hasar alacak şekilde ayarla
        for x in range(len(asteroids)):
            if asteroids[x].getxPos() + asteroids[x].getWidth() - 10 >= B.getX() and asteroids[x].getxPos() <= B.getX() + B.getWidth() and asteroids[x].isdestroyed() == False:
                if asteroids[x].getyPos() + asteroids[x].getHeight() >= B.getY() and asteroids[x].getyPos() <= B.getY() + B.getHeight():
                    #lazeri sıfırla
                    B.reset()
                    #asteroid hasar alacak
                    asteroids[x].TakeDamage()
                    #eğer asteroid yok olduysa, puan ekle
                    asterTimer(asteroids[x])
                        
                
    collisionid = root.after(1, Collisionchk)

#create a function that will check if any asteroids hit the left wall
def AsterWallchk():    
    #eğer asteroid yoksa, kodu atla
    if len(asteroids) == 0:
        pass
    else:
        #tüm asteroidleri kontrol et, eğer soldaki duvara çarptıysa, oyuncu hasar alacak
        for x in range(len(asteroids)):
            if asteroids[x].getxPos() + asteroids[x].getWidth() <= 0 and  asteroids[x].isdestroyed() == False:
                #asteroidi yok et ve offset yap
                asteroids[x].destroy()
                asteroids[x].makeinvis()
                
                #oyuncuya hasar ver ve hayatlarını kontrol et
                P.takeDamage()
                playerlives()               
    
#spawndaki her bir asteroid için y-axis değerini kontrol et    
ySpawnPos = 0
#create a function to check whether an asteroid can spawn on a specific y-axis value
def checkspawn(A):
    global asteroids
    global ySpawnPos
    
    #asteroidlerin üst üste gelip gelmediğini kontrol et
    for x in range(len(asteroids)):
        #bu asteroid duvara çarpmıyorsa, diğerine geç
        if asteroids[x].getxPos() + asteroids[x].getWidth() <= canvas.winfo_reqwidth():
            pass
        else:
            #bu asteroidin hitbox'ını al
            ytop = asteroids[x].getyPos()
            ybot = asteroids[x].getHeight()
            xL = asteroids[x].getxPos()
            xR = asteroids[x].getWidth()
            #spawndaki y değeri
            ySpawnPos = A.genYSpawn(y1 = ytop, y2 = ybot,x1= xL,x2= xR)
            return ySpawnPos
    
    #spawndaki y değeri
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
    
    #zorlaştırmak için oyun zorluk seviyesini kontrol et ve asteroidlerin hızını artır
    if difficulty == 2 and asteroid_speed != 40:
        asteroid_speed -= 30
        difficulty = 0
    elif difficulty == 2 and asteroid_speed != 10:
        asteroid_speed -= 10
        difficulty = 0
       
    #10dan az asteroid varsa, yeni asteroid yarat
    if len(asteroids) < 10:
        #yeni bir asteroid nesnesi oluştur
        A = Asteroid(canvas, imgTitle)
        #asteroidin özelliklerini oluştur
        A.Generate()
        
        #ilk asteroid yaratıldığında, y-axis değerini rastgele oluştur
        if len(asteroids) == 0:
            A.genYSpawn()
        else:
            #asteroidin y-axis'ine spawn olup olamayacağını kontrol et
            checkspawn(A)
        #resmi görünür yap    
        A.SpawnAsteroid()
        #hız ayarla
        A.setSpeed(asteroid_speed)
        #asteroidi hareket ettir
        A.moveAsteroid()
        #nesneyi asteroids listesine ekle
        asteroids.append(A)

        #oyunu zorlaştır
        if asteroid_spawn_rate > 500:
            asteroid_spawn_rate -= 100
        
        #spawn oranını ayarla
        asterspawntmrid = root.after(asteroid_spawn_rate, create_Asteroid)
    else:
        #asteroidlerin yavaş hareket etmesini sağla
        asterspawntmrid = root.after(100, create_Asteroid)

#create window for game
root = Tk()
root.title("Asterpocalypse")
canvas = Canvas(root, width = 800, height = 600, bg = 'black')
canvas.pack()

#set game icon
root.iconbitmap("spaceship.ico")

#set background images for parallax effect
background_list = []
xpos = []

imgBackground = PhotoImage(file="background.png")
imgBackground2 = PhotoImage(file="background2.png")
background_list.append(canvas.create_image(0, 0, image = imgBackground, anchor = "nw"))
background_list.append(canvas.create_image(0, 0, image = imgBackground2, anchor = "nw"))
xpos.append(0)
xpos.append(imgBackground.width())

#call the background movement function
background_timer()

#initialize player class
P = Player(canvas)
P.spawn()
P.setLives(3)
P.setHealth(3)

#create a bullet
B = Bullet(canvas)
B.reset()

#create a list to store asteroids
asteroids = []

#initialize score
score = 0

#initialize score display
score_text = canvas.create_text(750, 25, text = score, font = ("Helvetica", 20), fill = "white")

#call scoretimer() every 50ms
scoretimer()

#create asteroid every 2000ms
create_Asteroid()

#create ship
P.spawn()

#main loop
root.mainloop()
