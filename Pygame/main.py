import pygame

pygame.init()

white = (255,255,255)

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

while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
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
    surface.fill(white)
    surface.blit(python, (move_x,move_y))
    win.update()
    clock.tick(30)
pygame.quit()