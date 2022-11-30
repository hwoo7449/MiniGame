BLACK = (0,0,0)

class Text:
    def __init__(self, text, font, color = BLACK):
        self.font = font
        self.color = color
        self.text = font.render(text, True, color)
        self.rect = self.text.get_rect()

    def Draw(self, screen):
        screen.blit(self.text, self.rect)





















# Box_list = []
# class MovingBox:
#     global Box_list

#     def __init__(self, screen: pygame.Surface):
#         self.screen = screen
#         self.color = randomColor()
#         self.size_width = 10
#         self.size_height = 10
#         self.pos_x = (screen.get_width() + self.size_width)
#         self.pos_y = randint(10, screen.get_height() - self.size_height)
#         self.rect = [ self.pos_x, self.pos_y, self.size_width, self.size_height ]
#         self.dx = -randint(5, 15)

#     def Add(self):
#         Box_list.append(self)

#     def Del(self):
#         Box_list.remove(self)
#         del self
#         return

#     def Draw(self):
#         if self.rect[0] < -self.size_width:
#             self.Del()
#             return

#         pygame.draw.rect(self.screen, self.color, self.rect)

#     def Move(self):
#         self.rect[0] += self.dx

# def CheckBox():
#     if len(Box_list) < 10:
#         Box_list.append(MovingBox(screen))

# def AllBoxMove():
#     for i in Box_list:
#         i.Move()
#         i.Draw()

# def BG_Animation():
#     CheckBox()
#     AllBoxMove()