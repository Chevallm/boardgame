from spritesheet import SpriteSheet

class Player:
    def __init__(self, name = '', sprite = None, x = 0, y = 0):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        spritesheet = SpriteSheet(f'./assets/players/{sprite}.png')
        rects = []
        for line in range(0,4):
            rectsForDir = []
            for col in range (0,3):
                rectsForDir.append((0, 32*line, 32*col+32, 32*line+32))
            rects.append(rectsForDir)
        self.sprite_bottom = spritesheet.images_at(rects[0])
        self.sprite_left = spritesheet.images_at(rects[1])
        self.sprite_right = spritesheet.images_at(rects[2])
        self.sprite_right = spritesheet.images_at(rects[3])
            
        