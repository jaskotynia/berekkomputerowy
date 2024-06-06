# Punkty

1. [x] wyswietlic koodynaty gracza
2. [x] gracz1.punkty
3. [x] gracz2.punkty
4. [x] runda_gracz   # ktory gracz teraz goni



1. [ ] Jesli gracz goni i dogoni dswtedy dostaje punkt 
2. [ ] po otrzymaniu punktu reset pozycji gracza resetuje sie pozycja graczy
3. [ ] odgrywamy dzwiek kiedy ktos dostaje punkt
4. [ ] ? Jesli gracz poza ekranem wtedy przegrywa runde?


```python 
teskst = "Aaaaa"
liczba  =1111111
abs(-10) =10 #zawsze wartosc dodatnia  
abs(10) =10
int(12.1234) #Do liczby calkowitej
str(12.1234) # Do tekstu
'{:04}'.format(100) #Formatowanie do 4  zer  przed 
```

Inicjalizacja tekstu

```python
pygame.font.init() 
self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
```

Pisanie na ekranie
```python
textsurface = self.font.render("TEKST", False, (255, 255, 255))
self.screen.blit(textsurface,(0,0))  ## koordynaty gdzie
```

Przykłady
```python
         textsurface = self.font.render(
                    ' P1'+
                    ' x: {:04}'.format(int(self.gracz1.pos.x))  + 
                    ' y: {:04}'.format(int(self.gracz1.pos.y))  +
                    ' P2' +
                    ' x: {:04}'.format(int(self.gracz2.pos.x))  + 
                    ' y: {:04}'.format(int(self.gracz2.pos.y))  +
                    self.msg
                , False, (255, 255, 255))
                self.screen.blit(textsurface,(0,0))
```



Granie muzyki

```
        pygame.mixer.init()
        pygame.mixer.music.load('C:\\git\\jas\\berekkomputerowy\\boom.mp3') 
        pygame.mixer.music.play()
```

