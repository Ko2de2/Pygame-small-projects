import pygame

class Square:
    def __init__(self):
        pygame.init()
        pygame.time.get_ticks()
        
        Width, Height = 1000, 800
        self.screen = pygame.display.set_mode((Width, Height))
        self.Msquare = pygame.Rect(0, 0, 50, 50)
        self.Msquare.center = (Width // 2, Height // 2)
        self.movement_x = [False, False]
        self.movement_y = [False, False]

    
    def run(self):
        Go = True
        while Go:
            # Key pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Go = False
            # Moving
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement_x[0] = True
                    if event.key == pygame.K_d:
                        self.movement_x[1] = True
                    if event.key == pygame.K_w:
                        self.movement_y[0] = True
                    if event.key == pygame.K_s:
                        self.movement_y[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement_x[0] = False
                    if event.key == pygame.K_d:
                        self.movement_x[1] = False
                    if event.key == pygame.K_w:
                        self.movement_y[0] = False
                    if event.key == pygame.K_s:
                        self.movement_y[1] = False

            self.Msquare.x += self.movement_x[1] - self.movement_x[0]
            self.Msquare.y += self.movement_y[1] - self.movement_y[0]

            self.screen.fill((255, 255, 255))
            self.square = pygame.draw.rect(self.screen, (0, 0, 255), self.Msquare)
            pygame.display.update()
            
        pygame.quit()

Square().run()