"""This module contains the Image class, which is a subclass of the Sprite class."""

import os
import pygame

from .sprite import Sprite
from ..io import convert_pos


class Image(Sprite):
    def __init__(
        self, image, x=0, y=0, angle=0, size=100, transparency=100
    ):  # pylint: disable=too-many-arguments
        super().__init__()
        if isinstance(image, str):
            if not os.path.isfile(image):
                raise FileNotFoundError(f"Image file '{image}' not found.")
            image = pygame.image.load(image)
        self._image = image
        self._x = x
        self._y = y
        self._angle = angle
        self._size = size
        self._transparency = transparency
        self.rect = self._image.get_rect()
        self.update()

    def update(self):
        """Update the image's position, size, angle, and transparency."""
        if self._should_recompute:
            self._image = pygame.transform.scale(
                self._image,
                (self.width * self.size // 100, self.height * self.size // 100),
            )
            self._image = pygame.transform.rotate(self._image, self.angle)
            self._image.set_alpha(self.transparency * 2.55)
            self.rect = self._image.get_rect()
            pos = convert_pos(self.x, self.y)
            self.rect.center = pos
            super().update()
