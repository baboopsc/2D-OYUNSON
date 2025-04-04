# Asterpocalypse - Asteroid Sınıfı Raporu

## Genel Bakış

**Asteroid Sınıfı**, oyunun temel öğelerinden biri olan asteroitlerin davranışlarını yönetir. Bu sınıf, asteroitlerin rastgele doğmasını, hareket etmelerini, hasar almalarını ve yok olmalarını sağlar. Ayrıca her asteroitin puan, sağlık ve hız gibi özelliklerini belirler ve bu değerleri yönetir. Asteroitler, ekrandaki görselleri ile hareket eder, patlama animasyonları ve hasar alma gibi özelliklere sahiptir.

---

## Temel Özellikler

- **Puan (Points):**
    - Her asteroitin farklı puan değerleri vardır: 10, 20, 30.
  
- **Sağlık (Hitpoints):**
    - Asteroitlerin 3 farklı sağlık değeri bulunur: 1, 2, 3.

- **Görseller (Images):**
    - Asteroitlerin görselleri `images/asteroid0.png`, `images/asteroid1.png`, `images/asteroid2.png`, `images/explosion0.png` ve `images/blank.png` gibi dosyalarla temsil edilir.

- **Hız (Speed):**
    - Asteroitlerin hareket hızı zaman içinde değiştirilebilir. Varsayılan hız 20'dir.

- **Hasar Alma ve Yok Olma:**
    - Asteroitler hasar aldıkça sağlıkları azalır ve sağlık sıfırlandığında patlar (yok olur).

- **Doğma (Spawn) ve Hareket (Movement):**
    - Asteroitler rastgele yerlerde doğar ve ekranın sağ tarafından sola doğru hareket ederler.

---

## Sınıfın Metodları

### 1. `SpawnAsteroid(self)`
   Asteroit görüntüsünü ekranda görünür hale getirir.

### 2. `getSpeed(self)`
   Asteroitin mevcut hızını döndürür.

### 3. `setSpeed(self, speed)`
   Asteroitin hızını belirler.

### 4. `moveAsteroid(self)`
   Asteroitin ekranda sola doğru hareket etmesini sağlar.

### 5. `genYSpawn(self, y1=0, y2=0, x1=0, x2=0)`
   Asteroitin doğma konumunu rastgele belirler ve geçerli bir y konumu üretir.

### 6. `Generate(self)`
   Asteroitin rastgele bir boyut seçmesini sağlar ve bununla birlikte istatistiklerini (sağlık, puan) oluşturur.

### 7. `getyPos(self)` ve `setyPos(self, y)`
   Asteroitin y koordinatını alır ve ayarlar.

### 8. `getxPos(self)` ve `setxPos(self, x)`
   Asteroitin x koordinatını alır ve ayarlar.

### 9. `setAsteroidimg(self, size)`
   Asteroitin resmini belirler.

### 10. `getAstroidimg(self)`
   Asteroitin resmini döndürür.

### 11. `setAsteroidhp(self, size)`
   Asteroitin sağlık değerini ayarlar.

### 12. `getAsteroidhp(self)`
   Asteroitin sağlık değerini döndürür.

### 13. `setAsteroidpoints(self, size)`
   Asteroitin puanını ayarlar.

### 14. `getAsteroidpoints(self)`
   Asteroitin puanını döndürür.

### 15. `getWidth(self)` ve `getHeight(self)`
   Asteroitin genişlik ve yüksekliğini döndürür.

### 16. `destroy(self)`
   Asteroiti yok eder.

### 17. `isdestroyed(self)`
   Asteroitin yok olup olmadığını kontrol eder.

### 18. `undestroy(self)`
   Asteroiti tekrar aktif hale getirir.

### 19. `makeinvis(self, setback=0)`
   Asteroiti ekrandan dışarı çıkarır.

### 20. `TakeDamage(self)`
   Asteroite hasar verir ve yok olup olmadığını kontrol eder.

---

## Görseller

