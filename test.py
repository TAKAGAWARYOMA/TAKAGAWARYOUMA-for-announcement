import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# 画面サイズとタイトルの設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("シューティングゲーム")

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ゲームのフレームレート設定
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 2 * self.height
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def shoot(self):
        bullet = Bullet(self.x, self.y)
        bullets.append(bullet)

class Bullet:
    def __init__(self, x, y):
        self.width = 3
        self.height = 5
        self.speed = -10
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Enemy:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.x = random.randrange(SCREEN_WIDTH - self.width)
        self.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 5)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

player = Player()
bullets = []
enemis = []

for _ in range(5):
    enemy = Enemy()
    enemis.append(enemy)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす

        # ゲームの更新
        player.update()

        for enemy in enemis:
            enemy.update()
            if enemy.y >= SCREEN_HEIGHT:
                enemis.remove(enemy)

        for bullet in bullets:
            bullet.update()
            if bullet.y <= bullet.height:
                bullets.remove(bullet)

        for enemy in enemis:
            if player.rect.colliderect(enemy.rect):
                print("衝突しました！")

        for enemy in enemis:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemis.remove(enemy)
                    bullets.remove(bullet)
                    print("衝突しました！")

        pygame.draw.rect(screen, RED, player.rect)

        for enemy in enemis:
            pygame.draw.rect(screen, RED, enemy.rect)

        for bullet in bullets:
            pygame.draw.rect(screen, RED, bullet.rect)

        pygame.display.flip()
        clock.tick(60)  # FPSを60に設定

if __name__ == "__main__":
    main()
