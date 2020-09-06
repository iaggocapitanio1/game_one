"""
@Description:
Provides a class to build  the player ship,
"""
__author__ = "Iaggo Capitanio"
__copyright__ = "Copyright (C) 2020 Iaggo Capitanio"
__license__ = "Public Domain"

from shipAbstractGraphic import Ship
from laserGraphics import Laser
import pygame
import os

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


class Player(Ship):
    """
        Inherits the Ship class.
    """
    COOL_DOWN = 15  # constant class variable.

    def __init__(self, x, y, health=100):
        super(Player, self).__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

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
        for laser in self.lasers:
            laser.draw(parent)

    def move_lasers(self, velocity, objects, height):
        """
        Move the lasers
        """
        self.cool_down()
        for laser in self.lasers:
            laser.move(velocity)
            # if laser id off the screen, that it will be deleted from the laser list
            if laser.off_screen(height):
                self.lasers.remove(laser)
            else:
                for obj in objects:
                    if laser.collision(obj):
                        objects.remove(obj)
                        self.lasers.remove(laser)

    def shoot(self):
        """
        create a laser.
        """
        if self.cool_down_counter == 0:
            laser = Laser(x=self.x, y=self.y, img=self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def cool_down(self):
        """
        Handle the cool down counter. This will make th laser wait until another laser
        can be released.
        """
        if self.cool_down_counter >= self.COOL_DOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
