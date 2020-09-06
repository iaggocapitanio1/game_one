import pygame
import os
import time
import random
import sys

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


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5
    player = Player(x=200, y=200)

    def redraw_window():
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
        if keys[pygame.K_d] and (player.x + player_vel + player.width) < WIN.get_width():
            player.x += player_vel
        # up
        if keys[pygame.K_w] and (player.y - player_vel) > 0:
            player.y -= player_vel
        # down
        if keys[pygame.K_s] and (player.y + player_vel + player.height) < WIN.get_height():
            player.y += player_vel



# An Abstract Class

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = list()
        self.cool_down_counter = 0
        self.width = 50
        self.height = 50

    def draw(self, parent):
        parent.blit(self.ship_img, (self.x, self.y))


class Player(Ship):
    def __init__(self, x, y, health=100):
        super(Player, self).__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASERS
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


if __name__ == "__main__":
    main()
