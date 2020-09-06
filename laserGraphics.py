"""
@Description:
 Class to build athe lasers.
"""
__author__ = "Iaggo Capitanio"
__copyright__ = "Copyright (C) 2020 Iaggo Capitanio"
__license__ = "Public Domain"

import pygame
import typing as ty
from shipAbstractGraphic import Ship


class Laser:
    """
    Create an laser class
    """

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    @staticmethod
    def collide(obj1, obj2) -> ty.Union[None, tuple]:
        """
        :param obj1: pygame object with a mask that covers its borders.
        :param obj2:  pygame object with a mask that covers its borders.
        """
        offset_x = obj1.x - obj2.x
        offset_y = obj1.y - obj2.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

    def draw(self, window: pygame.display) -> None:
        """
        Display the laser.
        :param window: where it'll be displayed.
        """
        window.blit(self.img, (self.x, self.y))

    def move(self, vel: float) -> None:
        """
        This function allows the laser object to move with an velocity.
        :param vel: the velocity of the object.
        """
        self.y += vel

    def off_screen(self, height: float) -> bool:
        """
        Tells if the laser is in or out of the screen.
        :return return an boolean that tells if the laser is in or off.

        """
        return not(height >= self.y >= 0)

    def collision(self, obj: pygame.image) -> ty.Union[None, tuple]:
        """
        This function tells if the laser collides with a ship.
        :param obj: the object that were drawn.
        :return:
        """
        return self.collide(obj, self)
