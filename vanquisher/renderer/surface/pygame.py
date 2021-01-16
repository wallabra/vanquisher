"""
Defines a pygame surface that implements the
FramebufferSurface interface.
"""

import typing

import pygame

from . import FramebufferSurface


class PygameSurface(FramebufferSurface):
    """
    A pygame surface, used when rendering the
    game to a pygame window.

    __init__ takes the same parameters as
    pygame.display.set_mode; see the pygame
    documentation on how to use those.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes this surface, including initializing
        the underlying Pygame surface.
        """

        self.surf = pygame.display.set_mode(*args, **kwargs)

    def get_size(self) -> typing.Tuple[int, int]:
        """
        Returns the size of the pygame window.

        For all intents and purposes, this is the size
        that the renderer uses.
        """

        return pygame.display.get_window_size(self.surf)

    def plot_pixel(self, x: int, y: int, rgb: typing.Tuple[float, float, float]):
        """
        Plots an RGB pixel at the specified position with the
        specified colour, within the pygame window.
        """
        self.surf.set_at((x, y), rgb)

    def plot_rect(
        self,
        xy1: typing.Tuple[int, int],
        xy2: typing.Tuple[int, int],
        rgb: typing.Tuple[float, float, float],
    ):
        """
        This implementation uses pygame's utilities to fill
        a rectangle of the specified colour between the
        specified corners.
        """
        self.surf.fill(rgb, (*xy1, *xy2))

    def update(self):
        """
        Updates the pygame surface.
        """
        pygame.display.updat()