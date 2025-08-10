import enum
import pygame

from constants import FRAME_PER_SECOND, SCREEN_WIDTH, SCREEN_HEIGHT
from bg import get_bg_group, get_ground_group
from bird import get_bird_group
from pipe import get_pipe_group
from restart import get_restart_group

class GameState(enum.Enum):
    END = 0
    RUNNING = 1
    RESTART = 2

class Game():
    def __init__(self):
        super().__init__()
        self.state = GameState.RUNNING

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.register_sprite_groups()

    def register_sprite_groups(self):
        self.groups = {
            "bg": get_bg_group(),
            "bird": get_bird_group(),
            "pipe": get_pipe_group(),
            "ground": get_ground_group(),
            "restart": get_restart_group(),
        }

    def run(self):
        while self.state != GameState.END:
            self.clock.tick(FRAME_PER_SECOND)
            self.update_and_draw_groups()

            if self.state == GameState.RUNNING:
                self.check_collision()
            elif self.state == GameState.RESTART and self.groups["restart"].check_clicked():
                self.__init__()

            self.check_quit_event()

    def update_and_draw_groups(self):
        if self.state == GameState.RESTART:
            self.update_and_draw_group("restart")
        elif self.state == GameState.RUNNING:
            self.update_and_draw_group("bg", "bird", "pipe", "ground")
        pygame.display.flip()

    def update_and_draw_group(self, *group_keys):
        for key in group_keys:
            group = self.groups[key]
            group.update()
            group.draw(self.screen)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.END

    def check_collision(self):
        if self.has_collided():
            self.state = GameState.RESTART

    def has_collided(self):
        bird = self.groups["bird"].sprites()[0]
        pipes = self.groups["pipe"].sprites()
        ground = self.groups["ground"].sprites()[0]

        for pipe in pipes:
            if bird.rect.colliderect(pipe.rect):
                return True

        return bird.rect.colliderect(ground.rect)
