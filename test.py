import pygame
width=1000
height=950
WHITE=(250,250,250)
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pachinko")
pygame.init()
pygame.font.init()
font=pygame.font.SysFont('comicsans',50)
text=font.render("cool",False,WHITE)
win.blit(text,(100,200))
pygame.display.update()
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()