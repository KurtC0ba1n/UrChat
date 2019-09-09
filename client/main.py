import pygame as pg
from widgets import *

pg.init()
screen=pg.display.set_mode((300,400))
done = False

chatBox = chatFrame((10, 10))
input = inputBox(screen, (10, 330), (30))


while not done:
    chatBox.update()
    screen.blit(chatBox.get_frame(), chatBox.position)
    screen.blit(input.get_frame(), input.position)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                chatBox.get_message(input.message)
                input.clear()

            else:
                input.update(event.key)
        if event.type == pg.QUIT:
            done=True
    pg.display.flip()

pg.quit()
