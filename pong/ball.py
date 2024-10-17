import pygame

class Ball:
    def __init__(self, x, y, width, height, color, velocity_x, velocity_y) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.top <= 0 or self.rect.bottom >= 720:  
            self.velocity_y = -self.velocity_y  

        