import pygame
import sys

from core.input import Input


class Base:

    def __init__(self, screen_size=(512, 512)):
        pygame.init()
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        pygame.display.set_caption("Graphics Window")
        self.running = True
        self.clock = pygame.time.Clock()
        self.input = Input()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while self.running:
            self.update()

            self.input.update()
            if self.input.quit:
                self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

