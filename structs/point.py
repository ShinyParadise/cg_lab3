class Point:
    def __init__(self, x: float, y: float, color: tuple) -> None:
        self.color = color
        self.x = x
        self.y = y
        
    def multiply(self, factor: float) -> None:
        self.x *= factor
        self.y *= factor

    def __str__(self):
        return f"Point({self.x}, {self.y}) - Color: {self.color}"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.color == other.color

    def __ne__(self, other):
        return not self.__eq__(other)    
