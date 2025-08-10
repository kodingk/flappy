import pygame

from click_event_observer import ClickEventObserver
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class RestartButton(pygame.sprite.Sprite, ClickEventObserver):
    image = pygame.image.load('img/restart.png')
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ClickEventObserver.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def check_clicked(self):
        return super().check_clicked() and self.rect.collidepoint(pygame.mouse.get_pos())

class RestartButtonGroup(pygame.sprite.Group, ClickEventObserver):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        ClickEventObserver.__init__(self)
        self.add(RestartButton())

    def check_clicked(self):
        return super().check_clicked() and self.sprites()[0].check_clicked()


def get_restart_group():
    return RestartButtonGroup()
