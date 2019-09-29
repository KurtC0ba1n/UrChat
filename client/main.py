import pygame as pg
from widgets import *
from net import Networker

pg.init()
screen=pg.display.set_mode((300,400))
done = False

chatBox = chatFrame((10, 10))
input = inputBox(screen, (10, 330), (30))
connection = Networker('localhost', 25565)
connectButton = Button((30,30), (260, 360), './pictures/connection_icon.png')


while not done:
    chatBox.update()
    screen.blit(chatBox.get_frame(), chatBox.position)
    screen.blit(input.get_frame(), input.position)
    screen.blit(connectButton.get_frame(), connectButton.position)
    text = connection.get_message()
    if text != '':
        chatBox.get_message(text)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                connection.net_send(bytes(input.message, 'utf-8'))
                input.clear()
            else:
                input.update(event.key)
        if event.type == pg.MOUSEBUTTONDOWN:
            if connectButton.isCliked():
                connection.net_connect()
        if event.type == pg.QUIT:
            connection.net_end()
            done=True
    pg.display.flip()

pg.quit()
