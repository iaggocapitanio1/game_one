"""
@Description:
A funny game. To play it, you must use the following keyboards:
W: to go up.
A: to fo left.
S: to go down.
D: to go right.
"""
__author__ = "Iaggo Capitanio"
__copyright__ = "Copyright (C) 2020 Iaggo Capitanio"
__license__ = "Public Domain"
__version__ = "1.0.1"

import pygame
import os
import time
import random
import sys
import typing as ty

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 550, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("StarWars")
# Load images
file_resources = "assets"

try:
    RED_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_red_small.png'))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_green_small.png'))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_blue_small.png'))
    # player player
    YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(file_resources, 'pixel_ship_yellow.png'))
    # Lasers
    RED_LASERS = pygame.image.load(os.path.join(file_resources, 'pixel_laser_red.png'))
    GREEN_LASERS = pygame.image.load(os.path.join(file_resources, 'pixel_laser_green.png'))
    BLUE_LASERS = pygame.image.load(os.path.join(file_resources, 'pixel_laser_blue.png'))
    YELLOW_LASERS = pygame.image.load(os.path.join(file_resources, 'pixel_laser_yellow.png'))
    # Background
    BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIN.get_height(),
                                                                                                    WIN.get_width()))
except pygame.error:
    print("The file in the assets folder was not found, please try to put it in the right location: " +
          str(os.path.join(__file__, file_resources)))


def main() -> None:
    """
    The main feature of this function is to run the game code, here is where all the game functionality works!

    :return None
    """
    run = True
    FPS = 60
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5
    player = Player(x=200, y=200)

    def redraw_window() -> None:
        """
        The main functionality of this method is to provides an update to the parent object. Here will be defined the
        match's scoreboard on the top of the screen also.
        """
        WIN.blit(BG, (0, 0))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        # left
        if keys[pygame.K_a] and (player.x - player_vel) > 0:
            player.x -= player_vel
        # right
        if keys[pygame.K_d] and (player.x + player_vel + player.get_width()) < WIN.get_width():
            player.x += player_vel
        # up
        if keys[pygame.K_w] and (player.y - player_vel) > 0:
            player.y -= player_vel
        # down
        if keys[pygame.K_s] and (player.y + player_vel + player.get_height()) < WIN.get_height():
            player.y += player_vel


# An Abstract Class

class Ship:
    """
    This is an abstract class, it defines the main features of the object: ship.
    """

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = list()
        self.cool_down_counter = 0

    # width getter
    def get_width(self) -> float:
        """

        :return: the width of the ship image.
        """
        pass

    def get_height(self) -> float:
        """

        :return: the height of the ship image.
        """
        pass

    def draw(self, parent) -> None:
        """

        :param parent: Parent is a pygame object, it means that it will be draw as a surface on the
         pygame objet (screen).
        """
        pass


class Player(Ship):
    """
        Inherits the Ship class.
    """

    def __init__(self, x, y, health=100):
        super(Player, self).__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASERS
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


if __name__ == "__main__":
    main()
