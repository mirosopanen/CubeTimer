
import pygame
from pygame import *
import time
import sys

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()

width, height = (640, 480)

screen = pygame.display.set_mode((width, height))
text = "Jarkko is bi"
textLen = 0
typewriterEvent = pygame.USEREVENT+1
pygame.time.set_timer(typewriterEvent, 100)
textSurf = None

pygame.font.init()
timerFont = pygame.font.SysFont("Arial", 50)


clock = pygame.time.Clock()


initTime = 0
countDownOn = False
# Main loop

while True:
    screen.fill((245, 245, 220))
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == typewriterEvent:
            textLen += 1
            if textLen > len(text):
                textLen = 0
            textSurf = None if textLen == 0 else timerFont.render(
                text[:textLen], True, (0, 0, 0))

        if textSurf:
            screen.blit(textSurf, textSurf.get_rect(
                midleft=screen.get_rect().midleft).move(40, 0))

    pygame.display.set_caption("Rubics Cube Timer")
    pygame.display.flip()
    fpsClock.tick(fps)
