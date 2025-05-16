#// ALİ MUHSİN MIŞRAKLI 
#//OKAN KARAHAN
#//Pamukkale Program
#//01/04/2025
    
# Gerekli tüm sınıfları içeri aktar
from tkinter import Tk, Canvas, PhotoImage, messagebox
from Bullet import Bullet
from Player import Player
from Asteroid import Asteroid
import pygame

# Miksere başlat
pygame.mixer.init()

# Arka plan şarkısını yükle ve tekrar çal
pygame.mixer.music.load("15 MilkyWay (Battle).mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(loops=-1)

# Bir ses efekti çalmak için bir fonksiyon oluştur
def playlasereffect():
    #ses efektini başlat
    laser = pygame.mixer.Sound("064-laser.wav")
    #oynat efekti
    pygame.mixer.Sound.play(laser)
 
# Bir ses efekti çalmak için bir fonksiyon oluştur
def playexplosioneffect():
    #ses efektini başlat
    explode = pygame.mixer.Sound("explosion.wav")
    #oynat efekti
    pygame.mixer.Sound.play(explode)

# Zamanlayıcıyı duraklatmak ve tekrar başlatmak için bir fonksiyon oluştur
def pausetimers(flag = True):
    global frametmrid
    global bullettmrid
    global collisionid
    global asterspawntmrid
    
    # Duraklatmak mı yoksa devam ettirmek mi istediğini kontrol et (duraklatmak için True, devam ettirmek için False)
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
       # Bu zamanlayıcıları devam ettir (un-pause)
        frame()
        bulletTimer()
        Collisionchk()
        create_Asteroid()

# Skoru her 50ms'de bir güncelleyen fonksiyon
def scoretimer():
    global score
    global scoretmrid
    canvas.itemconfig(score_text, text = score)
    scoretmrid = root.after(50, scoretimer)
    
# 125 ms'de bir gemi animasyonu çerçevesini (frame) güncelleyen bir zamanlayıcı fonksiyonu 
def frame():
    global frametmrid
  
    P.animate(B.isFired())
    frametmrid = root.after(125, frame)

# Oyunu kapatmak için bir program oluştur
def exit_program():
   
    root.after_cancel(btid)
    root.after_cancel(scoretmrid)
    
    pausetimers()
    
    exit()

# Oyunu sıfırlamak için bir program oluştur

def reset(flag = True):
    global score
    global asteroid_spawn_rate
    global asteroid_speed
    # Asteroitleri en sağ duvara sıfırla ve onları kaydır

    widthsetback = 0
    for x in range(len(asteroids)):
        asteroids[x].destroy()
        widthsetback += asteroids[x].getWidth()
        asteroids[x].makeinvis(widthsetback)
        
    #reset the laser
    B.reset()
    
    # Oyunu tamamen sıfırla, hızı temel hıza ayarla ve skoru sıfırla

    if flag == True:
        asteroid_speed = 100
        asteroid_spawn_rate =2000
        score = 0
        canvas.itemconfig(score_text, text = score)

# Bir oyuncunun bir can kaybedip kaybetmediğini veya oyunun bitip bitmediğini kontrol eden bir fonksiyon oluştur
     
def playerlives():

    global score
    
    # Toplam canları kontrol et, eğer 0 ise tekrar oynamak isteyip istemediklerini sor

    if P.getLives() == 0:
       # Zamanlayıcıları duraklat, oyuncu sağlığını/canlarını sıfırla, oyunu yumuşak bir şekilde sıfırla
        pausetimers()
        P.reset()
        reset(False)
        flag = messagebox.askyesno("Pamukkale", "Sen " + str(score) + " puan yaptın\n Bir daha oynamak ister misin ?")
       # Oyunu tamamen sıfırla
        reset()
       # Oyuncu konumunu sıfırla
        P.resetlocation()
      
        if flag == False:
            exit_program()
       
        pausetimers(False)
            
            
    if P.getHealth() == 0:
        pausetimers()
        P.resethealth()
        reset(False)
        messagebox.showinfo("Pamukkale", "Canın gitti")
        P.resetlocation()
        
        pausetimers(False)    
    
# Bir asteroit yok olduysa kontrol eden bir fonksiyon oluştur ve eğer evet ise, değeri kadar puanı toplam puana ekle   
def asterTimer(spacerock):

    global score
    # Asteroit yok oldu mu diye kontrol et
    if spacerock.isdestroyed() == True:
       # Puan değerini al
        points = spacerock.getAsteroidpoints()
        # Puanı skora ekle
        score += points
      # Asteroiti sıfırla
        spacerock.makeinvis()
        
# Her 50ms'de bir lazerin ekranın sağ tarafına çıkıp çıkmadığını kontrol eden bir zamanlayıcı oluştur
           
def bulletTimer():
    global bullettmrid
    if B.getX() > canvas.winfo_width():
        B.reset()

    bullettmrid = root.after(50, bulletTimer)

# Arka planı animasyon yapmak için bir zamanlayıcı oluştur ve her 50ms'de bir çağır

def background_timer():
    global btid
    
   # Çerçeve listesini döngüye al
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5
    
    btid = root.after(50, lambda: background_timer())
    root.update()
    
    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

# Her 1ms'de bir çarpışmayı kontrol etmek için bir zamanlayıcı oluştur
def Collisionchk():
    global collisionid
    
    
    for x in range(len(asteroids)):
        
        if asteroids[x].isdestroyed() == True:
            pass
        else:
           
            if P.getX() + P.getWidth() - 10 >= asteroids[x].getxPos() and P.getX() <= asteroids[x].getxPos() + asteroids[x].getWidth() and asteroids[x].isdestroyed() == False:
                if P.getY() + P.getHeight() >= asteroids[x].getyPos() and P.getY() <= asteroids[x].getyPos() + asteroids[x].getHeight():
                   
                    P.setHealth(1)
                   
                    P.takeDamage()
                   
                    playexplosioneffect()
                   
                    playerlives()
                    break
                
   
    if B.isFired() == True:
       
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

# Herhangi bir asteroit sol duvara çarptı mı diye kontrol eden bir fonksiyon oluştur

def AsterWallchk():    
   
    if len(asteroids) == 0:
        pass
    else:
        # Tüm asteroitleri kontrol et ve sol duvarı geçip geçmediklerini kontrol et, eğer geçtilerse oyuncu hasar alır

        for x in range(len(asteroids)):
            if asteroids[x].getxPos() + asteroids[x].getWidth() <= 0 and  asteroids[x].isdestroyed() == False:
                
                asteroids[x].destroy()
                asteroids[x].makeinvis()
                
               
                P.takeDamage()
                playerlives()               
                break
    
            
                    
ySpawnPos = 0
# Bir asteroitin belirli bir y ekseni değeriyle doğup doğamayacağını kontrol eden bir fonksiyon oluştur
def checkspawn(A):
    global asteroids
    global ySpawnPos
    
  # Asteroitleri kontrol et ve en yeni asteroitin, diğerleriyle örtüşüp örtüşmediğini kontrol et
    for x in range(len(asteroids)):
       # Eğer bu asteroit sağ duvarla örtüşmüyorsa, bir sonrakine geç
        if asteroids[x].getxPos() + asteroids[x].getWidth() <= canvas.winfo_reqwidth():
            pass
        else:
           
            ytop = asteroids[x].getyPos()
            ybot = asteroids[x].getHeight()
            xL = asteroids[x].getxPos()
            xR = asteroids[x].getWidth()
            #get a y value that is spawnable
            ySpawnPos = A.genYSpawn(y1 = ytop, y2 = ybot,x1= xL,x2= xR)
            return ySpawnPos
    
   
    ySpawnPos = A.genYSpawn()
                
    return ySpawnPos
        
   
asteroid_spawn_rate = 2000
asteroid_speed = 100
difficulty = 0


def create_Asteroid():
    global asterspawntmrid
    global asteroid_spawn_rate
    global asteroid_speed

    global difficulty
    canspawn = False
    
    
    
   
    if difficulty == 2 and asteroid_speed != 40:
        asteroid_speed -= 30
        difficulty = 0
    elif difficulty == 2 and asteroid_speed != 10:
        asteroid_speed -= 10
        difficulty = 0
       
    
    if len(asteroids) < 10:
       
        A = Asteroid(canvas, imgTitle)
       
        A.Generate()
        
      
        if len(asteroids) == 0:
            A.genYSpawn()
        else:
            
            checkspawn(A)
          
        A.SpawnAsteroid()
       
        A.setSpeed(asteroid_speed)
        
        A.moveAsteroid()
        
        asteroids.append(A)
   
    elif len(asteroids) == 10:
       # Eğer 10 asteroit nesnesi zaten oluşturulmuşsa
# Hepsini kontrol et ve bir sonraki dalganın 10 asteroiti doğup doğamayacağını kontrol et
        for y in range(len(asteroids)):
           # Eğer tüm asteroitler yok edildiyse, bir sonraki dalgayı doğur; aksi takdirde bir sonraki dalgayı doğurma
            if asteroids[y].isdestroyed() == True:
                canspawn = True
            else:
                canspawn = False
                break
        
          
        if canspawn == True:
            canvas.itemconfig(text, text = "New Wave Approaching!")
           
            difficulty +=1
        
       
        if canspawn == True:  
            
            
            setback = canvas.winfo_reqwidth()
            for x in range(len(asteroids)):
                
                asteroids[x].undestroy()
               
                asteroids[x].Generate()
               
                checkspawn(asteroids[x])
               
                setback += asteroids[x].getWidth()
               
                asteroids[x].setxPos(setback + 100)
                
                asteroids[x].SpawnAsteroid()
                
                asteroids[x].setSpeed(asteroid_speed)
                
                asteroids[x].moveAsteroid()
                
             
        if asteroids[0].getxPos() <= canvas.winfo_reqwidth():
            canvas.itemconfig(text, text = "")
                
                
           
                
    AsterWallchk()
    asterspawntmrid = root.after(asteroid_spawn_rate, create_Asteroid)
    
             
def onkeypress(event):
    global bullx
    global bully
   
    if event.keysym == 'space' and B.isFired() == False:
       
        B.setLocation(bullx + P.getWidth() - 10 , bully + P.getHeight() // 2 - 10)
        
       
        playlasereffect()
        
        B.fireBullet()
       
        bulletTimer()
        
        
bullx = 0
bully = 0

def onmousemove(event):
    global bullx
    global bully
    x = event.x - P.getWidth() // 2
    y = event.y - P.getHeight() // 2
    
   # Ekran sınırlarını belirle ve eğer fare sınırları geçerse oyuncu gemisinin nerede olması gerektiğini ayarla
    if x <= 0:
        x = 0
    elif x + P.getWidth() >= canvas.winfo_width():
        x = canvas.winfo_reqwidth() - P.getWidth() - 5
    
    if y <= imgTitle.height():
        y = imgTitle.height()
        
    elif y + P.getHeight() >= canvas.winfo_height():
        y = canvas.winfo_height() - P.getHeight() - 5
    
   # Oyuncu gemisinin konumunu, fareye göre ayarla
    P.setLocation(x,y)
    
    bullx = x + 10
    bully = y
root = Tk()
root.title('Pamukkale')
root.protocol('WM_DELETE_WINDOW', exit_program)

root.bind('<KeyPress>', onkeypress)
root.bind('<Motion>', onmousemove)


imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')


root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))

canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()

background_list = [0] * 2
xpos = [0, imgBackground.width()]


for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')

#set the score, and display it
score = 0
score_text = canvas.create_text(canvas.winfo_reqwidth() //8 , 35, text = score, fill = "orange", font = "neuropol-Regular 30")
text = canvas.create_text(canvas.winfo_reqwidth() //2 , canvas.winfo_reqheight() // 2, text = "", fill = "orange", font = "neuropol-Regular 30")


asteroids = []
# Oyuncu ve lazer (mercek) nesnelerini başlat
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
