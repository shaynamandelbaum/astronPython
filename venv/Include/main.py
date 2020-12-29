import pygame
map = pygame.image.load('C:\\Users\\shayn\\PycharmProjects\\astron\\venv\\Include\\astronMap.png')
(width,height) = (600,600)
screen = pygame.display.set_mode((width,height))
#2481,554
map = pygame.transform.smoothscale(map,(1860,413))

screen.blit(map,(100,100),(300,50,600,300))
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()