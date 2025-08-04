import pygame

class ClickEventObserver:
    def __init__(self):
        self.clicked = False

    def check_clicked(self):
        if not self.clicked and pygame.mouse.get_pressed()[0]:
            self.clicked = True
            return True
        if self.clicked and not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return False
