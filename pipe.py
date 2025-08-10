import pygame
import random

from scrollable import Scrollable
from constants import MAIN_SCREEN_BOTTOM, SCREEN_WIDTH, MAIN_SCREEN_TOP


PIPE_IMAGE_PATH = "img/pipe.png"
PIPE_PERIOD_IN_MILLISECONDS = 1000
PIPE_GAP, PADDING = 300, 50


def get_pipe_group():
    return PipeGroup()


class Pipe(Scrollable):
    def __init__(self, x, y, rotated):
        self.scored = False  # 아직 점수로 계산되지 않음
        self.rotated = rotated
        super().__init__(x, y, PIPE_IMAGE_PATH)
        if rotated:
            self.image = pygame.transform.rotate(self.image, 180)

    @staticmethod
    def create_pipe_pair():
        upper, lower = Pipe(SCREEN_WIDTH, 0, True), Pipe(SCREEN_WIDTH, 0, False)
        upper.rect.bottom = random.randint(MAIN_SCREEN_TOP + PADDING, MAIN_SCREEN_BOTTOM - PIPE_GAP - PADDING)
        lower.rect.top = upper.rect.bottom + PIPE_GAP
        return upper, lower


class PipeGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.last_spawn_time = pygame.time.get_ticks()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > PIPE_PERIOD_IN_MILLISECONDS:
            self.last_spawn_time = current_time
            self.add(*Pipe.create_pipe_pair())

        self.remove_offscreen()

    def remove_offscreen(self):
        self.remove(*[pipe for pipe in self if pipe.rect.right < 0])
