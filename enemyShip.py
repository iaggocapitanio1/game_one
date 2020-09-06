"""
@Description:
 Class to build an enemy ship.
"""
__author__ = "Iaggo Capitanio"
__copyright__ = "Copyright (C) 2020 Iaggo Capitanio"
__license__ = "Public Domain"

from shipAbstractGraphic import Ship
import pygame
import os
import typing as ty

file_resources = "assets"
try:
    RED_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_red_small.png'))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_green_small.png'))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_blue_small.png'))
    # player player
    YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_yellow.png'))
    # Lasers
    RED_LASER = pygame.image.load(os.path.join(file_resources, 'pixel_laser_red.png'))
    GREEN_LASER = pygame.image.load(os.path.join(file_resources, 'pixel_laser_green.png'))
    BLUE_LASER = pygame.image.load(os.path.join(file_resources, 'pixel_laser_blue.png'))
    YELLOW_LASER = pygame.image.load(os.path.join(file_resources, 'pixel_laser_yellow.png'))

except pygame.error:
    print("The file in the assets folder was not found, please try to put it in the right location: " +
          str(os.path.join(__file__, file_resources)))


class Enemy(Ship):
    """
    This class defines the enemy ships.
    """
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)

    }

    def __init__(self, x, y, color, health=100):
        super(Enemy, self).__init__(x, y, health=health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]

    def move(self, value: ty.Union[float, int]) -> None:
        """

        :param value: an float value to defines the velocity
        """
        self.y += value

    def get_height(self) -> float:
        """
        Overload the parent method: get the ship's height.
        :return:
        """
        return self.ship_img.get_height()

    def get_width(self):
        """
        Overload the parent method: get the ship's width.
        :return:
        """
        return self.ship_img.get_width()

    def draw(self, parent):
        """
        Overload: parent method: draw.
        :param parent: Parent is a pygame object, it means that it will be draw as a surface on the
         pygame objet (screen).
        """
        parent.blit(self.ship_img, (self.x, self.y))
