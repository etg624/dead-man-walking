# pygame template for new pygame proj
# sprite URL https://i.stack.imgur.com/C3ZwL.png
import pygame
import random
import os
from os import path

WIDTH = 500
HEIGHT = 500
FPS = 60

img_dir = path.join(path.dirname(__file__), 'img')

# define colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead Man Walking")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.radius = 6
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.image.set_colorkey(WHITE)
        self.rect.centerx = (WIDTH / 2)
        self.rect.left = 0

        self.rect.bottom = HEIGHT - 10
        self.x_speed = 0

    def update(self):

        self.x_speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_speed = -8
        if keystate[pygame.K_RIGHT]:
            self.x_speed = 8
        self.rect.x += self.x_speed
        if self.rect.right > WIDTH:

            self.rect.right = 0

        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boulder_image
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.image.set_colorkey(BLACK)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.y_speed = random.randrange(1, 8)
        self.x_speed = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):

        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH)
            self.rect.y = random.randrange(-100, -40)
            self.y_speed = random.randrange(1, 8)

        # start game and create window


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):

        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


def show_game_over_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "DEAD MAN WALKING", 64, WIDTH / 2, HEIGHT / 4)
    # todo add instructions
    draw_text(screen, "You wake up dead, (yes I know) only to find yourself lost",
              20, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "on a never ending trail.",
              20, WIDTH / 2, HEIGHT / 1.9)
    draw_text(screen, "Only to realize more and more rocks falling at your head as you move along.",
              20, WIDTH / 2, HEIGHT / 1.8)
    draw_text(screen, "How long can you survive until you are...",
              20, WIDTH / 2, HEIGHT / 1.65)
    draw_text(screen, " FOREVER DEAD?!",
              28, WIDTH / 2, HEIGHT / 1.5)
    draw_text(screen, "Press any key to begin your journey to impending doom", 18,
              WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

            # load all graphics
background = pygame.image.load(
    path.join(img_dir, 'grassy_plains.jpg')).convert()
background_rect = background.get_rect()
player_image = pygame.image.load(
    os.path.join(img_dir, 'walk_right0000.png')).convert()
boulder_image = pygame.image.load(
    os.path.join(img_dir, 'boulder.png')).convert()


game_over = True
running = True
while running:
    if game_over:
        score = 0
        show_game_over_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()

        all_sprites.add(player)
        clock.tick(FPS)
   # Process events or input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # update
    all_sprites.update()

    if player.rect.right >= 498 and player.rect.right <= 499:
        score += 1
        for i in range(1):
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        # draw_text(screen, str(score), 18, WIDTH / 2, 10)

    # check if player hit mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(
        player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        game_over = True

    # draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    # after drawing everything flip display
    pygame.display.flip()


pygame.quit()
