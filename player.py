from spritesheet import SpriteSheet


class Player:
    def __init__(self, name='', sprite=None, x=0, y=0):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        spritesheet = SpriteSheet(f'./assets/players/{sprite}.png')
        rects = []
        for line in range(0, 4):
            rects_for_dir = []
            for col in range(0, 3):
                rects_for_dir.append((0, 32 * line, 32 * col + 32, 32 * line + 32))
            rects.append(rects_for_dir)
        self.sprite_bottom = spritesheet.images_at(rects[0])
        self.sprite_left = spritesheet.images_at(rects[1])
        self.sprite_right = spritesheet.images_at(rects[2])
        self.sprite_right = spritesheet.images_at(rects[3])
