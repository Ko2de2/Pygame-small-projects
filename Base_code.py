import pygame

class Square:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.Width, self.Height = 1000, 800
        self.screen = pygame.display.set_mode((self.Width, self.Height))
    
    def run(self):
        Go = True
        while Go:
            # Key pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Go = False
            
            self.screen.fill((255, 255, 255))
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

Square().run()