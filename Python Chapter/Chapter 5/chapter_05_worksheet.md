# 1. Explain how the computer coordinate system differs from the standard Cartesian coordinate system. There are two main differences. List both.
- Die System funktionieren nach dem gleichen Prinzip
- Die Y Koordinate ist allerding umgedreht
- Beim Computer Koordinatensystem wird das rechte untere Quadrat betrachtet
- Das Cartesian System betrachtet überlicherweise das rechte obere Quadrat

# 2. Before a Python Pygame program can use any functions like pygame.display.set_mode(), what two lines of code must occur first?
- Pygame importieren = import pygame
- Game Engine initalisieren = pygame.init()

# 3. Explain how WHITE = (255, 255, 255) represents a color.
- RGB Mischverhältnis = (XXX,XXX,XXX)
- Helligkeit aller Farben auf den höchsten Wert gestellt, dass ergibt Weiß

# 4. When do we use variable names for colors in all upper-case, and when do we use variable names for colors in all lower-case? (This applies to all variables, not just colors.)
- upper-case = unveränderbar, eine konstante
- lower-case = im nachhinein noch veränderbar

# 5. What does the pygame.display.set_mode() function do?
- Es öffnet ein Fenster, welches vom Nutzer in der Größe definiert werden kann
- Es können auch Vollbildfenster geöffnet werden und somit alles andere auf dem Bildschirm enfernt werden z.B. Steuerungselemente von Windows

# 6. What does this for event in pygame.event.get() loop do?
- Wartet ab bis der User eine definierte Tätigkeit ausführt
- Es verwaltet alle möglichen Eingaben des User

# 7. What is pygame.time.Clock used for?
- Es bestimmt die Geschwindigkeit bzw. Bildwiederholrate, in der die grafische Darstellung geladen wird

# 8. For this line of code: pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
# 8.1 What does screen do?
- deklariert die Oberfläche in welcher gezeichnet werden soll
# 8.2 What does [0, 0] do?
- deklariert den Startpunkt
# 8.3 What does [100, 100] do?
- deklariert den Endpunkt
# 8.4 What does 5 do?
- Gibt die Breite an

# 9. What is the best way to repeat something over and over in a drawing?
- mit loops und offsets

# 10. When drawing a rectangle, what happens if the specified line width is zero?
- das Rechteck wird ausgefüllt

# 11. Describe the ellipse drawn in the code below.  pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
# 11.1 What is the x, y of the origin coordinate?
- 20,20
# 11.2 What does the origin coordinate specify? The center of the circle?
- obere linke Ecke, damit der Computer weiß wo anfangen muss zu zeichnen
# 11.3 What is the length and the width of the ellipse?
- 250x100

# 12. When drawing an arc, what additional information is needed over drawing an ellipse?
- start and end angels

# 13. Describe, in general, what are the three steps needed when printing text to the screen using graphics?
- Programm was die Variablen kreiert und die Informationen behinhaltet (font, typeface, size)
- Programm welches image vom text kreiert, stamp of the tex
- Koordinaten wo der Text plaziert werden soll

# 14. When drawing text, the first line of the three lines needed to draw text should actually be outside the main program loop. It should only run once at the start of the program. Why is this? You may need to ask.
- 

# 15. What are the coordinates of the polygon that the code below draws? pygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)
- [50,100],[0,200],[200,200],[100,50]

# 16. What does pygame.display.flip() do?
- sorgt dafür, dass alles was gezeichnet wurde auch auf dem screen erscheint

# 17. What does pygame.quit() do?
- beendet das Spiel

# 18.Look up on-line how the pygame.draw.circle works. Get it working and paste a working sample here. I only need the one line of code that draws the circle, but make sure it is working by trying it out in a full working program.
- pygame.draw.circle(screen,RED,(100,100),radius)