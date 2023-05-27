import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 640

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('O JOGO')

while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
   
            
