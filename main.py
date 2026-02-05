import pygame

print('Setup Start')
pygame.init()
windows = pygame.display.set_mode(size=(640, 480))
print('Setup end')

print('Lopp Start')
while True:

    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Windows
            quit()  # end pygame
