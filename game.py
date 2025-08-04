import pygame


from click_event_observer import ClickEventObserver
from constants import FRAME_PER_SECOND, SCREEN_WIDTH, SCREEN_HEIGHT
from bg import get_bg_group, get_ground_group
from bird import get_bird_group
from pipe import get_pipe_group

class Game(ClickEventObserver):
    def __init__(self):
        super().__init__()
        self.running = True

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.register_sprite_groups()

    def register_sprite_groups(self):
        self.groups = {
            "bg": get_bg_group(),
            "bird": get_bird_group(),
            "pipe": get_pipe_group(),
            "ground": get_ground_group(),
        }

    def run(self):
        while self.running:
            self.clock.tick(FRAME_PER_SECOND)
            self.update_and_draw_groups()
            self.check_collision()
            self.check_quit_event()

        pygame.quit()

    def update_and_draw_groups(self):
        for key, group in self.groups.items():
            if key != "restart":
                group.update()
                group.draw(self.screen)
        pygame.display.flip()

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def check_collision(self):
        if self.has_collided():
            self.running = False

    def has_collided(self):
        bird = self.groups["bird"].sprites()[0]
        pipes = self.groups["pipe"].sprites()
        ground = self.groups["ground"].sprites()[0]

        for pipe in pipes:
            if bird.rect.colliderect(pipe.rect):
                return True

        return bird.rect.colliderect(ground.rect)
