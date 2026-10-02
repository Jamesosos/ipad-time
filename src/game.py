import pygame
import sys
from src.constants import *
from src.player import Player

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(COLOR_PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("漂浮夢境 (Floating Dreamscape) - MVP Test")
    clock = pygame.time.Clock()

    # 初始化物件
    player = Player(100, 100)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # 簡單的平台列表 (將從 level1.json 讀取，目前先手動建立)
    platforms = pygame.sprite.Group()
    platforms.add(Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)) # 地板
    platforms.add(Platform(200, 450, 150, 20))
    platforms.add(Platform(450, 350, 150, 20))
    platforms.add(Platform(650, 250, 150, 20))

    running = True
    while running:
        screen.fill(COLOR_BG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.vel_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            player.vel_x = PLAYER_SPEED
        else:
            player.vel_x = 0

        # 更新
        player_group.update(platforms)

        # 繪製
        platforms.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
