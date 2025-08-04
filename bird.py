import pygame
from itertools import cycle
from constants import MAIN_SCREEN_BOTTOM, MAIN_SCREEN_TOP, SCREEN_HEIGHT
from click_event_observer import ClickEventObserver


INITIAL_BIRD_X, INITIAL_BIRD_Y = 100, SCREEN_HEIGHT // 2
BIRD_IMAGE_UPDATE_DELAY_FRAME = 5
JUMP_VELOCITY = -10
GRAVITY = 0.5


def get_bird_group():
    bird_group = pygame.sprite.Group()
    bird_group.add(Bird(INITIAL_BIRD_X, INITIAL_BIRD_Y))
    return bird_group


class Bird(pygame.sprite.Sprite, ClickEventObserver):
    images = cycle(map(pygame.image.load, ["img/bird1.png", "img/bird2.png", "img/bird3.png"]))

    def __init__(self, x, y):
        # 상위 클래스 __init__ 호출
        pygame.sprite.Sprite.__init__(self)
        ClickEventObserver.__init__(self)

        self.image = next(Bird.images)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.delay_counter = 0
        self.velocity = 0

    def update(self):
        self.update_img()
        self.update_velocity()
        self.update_bound()

        self.rect.y += int(self.velocity)

    def update_img(self):
        self.delay_counter += 1
        if self.delay_counter >= BIRD_IMAGE_UPDATE_DELAY_FRAME:
            self.image = next(Bird.images)
            self.delay_counter = 0

    def update_velocity(self):
        if self.check_clicked():
            self.velocity = JUMP_VELOCITY
        else:
            self.velocity += GRAVITY

    def update_bound(self):
        if self.is_below_floor():
            self.rect.bottom = MAIN_SCREEN_BOTTOM
            self.velocity = 0
        elif self.is_above_ceiling():
            self.rect.top = MAIN_SCREEN_TOP
            self.velocity = 0

    def is_below_floor(self):
        return self.rect.bottom > MAIN_SCREEN_BOTTOM

    def is_above_ceiling(self):
        return self.rect.top < 0
