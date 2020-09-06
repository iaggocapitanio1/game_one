"""
@Description:
Provides an abstract class to build a ship.
"""
__author__ = "Iaggo Capitanio"
__copyright__ = "Copyright (C) 2020 Iaggo Capitanio"
__license__ = "Public Domain"


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

    def move_lasers(self, velocity, obj, height):
        """
        Move the lasers
        """
        pass

    def shoot(self) -> None:
        """
        The shoot of the ship.
        """

        pass

    def cool_down(self):
        """
        Handle the cool down counter.
        :return
        """
        pass
