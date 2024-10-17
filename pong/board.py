import pygame

class Board:
    def __init__(self, x, y, width, height, color, velocity):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color  
        self.velocity = velocity

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, button_up, button_down, screen_height):
        keys = pygame.key.get_pressed()

        if keys[button_up] and self.rect.y > 10:  
            self.rect.y -= self.velocity
        if keys[button_down] and self.rect.y < screen_height - 10 - self.rect.height:
            self.rect.y += self.velocity
