import pygame


class Input:

    def __init__(self):
        self.quit = False
        self.key_downs = []
        self.key_pressed = []
        self.key_ups = []

    def update(self):
        self.key_downs = []
        self.key_ups = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.key_downs.append(key_name)
                self.key_pressed.append(key_name)
            elif event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self.key_pressed.remove(key_name)
                self.key_ups.append(key_name)

    def is_key_down(self, key_code):
        return key_code in self.key_downs

    def is_key_pressed(self, key_code):
        return key_code in self.key_pressed

    def is_key_up(self, key_code):
        return key_code in self.key_ups

