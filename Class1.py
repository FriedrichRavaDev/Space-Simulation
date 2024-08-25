import pygame

running = True

def MousePos():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                pos = (x, y)

                q = pos
                return q  # return 'hello world' would do, too

x = MousePos()

def Return():
    if x[0] >= 950 or x[1] >= 600:
       return 1
    if x[0] < 950 or x[1] < 600:
        return -1

r = Return()