from superwires import games, color
import random

games.init(screen_width=800, screen_height=600, fps=60)

class Player(games.Sprite):
    image = games.load_image("player.png")
    sound_shoot = games.load_sound("sounds/pistol.wav")
    sound_reload = games.load_sound("sounds/reload.wav")
    NEXT_SHOT = 25

    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                     x = games.screen.width/2,
                                     y = 560)

        self.shoot_wait = 0

        self.ammo_text = games.Text(value = "Ammo",
                                    size = 50,
                                    color = color.white,
                                    x = 60,
                                    y = 40,
                                    is_collideable = False)

        self.ammo_count = games.Text(value = 20,
                                      size = 50,
                            color = color.white,
                                         x = 60,
                                          y = 80,
                           is_collideable = False)

        games.screen.add(self.ammo_text)
        games.screen.add(self.ammo_count)


    def update(self):
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_d):
            self.x += 5

        if self.shoot_wait > 0:
            self.shoot_wait -= 1
        if games.keyboard.is_pressed(games.K_SPACE) and self.shoot_wait == 0 and self.ammo_count.value > 0:
            shoot = Bullet(self.x + 17, self.y - 50)
            games.screen.add(shoot)
            Player.sound_shoot.play()
            self.shoot_wait = Player.NEXT_SHOT
            self.ammo_count.value -= 1

        if games.keyboard.is_pressed(games.K_r) and self.ammo_count.value == 0:
            self.ammo_count.value = 20
            Player.sound_reload.play()


        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

class Bullet(games.Sprite):
    image = games.load_image("bullet.png")
    LIFE = 40

    def __init__(self, x, y):
        super(Bullet, self).__init__(image = Bullet.image,
                                     x = x,
                                     y = y,
                                     dy = -10)



def main():
    bg = games.load_image("background.jpg")
    games.screen.background = bg


    p = Player()
    games.screen.add(p)
    games.screen.mainloop()




main()
