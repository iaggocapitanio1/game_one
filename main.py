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
__version__ = "1.1.1"

import typing as ty
import pygame
import os
import random
from enemyShip import Enemy
from playerShip import Player

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("StarWars")
# Load images
file_resources = "assets"


def collide(obj1, obj2) -> ty.Union[None, tuple]:
    """
    :param obj1: pygame object with a mask that covers its borders.
    :param obj2:  pygame object with a mask that covers its borders.
    """
    offset_x = obj1.x - obj2.x
    offset_y = obj1.y - obj2.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


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
    # a factor related to the normal probability of the enemy shooting
    prob = 4
    # the laser velocity
    laser_velocity = 5
    # defines if the player lost the game
    lost = False
    # while run is true the application will keep running.
    run = True
    # this variable defines the number of frames per second that will be used inside the clock tick.
    FPS = 60
    # the start level.
    level = 0
    # the number of lives at the start.
    lives = 5
    # instance of the clock
    clock = pygame.time.Clock()
    # main parent font.
    main_font = pygame.font.SysFont("comicsans", 50)
    # lost message font.
    lost_font = pygame.font.SysFont("comicsans", 60)
    # the velocity of the ship
    player_vel = 5
    # the set of enemies list at start.
    enemies = []
    # the starting amount of enemies per wave.
    wave_length = 5
    # the enemy velocity
    enemy_vel = 2
    # Creation of the player object.
    player = Player(x=200, y=200)

    def redraw_window() -> None:
        """
        The main functionality of this method is to provides an update to the parent object. Here will be defined the
        match's scoreboard on the top of the screen also.
        """
        # BASIC SCREEN LAYOUT:
        #       # background image
        #   # scoreboard
        #   # lives label
        #   # level label
        ################################################################################################################
        # set the background image
        WIN.blit(BG, (0, 0))
        # draw text
        try:
            # noinspection PyCompatibility
            lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
            # noinspection PyCompatibility
            level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        except SyntaxError:
            lives_label = main_font.render("Lives: {}".format(lives), 1, (255, 255, 255))
            # noinspection PyCompatibility
            level_label = main_font.render("Level:{} ".format(level), 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # get the enemies from the array of images
        ################################################################################################################
        for enemy in enemies:
            enemy.draw(WIN)

        # draw the player ship
        ################################################################################################################
        player.draw(WIN)
        ################################################################################################################

        # if the player lost, this message will pop up.
        ################################################################################################################
        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255, 255, 255))
            x_pos = WIN.get_width() / 2 - lost_label.get_width() / 2
            WIN.blit(lost_label, (int(x_pos), 350))
        # update the game
        ################################################################################################################
        pygame.display.update()

    # lost count will be used to specifies the interim before the game restarts.
    # starting it at zero.
    lost_count = 0
    while run:
        clock.tick(FPS)
        redraw_window()
        if lives <= 0 or player.health <= 0:
            lost = True
            # this will defines
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue  # The difference between continue and pass is tha continue forces the start to a new iterator
                # and pass mean that there is no code here, so it will continue through the body loop. In another words,
                # pass will execute the code bellow and continue will stop and append one vale to the count.
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(100, WIN.get_width() - 100), random.randrange(-1500, -100),
                              random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

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
        if keys[pygame.K_s] and (player.y + player_vel + player.get_height() + 20) < WIN.get_height():
            player.y += player_vel
        # shoot
        if keys[pygame.K_SPACE]:
            player.shoot()

        ################################################################################################################
        # This part of the code defines the maximum range of the enemies ships, if they pass though the y value:
        # actual y enemy position plus the window height, the enemy ship will be removed from the enemies list.
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(velocity=laser_velocity, obj=player, height=WIN.get_height())

            if random.randrange(0, prob * FPS) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            if enemy.y + enemy.get_height() > WIN.get_height():
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_velocity, enemies, height=WIN.get_height())


def main_menu():
    """
    Main menu if the player loses.
    """
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin....", 1, (255, 255, 255))
        x_pos = int(WIN.get_width()/2 - title_label.get_width()/2)
        y_pos = int(WIN.get_height()/2)
        WIN.blit(title_label, (x_pos, y_pos))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main()


if __name__ == "__main__":
    main_menu()
