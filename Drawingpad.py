import pygame

class Square:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.Width, self.Height = 1000, 800
        self.screen = pygame.display.set_mode((self.Width, self.Height))
        self.drawing = False
        self.last_pos = None
    
    def run(self):
        Go = True
        self.screen.fill((255, 255, 255))

        while Go:
            # Key pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Go = False
            # Drawing
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.drawing = True
                    self.last_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    self.drawing = False
                if event.type == pygame.MOUSEMOTION and self.drawing:
                    new_pos = pygame.mouse.get_pos()
                    pygame.draw.line(self.screen, (0, 0, 0), self.last_pos, new_pos, 2)
                    self.last_pos = new_pos
                # Erase all 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.screen.fill((255, 255, 255))
                            
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

Square().run()