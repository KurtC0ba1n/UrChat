import pygame
import sys
from pygame.locals import *

def parseMessage(message, limit):
    if len(message)>limit:
        lines = []
        splittedMessage = message.split()
        i=0
        while i<len(splittedMessage):
            splittedMessage[i]+=" "
            i+=1
        while len(splittedMessage)>0:
            tmpLine = ""
            i=0
            while len(tmpLine)<limit and i<len(splittedMessage):
                tmpLine+=splittedMessage[i]
                i+=1
            lines.append(tmpLine)
            splittedMessage = splittedMessage[i:]
        return lines
    else: return [message]


class chatFrame(object):
    def __init__(self, position):
        self.surf = pygame.Surface((280, 310))
        self.surf.fill((100,100,100))
        self.position = position
        self.font = pygame.font.SysFont('Time New Roman', 25)
        self.messages = []

    def update(self):
        self.surf.fill((100,100,100))
        if len(self.messages)>22:
            self.messages = self.messages[1:]
        for message, line in zip(self.messages, range(0, 308, 14)):
            renderedMess = self.font.render(message, True, (0,0,0))
            renderedMessRect = renderedMess.get_rect()
            renderedMessRect.left = self.surf.get_rect().left
            renderedMessRect.y = line
            self.surf.blit(renderedMess, renderedMessRect)

    def get_message(self, message):
        parsedMessage = parseMessage(message, 30)
        for m in parsedMessage:
            self.messages.append(m)

    def get_frame(self):
        return self.surf

class inputBox():

    def __init__(self, surface, position, size, text=""):
        #ignit the widget
        if len(text) != 0:
            self.text = text + ": "
        else:
            self.text = ""
        self.position = position
        self.isFocused = False
        self.message = self.text
        self.charsLen = []
        self.surf = pygame.Surface((280, 25))
        self.surf.fill((255, 255, 255))
        self.colorBox = (255,255,255)
        self.colorInput = (0,0,0)
        self.Font = pygame.font.Font(None,round(size))
        self.inputFont = self.Font.render(self.message, True, (0,0,0))
        self.inputFontRect = self.inputFont.get_rect()
        self.inputFontRect.left = self.surf.get_rect().left


    def update(self, key):
        self.surf.fill((255,255,255))
        if key == pygame.K_BACKSPACE and len(self.message) > len(self.text):
            self.message = self.message[0:-1]
            self.charsLen = self.charsLen[:-2]
        elif key == pygame.K_RETURN:
            pass
        elif key <= 127 and len(self.message) < 100:
            self.message = self.message + chr(key)
        i=0
        while i < len(self.message):
            self.inputLetter = self.Font.render(self.message[i], True, (0,0,0))
            self.inputLetterRect = self.inputLetter.get_rect()
            offset = sum(self.charsLen) - self.surf.get_width()
            if i > 0:
                self.inputLetterRect.left = self.previousRectLetter
            else:
                if offset>0:
                    self.inputLetterRect.left = self.surf.get_rect().left-offset
                else:
                    self.inputLetterRect.left = self.surf.get_rect().left
            self.previousRectLetter = self.inputLetterRect.right
            self.surf.blit(self.inputLetter, self.inputLetterRect)
            i+=1
        self.charsLen.append(self.inputLetterRect.width)


    def clear(self):
        self.surf.fill((255,255,255))
        self.charsLen = []
        self.message = ""


    def get_text(self):
        return self.message[len(self.text):]

    def get_frame(self):
        return self.surf

class Button(object):

    def __init__(self, size, position, pathImage):
        self.image = pygame.image.load(pathImage)
        self.image = pygame.transform.scale(self.image, size)
        self.position = position
        self.imageRectPos = pygame.Rect(position, (position[0]+size[0], position[1]+size[1]))

    def get_frame(self):
       return self.image


    def isCliked(self):
        if self.imageRectPos.collidepoint(pygame.mouse.get_pos()):
            return True
        else: return False
