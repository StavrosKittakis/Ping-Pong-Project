from pygame import *

window = display.set_mode((700, 500))
display.set_caption("pygame window")
window.fill((173, 216, 230))
font.init()
font = font.Font(None, 100)

class SpriteCharacter(sprite.Sprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def render(self, window):
        window.blit(self.image, self.rect.topleft)

class Racket_L(SpriteCharacter):
    def movement(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

class Racket_R(SpriteCharacter):
    def movement(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

racket_left = Racket_L("racket.png", 10, 300, 3)
racket_right = Racket_R("racket.png", 620, 300, 3)
ball = SpriteCharacter("ball.png", 400, 100, 3)
pill = SpriteCharacter("pill.png", 400, 300, 2)

def reset_game():
    global finish, speed_x, speed_y, speed_pill_x, speed_pill_y, pill_active
    ball.rect.x, ball.rect.y = 400, 100
    racket_left.rect.y = 300
    racket_right.rect.y = 300
    pill.rect.x, pill.rect.y = 400, 300
    racket_left.speed = 3
    racket_right.speed = 3
    speed_x, speed_y = 3, 3
    speed_pill_x, speed_pill_y = -2, -2
    pill_active = True
    finish = False

game = True
clock = time.Clock()
FPS = 90

speed_x = 3
speed_y = 3
speed_pill_x = -2
speed_pill_y = -2
pill_active = True
finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    key_pressed = key.get_pressed()
    if key_pressed[K_r]:
        reset_game()

    if not finish:
        window.fill((173, 216, 230))

        racket_left.render(window)
        racket_left.movement()

        racket_right.render(window)
        racket_right.movement()

        ball.render(window)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if pill_active:
            pill.render(window)
            pill.rect.x += speed_pill_x
            pill.rect.y += speed_pill_y

        if sprite.collide_rect(racket_left, pill):
            racket_left.speed = 5
            pill_active = False

        if sprite.collide_rect(racket_right, pill):
            racket_right.speed = 5
            pill_active = False

        if sprite.collide_rect(racket_left, ball) or sprite.collide_rect(racket_right, ball):
            speed_x = speed_x * (-1)

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y = speed_y * (-1)

        if pill_active and (pill.rect.y > 450 or pill.rect.y < 0):
            speed_pill_y = speed_pill_y * (-1)

        if ball.rect.x < 0:
            finish = True
            lose1 = font.render("Player1 loses", True, (255, 0, 0))
            window.blit(lose1, (200, 200))

        if ball.rect.x > 700:
            finish = True
            lose2 = font.render("Player2 loses", True, (255, 0, 0))
            window.blit(lose2, (200, 200))

    clock.tick(FPS)
    display.update()