Aşağıdaki görseller `images` klasöründen alınmıştır:

- ![Asteroid 0](images/asteroid0.png)
- ![Asteroid 1](images/asteroid1.png)
- ![Asteroid 2](images/asteroid2.png)
- ![Explosion](images/explosion0.png)
- ![Blank](images/blank.png)

---

## Örnek Kod

Aşağıda, **Asteroid** sınıfının nasıl kullanılabileceğine dair bir örnek verilmiştir:

```python
from tkinter import Tk, Canvas
from asteroid import Asteroid

# Ana pencereyi oluştur
root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# Asteroit objesi oluştur
asteroid = Asteroid(canvas, 100)
asteroid.Generate()
asteroid.SpawnAsteroid()
asteroid.moveAsteroid()

root.mainloop()
# Asterpocalypse - Bullet Sınıfı Raporu

## Genel Bakış

**Bullet Sınıfı**, oyundaki mermileri temsil eder. Bu sınıf, merminin hareketini, ateşlenmesini ve ekran üzerinde nasıl görüntüleneceğini kontrol eder. Mermi, bir oyuncu tarafından ateşlendiğinde ekranda hareket eder ve hedefe doğru ilerler.

---

## Temel Özellikler

- **X ve Y Değerleri:**
    - Merminin ekran üzerindeki konumunu belirler. `__x` ve `__y` olarak saklanır.

    ![Bullet Position](images/bullet_position_example.png)

- **Görseller:**
    - Merminin görseli **laserbeam_red.png** olarak belirlenmiştir. Bu görsel, mermiyi temsil eder.
    
    ![Bullet Image](images/laserbeam_red.png)

- **Boş Görsel:**
    - Merminin boş durumda gösterilmesi için kullanılan görsel **blank.png** olarak belirlenmiştir.
    
    ![Blank Image](images/blank.png)

- **Genel Durum:**
    - **__fired:** Merminin ateşlenip ateşlenmediğini kontrol eder.
    - **__canvas:** Merminin yer alacağı tkinter canvas penceresi.

- **Boyutlar:**
    - Merminin genişliği (`__width`) ve yüksekliği (`__height`), görselin boyutlarından alınır.
    
    ![Bullet Size](images/bullet_size_example.png)

---

## Sınıfın Metodları

### 1. `getX(self)`
   - Merminin mevcut x koordinatını döndürür.

### 2. `getY(self)`
   - Merminin mevcut y koordinatını döndürür.

### 3. `setX(self, x)`
   - Merminin x koordinatını ayarlar.

### 4. `setY(self, y)`
   - Merminin y koordinatını ayarlar.

### 5. `setLocation(self, x, y)`
   - Merminin ekran üzerindeki konumunu belirler ve `__canvas.coords()` fonksiyonu ile görseli günceller.

    ![Bullet Location](images/bullet_location_example.png)

### 6. `fireBullet(self)`
   - Mermiyi ateşler ve ileriye hareket ettirir. Bu metod, mermiyi sürekli olarak sağa hareket ettirir.

    ![Bullet Firing](images/bullet_firing_example.png)

### 7. `isFired(self)`
   - Merminin ateşlenip ateşlenmediğini kontrol eder ve Boolean (True/False) değerini döndürür.

### 8. `reset(self)`
   - Merminin hareketini durdurur, zamanlayıcıyı iptal eder ve mermiyi boş bir görsel ile değiştirir.

   ![Bullet Reset](images/bullet_reset_example.png)

### 9. `getWidth(self)`
   - Merminin genişliğini döndürür.

### 10. `getHeight(self)`
   - Merminin yüksekliğini döndürür.

---

## Örnek Kod

Aşağıda **Bullet** sınıfının nasıl kullanılabileceğine dair bir örnek verilmiştir:

```python
from tkinter import Tk, Canvas
from bullet import Bullet

# Ana pencereyi oluştur
root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# Bullet objesi oluştur
bullet = Bullet(canvas)

# Bullet ateşle
bullet.fireBullet()

root.mainloop()
