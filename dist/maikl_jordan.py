from pygame import *
import pygame_menu

init()


class GameObject(sprite.Sprite):
    def __init__(self, picture, x, y, w, h, s):
        super().__init__()
        self.picture = transform.scale(image.load(picture), (w, h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = s

    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Ball(GameObject):
    def __init__(self, picture, x, y, w, h, sx, sy):
        super().__init__(picture, x, y, w, h, None)
        self.speed_x = sx
        self.speed_y = sy

    def update(self):
        global score_b, score_r, start_speed

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.colliderect(platform_l):
            self.speed_x *= -1.1
            kick.play()
        if self.colliderect(platform_r):
            self.speed_x *= -1.1
            kick.play()
        if self.colliderect(wall_u):
            self.speed_y *= -1
        if self.colliderect(wall_d):
            self.speed_y *= -1
        if self.rect.x >= mw_w - 40:
            score_b += 1
            self.rect.x = mw_w - 300
            self.speed_x = otr_start_speed
        if self.rect.x <= -20:
            score_r += 1
            self.rect.x = 300
            self.speed_x = start_speed
        if self.speed_x >= 20 or self.speed_x <= -20:
            finish_him.play()


class Platform(GameObject):
    def update(self, k_u, k_d):
        key_pressed = key.get_pressed()
        if key_pressed[k_u] and self.rect.y > 20:
            self.rect.y -= self.speed
        if key_pressed[k_d] and self.rect.y < mw_h - 220:
            self.rect.y += self.speed


def reset_game():
    global score_b, score_r, start_x, start_y
    score_b = 0
    score_r = 0
    start_x, start_y = mw_w / 2, mw_h / 2


mw_w = 1200
mw_h = 800
score_b = 0
score_r = 0
start_x, start_y = mw_w / 2, mw_h / 2
start_speed = 5
otr_start_speed = start_speed * -1

mixer.init()
mixer.music.load("assets/music/bc song.ogg")
mixer.music.set_volume(0.02)
mixer.music.play()

kick = mixer.Sound("assets/music/kick.ogg")
finish_him = mixer.Sound("assets/music/finish_him.ogg")
iamblue = mixer.Sound("assets/music/blue.ogg")
leddyred = mixer.Sound("assets/music/red.ogg")

font1 = font.SysFont("Impact", 40)
font2 = font.SysFont("Impact", 80)

mw = display.set_mode((mw_w, mw_h))
display.set_caption("basketball")
clock = time.Clock()
background = transform.scale(image.load("assets/new bc.png"), (mw_w, mw_h))
blue = transform.scale(image.load("assets/blue.png"), (mw_w, mw_h))
red = transform.scale(image.load("assets/red.png"), (mw_w, mw_h))
platform_l = Platform("assets/platform.png", 10, mw_h / 2, 40, 200, 5)
platform_r = Platform("assets/platform.png", mw_w - 50, mw_h / 2, 40, 200, 5)
ball = Ball("assets/basketball ball.png", start_x, start_y, 80, 80, start_speed, 5)
wall_u = GameObject("assets/walls.png", 0, 0, mw_w, 20, 0)
wall_d = GameObject("assets/walls.png", 0, mw_h - 20, mw_w, 20, 0)


def main_3():
    amount_round = 3
    finish = False
    while True:
        red_win = font2.render("КРАСНЫЙ ВЫЙГРАЛ", True, (255, 255, 255))
        blue_win = font2.render("СИНИЙ ВЫЙГРАЛ", True, (255, 255, 255))
        score = font1.render(f"Счёт: {score_b}|{score_r}", True, (255, 255, 255))

        for e in event.get():
            if e.type == QUIT:
                reset_game()
                return
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    finish = not finish

        if not finish:

            mw.blit(background, (0, 0))
            wall_u.draw()
            wall_d.draw()
            mw.blit(score, (20, 40))
            platform_l.draw()
            platform_l.update(K_w, K_s)
            platform_r.draw()
            platform_r.update(K_UP, K_DOWN)
            ball.draw()
            ball.update()

            if score_b == amount_round:
                mw.blit(blue, (0, 0))
                mw.blit(blue_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                iamblue.play()
                finish = True
                reset_game()

            if score_r == amount_round:
                mw.blit(red, (0, 0))
                mw.blit(red_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                leddyred.play()
                finish = True
                reset_game()

            display.update()
            clock.tick(60)


def main_5():
    amount_round = 5
    finish = False
    while True:
        for e in event.get():
            if e.type == QUIT:
                reset_game()
                return

            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    finish = not finish

        if not finish:
            red_win = font2.render("КРАСНЫЙ ВЫЙГРАЛ", True, (255, 255, 255))
            blue_win = font2.render("СИНИЙ ВЫЙГРАЛ", True, (255, 255, 255))
            score = font1.render(f"Счёт: {score_b}|{score_r}", True, (255, 255, 255))
            mw.blit(background, (0, 0))
            wall_u.draw()
            wall_d.draw()
            mw.blit(score, (20, 40))
            platform_l.draw()
            platform_l.update(K_w, K_s)
            platform_r.draw()
            platform_r.update(K_UP, K_DOWN)
            ball.draw()
            ball.update()

            if score_b == amount_round:
                mw.blit(blue, (0, 0))
                mw.blit(blue_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                iamblue.play()
                finish = True
                reset_game()

            if score_r == amount_round:
                mw.blit(red, (0, 0))
                mw.blit(red_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                leddyred.play()
                finish = True
                reset_game()

            display.update()
            clock.tick(60)


def main_10():
    amount_round = 10
    finish = False
    while True:
        for e in event.get():
            if e.type == QUIT:
                reset_game()
                return

            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    finish = not finish

        if not finish:
            red_win = font2.render("КРАСНЫЙ ВЫЙГРАЛ", True, (255, 255, 255))
            blue_win = font2.render("СИНИЙ ВЫЙГРАЛ", True, (255, 255, 255))
            score = font1.render(f"Счёт: {score_b}|{score_r}", True, (255, 255, 255))
            mw.blit(background, (0, 0))
            wall_u.draw()
            wall_d.draw()
            mw.blit(score, (20, 40))
            platform_l.draw()
            platform_l.update(K_w, K_s)
            platform_r.draw()
            platform_r.update(K_UP, K_DOWN)
            ball.draw()
            ball.update()

            if score_b == amount_round:
                mw.blit(blue, (0, 0))
                mw.blit(blue_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                iamblue.play()
                finish = True
                reset_game()

            if score_r == amount_round:
                mw.blit(red, (0, 0))
                mw.blit(red_win, (mw_w / 2 - 230, mw_h / 2 - 100))
                leddyred.play()
                finish = True
                reset_game()

            display.update()
            clock.tick(60)


def start_menu():
    menu = pygame_menu.Menu("basketball", mw_w, mw_h, theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button("3 rounds", main_3)
    menu.add.button("5 rounds", main_5)
    menu.add.button("10 rounds", main_10)
    menu.add.button("exit", pygame_menu.events.EXIT)
    menu.mainloop(mw)


start_menu()