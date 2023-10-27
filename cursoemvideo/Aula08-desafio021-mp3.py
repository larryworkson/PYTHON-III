#crie um programa que toque um mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Tito.mp3')
pygame.mixer.music.play()
input()
