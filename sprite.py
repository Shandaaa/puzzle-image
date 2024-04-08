from typing import Any
import pygame
from settings import *
from algorithm import *
import time
import copy

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game,x,y,gameType,index,tilesize,gameSize):
        self.groups=game.all_sprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image = pygame.Surface((tilesize,tilesize))
        self.tilesize=tilesize
        self.image.fill(backgroud_col[gameType[0]])
        self.x,self.y=x,y
        self.index=index
        self.gameType=gameType
        self.clock=pygame.time.Clock()
        self.rect=self.image.get_rect()
        if self.index :
            self.font=pygame.font.SysFont("Consoles",50)
            surface=pygame.image.load(get_image(self.gameType,self.index))
            self.image.fill(white)
            self.image.blit(surface,(0,0))
        
        


    def update(self):
        self.rect.x=self.x*self.tilesize
        self.rect.y=self.y*self.tilesize
        
        


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, hover_color, text, text_color,font_size, font='Georgia'):
        my_group = pygame.sprite.Group()
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size=font_size

    def draw_ellipse(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
        font=pygame.font.SysFont(self.font,self.font_size,bold=True)
        font_surface = font.render(self.text, True, self.text_color)
        font_rect = font_surface.get_rect(center=self.rect.center)
        screen.blit(font_surface, font_rect)

    def draw_rect(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font=pygame.font.SysFont(self.font,self.font_size,bold=True)
        font_surface = font.render(self.text, True, self.text_color)
        font_rect = font_surface.get_rect(center=self.rect.center)
        screen.blit(font_surface, font_rect)
    


    def click(self,mouse_x,mouse_y):
        return self.rect.left<=mouse_x<=self.rect.right and self.rect.top<=mouse_y<=self.rect.bottom
       