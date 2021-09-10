import pygame, random

from pygame import color

pygame.init()

white = (255,255,255)
black = (0,0,0,0)
red = (255,0,0)
blue = (0,0,255)
green =(0,255,0)
x = 600
y = 800
z = [x,y]

win = pygame.display

move_x,move_y = 200,200 
change_x,change_y = 0,0
win.set_caption('My Window')

surface = win.set_mode(z)
python = pygame.image.load('IMG.jpg')
window = True 
clock = pygame.time.Clock()
click = 0
colors = [white,black,red,blue,green]
fill = white


while window:
    font = pygame.font.SysFont('timesnewroman', 20)
    text = font.render('Start', 0, black)
    for event in pygame.event.get():
        cursor_x, cursor_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            window = False
            """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x -= 5
            if event.key == pygame.K_RIGHT:
                change_x += 5
            if event.key == pygame.K_UP:
                change_y += -5
            if event.key == pygame.K_DOWN:
                change_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                change_y = 0

            if event.key == pygame.K_UP:
                change_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
        

    move_x += change_x 
    move_y += change_y
    """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((300-cursor_x)**2+(400-cursor_y)**2) < 2500:
                fill = random.choice(colors)






    surface.fill(fill)
    #surface.blit(python, (move_x,move_y))
    surface.blit(text,(x//2-19,y//2-12))
    pygame.draw.circle(surface, black, (x//2,y//2), 50,1)
    

    win.update()
    clock.tick(30)
pygame.quit()