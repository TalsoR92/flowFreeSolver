class Button:
    def __init__(self, rect, cell):
        self.rect = rect
        self.cell = cell

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)