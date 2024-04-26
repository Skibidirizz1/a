import pygame

from player import Player
from bullet import Bullet
from explosion import Explosion
from enemy_top import EnemyTop
from enemy_left import EnemyLeft
from enemy_right import EnemyRight
from enemy_bottom import EnemyBottom

pygame.init()

width = 1366
height = 768
fps = 30
game_name = "Shooter"

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

snd_dir = 'media/snd/'
img_dir = 'media/img/'

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

icon = pygame.image.load(img_dir + 'icon.png')
pygame.display.set_icon(icon)


def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]


all_sprites = pygame.sprite.Group()
mobs_sprites = pygame.sprite.Group()
bullets_sprites = pygame.sprite.Group()
players_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
players_sprites.add(player)

enemy_bottom = EnemyBottom()
all_sprites.add(enemy_bottom)
mobs_sprites.add(enemy_bottom)
enemy_right = EnemyRight()
all_sprites.add(enemy_right)
mobs_sprites.add(enemy_right)
enemy_left = EnemyLeft()
all_sprites.add(enemy_left)
mobs_sprites.add(enemy_left)
enemy_top = EnemyTop()
all_sprites.add(enemy_top)
mobs_sprites.add(enemy_top)

timer = pygame.time.Clock()

# Иногда нужно добавлять pygame.mixer.init()
pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

run = True

while run:
    timer.tick(fps)
    all_sprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.snd_shoot.play()
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets_sprites.add(bullet)

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, True)
    if shots:
        sprite = get_hit_sprite(shots)
        sprite.snd_expl.play()

    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()

    screen.fill(CYAN)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
