import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from scrollable import Scrollable
from constants import GROUND_HEIGHT


BACKGROUND_IMAGE_PATH = "img/bg.png"
GROUND_IMAGE_PATH = "img/ground.png"


def get_bg_group():
    bg_group = pygame.sprite.Group()
    bg_group.add(Background())
    return bg_group

def get_ground_group():
    ground_group = pygame.sprite.Group()
    ground_group.add(Ground(0))
    return ground_group

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BACKGROUND_IMAGE_PATH)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self):
        pass


class Ground(Scrollable):
    def __init__(self, x):
        super().__init__(x, SCREEN_HEIGHT - GROUND_HEIGHT, GROUND_IMAGE_PATH)

    def update(self):
        super().update()  # 스크롤
        if self.rect.center[0] <= SCREEN_WIDTH // 2:
            self.rect.x = 0
