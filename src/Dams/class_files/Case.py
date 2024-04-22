class Case:
    def __init__(self, is_point: bool, color: str, is_connected: bool = False):
        self.is_point = is_point
        self.color = color
        self.is_connected = is_connected

    def __str__(self):
        return f"Point: (is_point={self.is_point}, color={self.color}, connected={self.is_connected})"
    
    def __json__(self):
        return {'x': self.x, 'y': self.y}

    def is_free_point(self):
        """
        Returns:
            bool: True if the case is a point and the point is not connected to a path, False otherwise.
        """
        return self.is_point and not self.is_connected

    def is_right_point(self, color):
        """
            Checks if the case is a point of the specified color and is not connected to a path.
        """
        return self.color == color and not self.is_connected