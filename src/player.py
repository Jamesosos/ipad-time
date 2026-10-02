import pygame
from src.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(COLOR_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 速度屬性
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        # 重力影響
        self.vel_y += GRAVITY
        
        # 更新位置
        self.rect.x += self.vel_x
        self.check_collisions(platforms, 'x')
        
        self.rect.y += self.vel_y
        self.check_collisions(platforms, 'y')

        # 限制在螢幕內
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

    def check_collisions(self, platforms, direction):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if direction == 'x':
                    if self.vel_x > 0:
                        self.rect.right = platform.rect.left
                    elif self.vel_x < 0:
                        self.rect.left = platform.rect.right
                elif direction == 'y':
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:
                        self.rect.top = platform.rect.bottom
                        self.vel_y = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False
