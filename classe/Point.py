class Point:
    def __init__(self, position, color,neighbour=None, connected=False, pair=False):

        self.pos = position
        self.color = color

        self.neighbour = neighbour
        self.connected = connected
        self.pair = pair

    def __str__(self):
        return f"Point: (posx={self.pos.x}, posy={self.pos.y}, color={self.color}, neighbour={self.neighbour}, connected={self.connected}, pair={self.pair})"
    
    def __json__(self):
        return {'x': self.x, 'y': self.y}