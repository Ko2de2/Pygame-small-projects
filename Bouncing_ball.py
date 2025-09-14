import pygame

class Square:
    def __init__(self):
        pygame.init()
        # Variables
        self.x, self.y = 500, 400
        self.dx, self.dy = 7, 10
        self.r = 25

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
            
            self.y += self.dy
            self.x += self.dx

            # Bounce check
            if self.y + self.r >= 800 or 800 - self.r <= self.y:
                self.dy = -self.dy
            if self.x + self.r >= 1000 or 1000 - self.r <= self.x:
                self.dx = -self.dx
            if self.y + self.r >= 0 or 0 + self.r <= self.y:
                self.dy = self.dy
            if self.x + self.r >= 0 or 0 + self.r <= self.x:
                self.dx = self.dx
            
            # Draw
            self.screen.fill((255, 255, 255))
            pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.r)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

Square().run()