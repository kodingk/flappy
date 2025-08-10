import pygame

class ClickEventObserver:
    def __init__(self):
        self.__clicked = False

    def check_clicked(self):
        if not self.__clicked and pygame.mouse.get_pressed()[0]:
            self.__clicked = True
            return True
        if self.__clicked and not pygame.mouse.get_pressed()[0]:
            self.__clicked = False

        return False
