from superwires import games, color
import random

games.init(screen_width=800, screen_height=600, fps=60)

class Player(games.Sprite):
    image = games.load_image("player.png")
    sound_shoot = games.load_sound("sounds/pistol.wav")
    sound_reload = games.load_sound("sounds/reload.wav")
    sound_empty = games.load_sound("sounds/empty_gun.wav")
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
        #Moving Left and Right
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_d):
            self.x += 5

        #Shooting
        if self.shoot_wait > 0:
            self.shoot_wait -= 1
        if games.keyboard.is_pressed(games.K_SPACE) and self.shoot_wait == 0 and self.ammo_count.value > 0:
            shoot = Bullet(self.x + 17, self.y - 50)
            games.screen.add(shoot)
            Player.sound_shoot.play()
            self.shoot_wait = Player.NEXT_SHOT
            self.ammo_count.value -= 1

        #Empty Clip
        if games.keyboard.is_pressed(games.K_SPACE) and self.shoot_wait == 0 and self.ammo_count.value == 0:
            Player.sound_empty.play()
            self.shoot_wait = Player.NEXT_SHOT

        #Reload
        if games.keyboard.is_pressed(games.K_r) and self.ammo_count.value == 0 and self.shoot_wait == 0:
            self.ammo_count.value = 20
            Player.sound_reload.play()
            self.shoot_wait = Player.NEXT_SHOT

        #Stops Player from going off screen
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

    def update(self):
        for sprite in self.overlapping_sprites:
            sprite.destroy()
            self.destroy()
            death = ZombieDeath(sprite.x, sprite.y)
            games.screen.add(death)



class ZombieWalk(games.Animation):
    images = ["zombie/walk/walk0001.png", "zombie/walk/walk0002.png", "zombie/walk/walk0003.png", "zombie/walk/walk0004.png", "zombie/walk/walk0005.png",
              "zombie/walk/walk0006.png", "zombie/walk/walk0007.png", "zombie/walk/walk0008.png", "zombie/walk/walk0009.png", "zombie/walk/walk0010.png",
              "zombie/walk/walk0011.png", "zombie/walk/walk0012.png", "zombie/walk/walk0013.png", "zombie/walk/walk0014.png", "zombie/walk/walk0015.png",
              "zombie/walk/walk0016.png", "zombie/walk/walk0017.png", "zombie/walk/walk0018.png", "zombie/walk/walk0019.png", "zombie/walk/walk0020.png",
              "zombie/walk/walk0021.png", "zombie/walk/walk0022.png", "zombie/walk/walk0023.png", "zombie/walk/walk0024.png", "zombie/walk/walk0025.png",
              "zombie/walk/walk0026.png", "zombie/walk/walk0027.png", "zombie/walk/walk0028.png", "zombie/walk/walk0029.png", "zombie/walk/walk0030.png", "zombie/walk/walk0031.png"]


    def __init__(self, x, y):
        super(ZombieWalk, self).__init__(images = ZombieWalk.images,
                                         x = x,
                                         y = y,
                                         angle = 90,
                                         dy = 3,
                                         n_repeats = 0,
                                         repeat_interval = 1)




class ZombieDeath(games.Animation):
    images = ["zombie/death01/death01_0001.png", "zombie/death01/death01_0002.png", "zombie/death01/death01_0003.png", "zombie/death01/death01_0004.png",
              "zombie/death01/death01_0005.png", "zombie/death01/death01_0006.png", "zombie/death01/death01_0007.png", "zombie/death01/death01_0008.png",
              "zombie/death01/death01_0009.png", "zombie/death01/death01_0010.png", "zombie/death01/death01_0011.png", "zombie/death01/death01_0012.png",
              "zombie/death01/death01_0013.png", "zombie/death01/death01_0014.png", "zombie/death01/death01_0015.png", "zombie/death01/death01_0016.png"]

    def __init__(self, x, y):
        super(ZombieWalk, self).__init__(images = ZombieDeath.images,
                                         x = x,
                                         y = y,
                                         angle = 90,
                                         n_repeats = 1,
                                         repeat_interval = 1)


def main():
    bg = games.load_image("background.jpg")
    games.screen.background = bg

    games.music.load("sounds/music.wav")
    games.music.play(-1)


    p = Player()
    games.screen.add(p)

    z = ZombieWalk(400,0)
    games.screen.add(z)

    games.screen.mainloop()




main()
