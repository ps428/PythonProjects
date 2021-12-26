import pygame
import time
import shutil

shutil.copyfile('original.txt','copy.txt')

pygame.init()


color = (255,0,0)
green = (0, 255, 0)
white = (255,255,255)
black = (0,0,0)

window = pygame.display.set_mode((800,150))
pygame.display.set_caption("Copying a file")

font=pygame.font.SysFont('timesnewroman', 32)


for i in range(10):
    window.fill(black)
    pygame.display.update()
    
    pygame.draw.rect(window, color, pygame.Rect(30, 30, 74*(i+1), 20) )
    text_data = 'Copying in progress: '+str((i+1)*10)+'% done.'
    text = font.render(text_data, True, white)

    window.blit(text, (30,80))
    
    pygame.display.update()
    time.sleep(0.5)
window.fill(black)
pygame.display.update()
   
pygame.draw.rect(window, green, pygame.Rect(30, 30, 80*i, 20) )

text_data = 'Copying Completed!'
text = font.render(text_data, True, white)

window.blit(text, (270,80))

pygame.display.update()
time.sleep(2)
