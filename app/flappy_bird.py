'''Flappy Bid main folder'''
import os
import pygame
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    '''Classe responsavel pelo passaro no jogo'''

    IMGS = IMAGENS_PASSARO

    #animação da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]
    
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -=2

        self.y += deslocamento
        
        # angulo do passaro

class Cano:
    '''Classe responsavel pelo cano no jogo'''
    pass

class Chao:
    '''Classe responsavel pelo chao no jogo'''
    pass
